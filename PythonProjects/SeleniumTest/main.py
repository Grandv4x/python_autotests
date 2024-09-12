import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2d6dea26bca329efd78a75d5e1a065d0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_regestration = {
    "trainer_token": TOKEN,
    "email": "Grandv4x@yandex.ru",
    "password": "Ker4ikru"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Generate",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "70244",
    "name": "Generate",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "70244"
}


'''response = requests.post (url = f'{URL}/trainers/reg', headers = HEADER, json = body_regestration )
print(response.text)
'''
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message = response_create.json()['id']
print(message)