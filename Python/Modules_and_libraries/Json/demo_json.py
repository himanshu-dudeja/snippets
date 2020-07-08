"""Javascript Object Notation"""

import json

def working_with_strings():

    people_string = """
    {
        "people": [
            {
                "name": "ABC",
                "phone": "12345",
                "emails": null,
                "has_license": false
            },
            {
                "name": "PQR",
                "phone": "123123",
                "emails": ["pqr@pqr.com"],
                "has_license": true
            }
        ]
    }
    """

    # Load a json string to python object
    # Loads -> here s refers to string
    data = json.loads(people_string)
    print(type(data))
    # print(data)

    # Dump a python object into a json string
    for person in data['people']:
        del person['phone']
    new_string = json.dumps(data, indent=2, sort_keys=True)
    print(new_string)


def working_with_files():

    with open('states.json') as f:
        data = json.load(f)

    for state in data['states']:
        print(state['name'], state['abbreviation'])
        del state['area_codes']

    with open('new_states.json', 'w') as f:
        json.dump(data, f, indent=2)


# working_with_strings()
# working_with_files()
