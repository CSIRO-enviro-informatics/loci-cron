# loci-cron.py
import requests
import re
import datetime
import json
import passwords as pwds
import assets


MESSAGES = []


def validate_endpoint_content(uri, pattern):
    # dereference the URI
    r = requests.get(uri)

    # parse the content looking for the thing specified in REGEX
    # print(r.content.decode('utf-8'))
    if re.search(pattern, r.content.decode('utf-8'), re.MULTILINE):
        return True
    else:
        return False


def add_validation_failure_to_list(asset_label, uri, pattern):
    MESSAGES.append('Asset \'{}\' failed URI {} with pattern "{}"'.format(asset_label, uri, pattern))


def make_error_message(messages):
    message = 'Failure messages from LOC-I cron for run {}:\n\n'.format(
        datetime.datetime.strftime(
            datetime.datetime.now(),
            '%Y-%m-%dT%H:%M'
        )
    )
    return message + '\n'.join(messages)


def send_email_via_mailjet(message, subject, to_addresses, secrets):
    recipients = []
    for to_address in to_addresses:
        recipients.append({'Email': to_address, 'Name': ''})
    data = {
        'Messages': [
            {
                'From': {
                    'Email': 'nicholas.car@csiro.au',
                    'Name': 'LCO-I cron bot'
                },
                'To': recipients,
                'Subject': subject,
                'TextPart': message
            }
        ]
    }

    r = requests.post(
        secrets['API_ENDPOINT'],
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'},
        auth=(secrets['MJ_APIKEY_PUBLIC'], secrets['MJ_APIKEY_PRIVATE'])
    )
    if r.status_code == 200:
        return True
    else:
        # print(r.content.decode('utf-8'))
        return False


if __name__ == '__main__':
    for asset in assets.ASSETS:
        print('validating ' + asset['label'])
        for uri in asset['uris']:
            print('uri: ' + uri['address'])
            if validate_endpoint_content(uri['address'], uri['regex']) is True:
                # do nothing as this passes
                pass
            else:
                # the validation has failed so add to failures list
                add_validation_failure_to_list(asset['label'], uri['address'], uri['regex'])

    # check for any failures and send to people
    if len(MESSAGES) > 0:
        print('Failures')
        message = make_error_message(MESSAGES)
        send_email_via_mailjet(message, 'Failures', pwds.emails, pwds.secrets)
    else:
        print('No failures')
        # no errors so send an 'OK' message to main maintainer only
        send_email_via_mailjet('No errors for this report', 'No failures', pwds.emails, pwds.secrets)

    print('done')
