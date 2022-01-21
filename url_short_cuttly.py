
# Required Py Libraries - [ Requirements.txt ]
# pip install requests

import requests

api_key = ' insert access token here '
url = input('Enter links to shorten: ')
api_url = f"https://cutt.ly?api/api.php?key={api_key}&short={url}"

data = requests.get(api_url).json()["url"]

if data ['status'] == 7:
  short_url = data['shortlink']
  print('SHORT URL: ', short_url)
else:
  print('!! ERROR SHORTENING URL :', data)


# Start by importing requests into our code.
# Next, we enter our API key.
# Then we ask the user for input URL.
# Also, we need to specify the api_url parameters.
# Then, we sent it to requests to get data.

# If data is valid, then we take the shortLink part of the data which is the shortened URL and we print it.
# If invalid, we return an error .

