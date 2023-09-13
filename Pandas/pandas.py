import numpy as np 
import pandas as pd

"""
Pandas
     é dependente no NumPy

Séries
    é o encapsulamento de um NParray
    só trabalha com array de dimensão 1
    a indexação pode ser atrubuída
    índice à esquerda e valores à direita
    tudo que funciona em ND1 funciona em Séries
"""

lista_1 = [1,2,3,4,5]
lista_2 = ["I", "II", "III", "IV", "V"]

dicionario_1 = {"I":1, "II":2, "III":3, "IV":4, "V":5}

ndarray_1 = np.array(lista_1)

"""
print(lista_1)
print(lista_2)
print(dicionario_1)
print(ndarray_1)
print("#"*60)
"""

ser_1 = pd.Series(lista_1)
print("\nLista 1:", ser_1, sep = "\n")

ser_1 = pd.Series(lista_2)
print("\nLista 2:", ser_1, sep = "\n")

### Relembrar é viver
print("\nSer Shape: ", ser_1.shape)
print("\nSer Values: ", ser_1.values)
print("\nSer Type: ", type(ser_1.values))
print("\nSer Index: ", ser_1.index)
print("#"*60)


ser_1 = pd.Series(lista_1, lista_2)
print("\nLista 1 e Lista 2:", ser_1, sep = "\n")
## (data, index)

ser_1 = pd.Series(dicionario_1)
print("\nDicionário 1:", ser_1, sep = "\n")
print("#"*60)

ser_1 = pd.Series(ndarray_1)
print("\nNDarray 1:", ser_1, sep = "\n")

ser_1 = pd.Series(ndarray_1, lista_2)
print("\nNDarray 1 e Lista 2:", ser_1, sep = "\n")

print("\nNumPy para Lista: ", ndarray_1.tolist())
print("\nSerie para NumPy: ", ser_1.to_numpy())
print("\nSerie para Lista: ", ser_1.tolist()) #ou (to_list) em pandas
print("#"*60)

### Acessando os elementos
print("\nAcessando os elementos: ", ser_1[:3], sep = "\n")
print("\nAcessando os elementos: ", ser_1.head(3), sep = "\n")
## o próprio índice tem um índice

print("\nAcessando os elementos: ", ser_1.tail(3), sep = "\n")
print("\nAcessando os elementos: ", ser_1[-3:], sep = "\n")

print("\nAcessando os elementos: ", ser_1[0])
print("\nAcessando os elementos: ", ser_1["I"])

print("\nIndex Max: ", ser_1.idxmax())
print("\nIndex Min: ", ser_1.idxmin())

#localizando com indice (loc) e indice do indice (iloc)
print("\nLOC: ", ser_1.loc["I":"III"], sep = "\n")
print("\nILOC: ", ser_1.iloc[0:3], sep = "\n")

ser_1 = pd.Series(lista_1)

#print("\nLOC: ", ser_1.loc["I":"III"], sep = "\n") 
#ERRO pq n tem string como indice
print("\nLOC: ", ser_1.loc[0:3], sep = "\n")
print("\nILOC: ", ser_1.iloc[0:3], sep = "\n")
print("#"*60)

"""
i = 1_500_000
print(i)
!só vale em python
"""

dicionario_2 = {"I":10, "II":42, "III":7, "V":1_000_000}
dicionario_3 = {"I":1, "II":12, "III":13, "IV":0}

ser_2 = pd.Series(dicionario_2)
ser_3 = pd.Series(dicionario_3)

print("\nDicionário 2:", ser_2, sep = "\n")
print("\nDicionário 3:", ser_3, sep = "\n")


