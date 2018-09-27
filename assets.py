ASSETS = [
    {
        'label': 'GN-NAF dataset',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/dataset/gnaf?_format=text/turtle',
                'regex': 'rdfs:label \"GNAF ontology\"'
            },
            {
                'address': 'http://gnafld.net/sparql?query=PREFIX%20gnaf%3A%20%3Chttp%3A%2F%2Fgnafld.net%2Fdef%2Font%23Address%3E%20SELECT%20(COUNT(%3Fs)%20AS%20%3Fc)%20WHERE%20%7B%3Fs%20a%20gnaf%3AAddress%20.%7D',
                'regex': 'value'  # to be changes to an actual number when there are Address objects in the triplestore
            }
        ]
    }
]