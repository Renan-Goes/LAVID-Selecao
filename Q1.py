import re
import csv
import pandas as pd

data = pd.read_csv("corpus-q1.csv")

saida = data.replace(to_replace = r'(S|P)([1-3])', value = r'\2\1', regex = True)

saida = saida.replace(to_replace = r'(\()+(\+)+(\))+', value = r'(+)', regex = True)

saida = saida.replace(to_replace = r'\s+', value = r' ', regex = True)

saida = saida.replace(to_replace = r'\b-+\b', value = r'', regex = True)

saida = saida.replace(to_replace = r'(\s)+_', value = r'_', regex = True)

saida = saida.replace(to_replace = r'(1S|2S|3S|1P|2P|3P)(_)([a-zA-Z])', value = r'\1\2 \3', regex = True)

saida = saida.replace(to_replace = r'(.)(\s)(\(\++)', value = r'\1\3', regex = True) #considerei que poderia haver mais um '+' por não
                                                                                    # #saber se dever ser apenas 1 '+' para intensidade
saida = saida.replace(to_replace = r'(NÃO)(\s)(\w)', value = r'\1_\3', regex = True)

saida = saida.replace(to_replace = r'([a-zA-Z])(_)(FAMOSO|FAMOSA)', value = r'\1&\3', regex = True) #considerei que _FAMOSO/FAMOSA
                                                                                                    #deveria vir depois de uma palavra
saida = saida.replace(to_replace = r'(\.)([^0-9])', value = r'\2', regex = True)

saida = saida.replace(to_replace = r'(\s)(\.)([0-9])', value = r' 0\2\3', regex = True)

print(saida)

saida.to_csv('corpus-q1-resposta.csv')