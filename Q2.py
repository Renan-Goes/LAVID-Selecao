import re
import pandas as pd
import csv
import json

data = pd.read_csv("corpus-q2.csv")

dados = data['gr'].append(data['gi'])

palavraEncontrada = []
palavras = {}

for frase in dados:
    palavraEncontrada = re.findall(r'(?<![\[\]\(\)])\b[^\s]+(?<![\[\]\(\)])', frase) #considero que números também valem
                                                                                     #como palavras
    if palavraEncontrada:
        for palavra in palavraEncontrada:
            palavra = palavra.lower()

            if palavra not in palavras:
                palavras[palavra] = 1
            else:
                palavras[palavra] += 1

palavrasOrd = {p: valor for p, valor in sorted(palavras.items(), key = lambda item: -item[1])}

print(palavrasOrd)

with open('corpus-q2-resposta.json', 'w', encoding = 'utf-8') as q2resposta:
    json.dump(palavrasOrd, q2resposta, indent = 4, ensure_ascii = False)