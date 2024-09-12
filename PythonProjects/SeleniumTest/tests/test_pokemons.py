import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2d6dea26bca329efd78a75d5e1a065d0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4974'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200