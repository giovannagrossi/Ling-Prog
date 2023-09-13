import numpy as np
import numpy.random as npr

"""
Comentários:
    Princípio da proximidade
    Princípio da simplicidade
    Princípio da não redundância
    Princípio do código limpo
    
    * Site: pep8.org
        "Como estilizar seu código"
"""

# Encontrar os valores comuns entre dois vetores

a1d_1 = np.array(range(0,15))
a1d_2 = np.array(range(10,20))

array_intersect = np.intersect1d(a1d_1 , a1d_2)

print(array_intersect)
print("#"*50)

# Em um vetor com 100 elementos (0-99), inverta os valores de 42 ate 66

a1d_3 = np.array(range(0,100))
a1d_3[(a1d_3>41) & (a1d_3<67)] *= -1 ## "C reduzido": a1d_3 = a1d_3 * -1
## Usamos filtro mas também dá pra usar slycing

print(a1d_3)
print("#"*50)

# Encontre o emelento de um vetor mais proximo de um dado valor

a1d_4 = npr.randint(1000, size = (4,4))

valor = npr.uniform(0,1000)
## Pega um valor entre 

aprox = np.abs(a1d_4 - valor).argmin()
## abs pega o módulo do elemento e argmin pega o índice do menor valor
## amin pegaria o menor valor

print(aprox)











