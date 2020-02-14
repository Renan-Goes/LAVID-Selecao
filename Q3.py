import re
import pandas as pd

data = pd.read_csv('corpus-q3.csv')

dados = data['gr'].append(data['gi'])

with open('corpus-q3-resposta.txt', 'w') as q3resposta:
    for frase in dados:
        fraseDirecional = re.search(r'\b(1|2|3)(P|S)\w+?(1|2|3)(P|S)\b', frase)
        if fraseDirecional:
            for letraPrimeira in ['S', 'P']:
                frase = re.sub(r'\b(1|2|3)(P|S)', r'\1'+letraPrimeira, frase)
                for i in range(1, 4):
                    frase = re.sub(r'\b(1|2|3)(P|S)', str(i)+r'\2', frase)
                    for letraSegunda in ['S', 'P']:
                        frase = re.sub(r'(\w+)(1|2|3)(P|S)\b', r'\1\2'+letraSegunda, frase)
                        for j in range(1, 4):
                            frase = re.sub(r'(1|2|3)(P|S)\b', str(j)+r'\2', frase)
                            q3resposta.write(frase+'\n')
        else:
            print(frase)
            q3resposta.write(frase+'\n')