import numpy as np
import time

# Vetorização de funções

"""
inicio_tempo_loop = time.time()

vetor_loop = list(range(1,11))

for number in range(len(vetor_loop)):
    vetor_loop[number] = vetor_loop[number]**2


fim_tempo_loop = time.time()

print(f"Tempo de loop: ", fim_tempo_loop - inicio_tempo_loop)
#dá o tempo que gastou para compilar o codigo

### Em NumPy

inicio_tempo_vetorizacao = time.time()

vetor_numpy = np.array(range(1,11))

for number in range(len(vetor_loop)):
    vetor_numpy[number] = vetor_numpy[number]**2


fim_tempo_vetorizacao = time.time()

print(f"Tempo de loop: ", fim_tempo_vetorizacao - inicio_tempo_vetorizacao)
# o numpy tem um tempo de compilação muito menor (30 a 40x)
"""

def calcular_quadrado(num):
    #essa função não consegue trabalhar com numpy
    return num ** 2

vetor_loop = list(range(1,11))
vetor_numpy = np.array(range(1,11))


funcao_vetorizada = np.vectorize(calcular_quadrado)
#uma função vetorizada trabalha com qualquer tipo de elemento

print(funcao_vetorizada(vetor_numpy)) 
print(funcao_vetorizada(vetor_loop))







