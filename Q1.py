import re
import csv
import pandas as pd

data = pd.read_csv("corpus-q1-v2.csv")

saida = data.replace(to_replace = r'(S|P)(1-3)', value = r'\2\1', regex = True)

saida = saida.replace(to_replace = r'(\()+(\+)+(\))+', value = r'(+)', regex = True)

saida = saida.replace(to_replace = r'\s+', value = r' ', regex = True)

saida = saida.replace(to_replace = r'\d-+\d', value = r'', regex = True)

saida = saida.replace(to_replace = r'(\s)+(_)(CIDADE|ESTADO|PAÍS)', value = r'_\3', regex = True) #considerei que podiam haver
                                                                                                  #vários espaços antes do lugar

saida = saida.replace(to_replace = r'[\s_{1}]+(1S|2S|3S|1P|2P|3P)\b', value = r'_\1', regex = True) #tratei os casos de ter vários
                                                                                                    #de ter vários espaços antes

saida = saida.replace(to_replace = r'\b(1S|2S|3S|1P|2P|3P)(_)(?<=\w)+', value = r'\1\2 ', regex = True) #considerei que deveria
                                                                                                        #ter algum caractere depois do direcional

saida = saida.replace(to_replace = r'(.)(\s)(\(\++)', value = r'\1\3', regex = True) #considerei que poderia haver mais um '+' por não
                                                                                    # #saber se dever ser apenas 1 '+' para intensidade

saida = saida.replace(to_replace = r'(NÃO)(\s)+(\w)', value = r'\1_\3', regex = True) #considerei que poderiam haver vários espaços entre
                                                                                      #"NÃO" e a palavra

saida = saida.replace(to_replace = r'([a-zA-Z])(_)(FAMOSO|FAMOSA)', value = r'\1&\3', regex = True) #considerei que _FAMOSO/FAMOSA
                                                                                                    #deveria vir depois de uma palavra

saida = saida.replace(to_replace = r'(\.)([^0-9])', value = r'\2', regex = True)

saida = saida.replace(to_replace = r'(\s)+(\.)([0-9])', value = r' 0\2\3', regex = True) #considerei que deveria haver espaõ antes do número

print(saida)

saida.to_csv('corpus-q1-resposta.csv')