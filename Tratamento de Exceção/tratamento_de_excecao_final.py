x = 10
y = 0
z = 2

try:
    resultado = x/z
    print(resultado)
    #raise ValueError("Peso deve ser positivo")
except (NameError, ZeroDivisionError) as erro:
    print ("Errou feio! Erro: ", type(erro), erro.__class__.mro())
else:
    print("Se der certo cai aqui")
finally: 
    print("Foi uma honra estudar ao seu lado.")
    
"""
peso = -1

if peso < 0:
    raise ValueError("Peso deve ser positivo")    
"""    
    
    
    
    
    
    
    