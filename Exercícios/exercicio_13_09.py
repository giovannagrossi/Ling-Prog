import numpy as np 
import pandas as pd

ser_1 = pd.Series([1,2,3,4,5])
ser_2 = pd.Series([4,5,6,7,8])

serie_uniao = pd.Series(np.union1d(ser_1, ser_2))
print("Serie união: ", serie_uniao, sep = "\n")

serie_intersecao = pd.Series(np.intersect1d(ser_1, ser_2))
print("Serie interseção: ", serie_intersecao, sep = "\n")

passo_1 = serie_uniao.isin(serie_intersecao)
print("Passo 1: ",passo_1, sep = "\n" )

passo_2 = ~passo_1
print("Passo 2: ",passo_2, sep = "\n" )

print("\nResultado: ", serie_uniao[passo_2], sep = "\n")


