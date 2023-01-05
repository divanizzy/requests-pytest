import requests
import pytest

url = 'https://pokemonbattle.me:5000/trainers'
def test_statuscode():
    response = requests.get(url, params={'trainer_id': '1691'})
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get(url, params={'trainer_id': '1691'})
    assert response.json()["trainer_name"] == "divanizzy_boom"