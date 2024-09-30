import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://fuzhuang.1688.com/nanzhuang?spm=a260k.dacugeneral.home2019category.2.663335e4bwa222'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with the result.
pprint(response.json())
