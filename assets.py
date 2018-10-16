ASSETS = [
    {
        'label': 'GN-NAF dataset',
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
        'label': 'GA Samples, Surveys, Sites',
        'uris': [
            {
                'address': 'http://pid.geoscience.gov.au/sample/?_format=text/turtle',
                'regex': 'rdfs\:label \"Sample igsn\:AU1000082\"\^\^xsd:string ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/sample/AU239?_format=text/turtle',
                'regex': 'rdfs\:label \"Sample igsn:AU239\"\^\^xsd\:string ;'
            },
            # {
            #     'address': 'http://pid.geoscience.gov.au/survey/?_format=text/turtle',
            #     'regex': ''
            # },
            # {
            #     'address': 'http://pid.geoscience.gov.au/survey/801?_format=text/turtle',
            #     'regex': ''
            # },
            {
                'address': 'http://pid.geoscience.gov.au/site/ga/?_format=text/turtle',
                'regex': 'rdfs\:label \"Site 94\"\^\^xsd:string ;'
            },
            {
                'address': 'http://pid.geoscience.gov.au/site/ga/94?_format=text/turtle',
                'regex': 'rdfs\:label \"Site 94\"\^\^xsd\:string ;'
            }
        ]
    }
]
