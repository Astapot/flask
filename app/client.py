import requests


response = requests.get('http://127.0.0.1:5000/advs/1',
                         json={'header': 'drhd', 'description': 'erg', 'owner': 'user4'}
                         )

print(response.status_code)
print(response.text)