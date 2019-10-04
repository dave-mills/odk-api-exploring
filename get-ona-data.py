import requests
import json

# add your Ona credentials here
# Actually, you should really put them into a seperate config file that is ignored in your version control...
# ...but this is just a simple example.
ona_username = ''
ona_password = ''


ona_data_url = 'https://api.ona.io/api/v1/data'

# Add the form id here
form_id = ''


headers = {'Content-Type': 'application/json'}


response = requests.get('%s/%s' % (ona_data_url,form_id),
                        headers=headers,
                        auth=(ona_username,ona_password)
                        );

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))

    with open('form_data.json', '+w') as outfile:
        json.dump(data, outfile)

    print('Done. Json file created')

else:
    print('Call to Ona returned status: %s' % response.status_code)
