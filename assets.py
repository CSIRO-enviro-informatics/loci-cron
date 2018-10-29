ASSETS = [
    {
        'label': 'G-NAF dataset',
        'uris': [
            {
                'address': 'http://linked.data.gov.au/dataset/gnaf?_format=text/turtle',
                'regex': 'dct:description \"A Linked Data API accessing all of the content of the GNAF in RDF \& HTML\"'
            },
            {
                'address': 'http://gnafld.net/sparql?query=SELECT(COUNT(%3Fs)AS%20%3Fc)%20WHERE%20%7B%20%3Fs%20a%20%3Chttp%3A%2F%2Flinked.data.gov.au%2Fdef%2Fgnaf%23Locality%3E%20.%20%7D',
                'regex': '15926'
            }
        ]
    },
    {
        'label': 'Geofabric dataset',
        'uris': [
            {
                'address': 'http://geofabricld.net/',
                'regex': '<h1>Geofabric - distributed as Linked Data</h1>'
            }
        ]
    }
]
