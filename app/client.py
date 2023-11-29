import requests


response = requests.post('http://127.0.0.1:5000/advs/',
                         json={'header': 'ddsgd', 'description': 'erg', 'owner': 'user4'}
                         )

print(response.status_code)
print(response.text)