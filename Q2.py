import re
import pandas as pd
import csv
import json

data = pd.read_csv("corpus-q2.csv")

dados = data['gr'].append(data['gi'])

palavraEncontrada = []
palavras = {}

for line in dados:
    palavraEncontrada = re.findall(r'(?<!\S)(\w+)(?!\S)', line)

    if palavraEncontrada:
        for palavra in palavraEncontrada:
            palavra = palavra.lower()

            if palavra not in palavras:
                palavras[palavra] = 1
            else:
                palavras[palavra] += 1

print(palavras)

with open('corpus-q2-resposta.json', 'w', encoding = 'utf-8') as q2resposta:
    json.dump(palavras, q2resposta)