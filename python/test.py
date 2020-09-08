import requests
import json


with open('domain.txt', 'r') as d:
    domains = d.read().splitlines()
    with open ('response.txt', 'w') as f:
        for i in domains:

            url = 'https://www.virustotal.com/vtapi/v2/url/report'

            params = {'apikey': 'c87205136d3d1e987c85d0cca44810c373c2589dd029db1328b8b45f4a74773b', 'resource': i}

            response = requests.get(url, params=params)
            x = response.json()
        
            f.write(json.dumps(x, indent=4))

