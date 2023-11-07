from tkinter import WORD
import requests

api_key = '32c9f4da-3262-490a-bfa5-6837f8794b66'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{WORD}?key={api_key}'
word = 'potato'

#root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
#final_url = f'{root_url}/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()

for definitions in definitions:
        print(definitions)