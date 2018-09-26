# loci-cron.py
import requests
import re
import datetime


ASSETS = [
    {
        'label': 'GN-NAF dataset',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/dataset/gnaf?_format=text/turtle',
                'regex': 'rdfs:label \"GNAF ontology\"'
            }
        ]
    }
]

MESSAGES = []

EMAIL_ADDRESSES = []


def validate_endpoint_content(uri, pattern):
    # dereference the URI
    r = requests.get(uri)

    # parse the content looking for the thing specified in REGEX
    # print(r.content.decode('utf-8'))
    if re.search(pattern, r.content.decode('utf-8'), re.MULTILINE):
        return True
    else:
        return False


def add_validation_to_failures_list(asset_label, uri, pattern):
    MESSAGES.append('Asset \'{}\' failed URI {} with pattern "{}"'.format(asset_label, uri, pattern))


def make_error_message(messages):
    message = 'Failure messages from LOC-I cron for run {}:\n\n'.format(
        datetime.datetime.strftime(
            datetime.datetime.now(),
            '%Y-%m-%dT%H:%M'
        )
    )
    message = message + '\n'.join(messages)
    return message


def send_email_via_mailjet(message, email_addresses, api_keys):
    api_key = api_keys['MJ_APIKEY_PUBLIC']
    api_secret = api_keys['MJ_APIKEY_PRIVATE']
    data = {
        'FromEmail': 'loci-cron@csiro.au',
        'FromName': 'LOC-I cron',
        'Subject': 'LOC-I cron report for {}'.format(
            datetime.datetime.strftime(
                datetime.datetime.now(),
                '%Y-%m-%dT%H:%M'
            )
        ),
        'Text-part': message,
        'Html-part': '',
        'Recipients': [
            {
                'Email': ','.join(email_addresses)
            }
        ]
    }

    r = requests.post(
        'https://api.mailjet.com/v3/send',
        data=data,
        headers={'Content-Type': 'application/json'},
        auth=(api_key, api_secret)
    )
    print(r.status_code)
    print(r.content.decode('utf-8'))


if __name__ == '__main__':
    for asset in ASSETS:
        print('validating ' + asset['label'])
        for uri in asset['uris']:
            print('uri: ' + uri['address'])
            if validate_endpoint_content(uri['address'], uri['regex']) is True:
                # do nothing as thuis passes
                pass
            else:
                # the validation has failed so add to failures list
                add_validation_to_failures_list(asset['label'], uri['address'], uri['regex'])

    # check for any failures and send to people
    import passwords as passes

    api_keys = {
        'MJ_APIKEY_PUBLIC': passes.MJ_APIKEY_PUBLIC,
        'MJ_APIKEY_PRIVATE': passes.MJ_APIKEY_PRIVATE
    }
    if len(MESSAGES) > 0:
        message = make_error_message(MESSAGES)
        send_email_via_mailjet(message, EMAIL_ADDRESSES, api_keys)
    else:
        # no errors so send an 'OK' message to main maintainer only
        send_email_via_mailjet('no errors for this report', ['nicholas.car@csiro.au'], api_keys)

    print('done')
