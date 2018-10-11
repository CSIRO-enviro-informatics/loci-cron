ASSETS = [
    {
        'label': 'GN-NAF dataset',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/dataset/gnaf?_format=text/turtle',
                'regex': 'rdfs:label \"GNAF Linked Data dataset top-level Register\"'
            },
            {
                'address': 'SELECT%20(COUNT(%3Fs)%20AS%20%3Fc)%20WHERE%20%7B%3Fs%20a%20%3Chttp%3A%2F%2Flinked.data.gov.au%2Fdef%2Fgnaf%23Locality%3E%20.%7D',
                'regex': '150'
            }
        ]
    }
]
