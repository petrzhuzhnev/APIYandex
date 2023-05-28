import requests
import json

url = 'https://akabab.github.io/superhero-api/api'
path = '/all.json'
respons = requests.get(url + path)
data = respons.json()
superhero_best = ['Hulk', 'Captain America', 'Thanos']
superhero_dict = {}
for superheros in data:
    if superheros['name'] in superhero_best:
        superhero_dict[superheros['name']] = superheros['powerstats']['intelligence']

print(*[k for k, v in superhero_dict.items() if v == max(superhero_dict.values())])
