import requests

# Создание покемона
url_create = 'https://pokemonbattle.me:5000/pokemons'

response_create = requests.post(url_create, json={
  "name": "Test4",
  "photo": 'https://dolnikov.ru/pokemons/05.png'
}, headers={'trainer_token': '6c8fd755111c3c19b705380aee95e04c'})
print(response_create.json())

# Смена имени покемона
url_update = 'https://pokemonbattle.me:5000/pokemons'

response_update = requests.put(url_update, json={
  "pokemon_id": "2854",
  "name": "Parampam",
  "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers={'trainer_token': '6c8fd755111c3c19b705380aee95e04c'})
print(response_update.json())

# Поймать покемона в покебол
url_catch = 'https://pokemonbattle.me:5000/trainers/add_pokeball'

param = {"pokemon_id": "2854"}
response_catch = requests.post(url_catch, json=param,
  headers={'trainer_token': '6c8fd755111c3c19b705380aee95e04c'})
print(response_catch.json()) #Ответ на запрос
print(param) #Отправленные данные


