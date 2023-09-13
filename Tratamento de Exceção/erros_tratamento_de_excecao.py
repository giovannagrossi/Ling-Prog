# var -> 0/0 !ERRO sintático
# var = 0/ !ERRO aritmético

# Tratamento de execeção
"""
try:
    with open ("emap.fgv") as file:
        read_data = file.read()
except:
    print("Arquivo não existe")
"""

# x = 10
# y = 0


# resultado = x/y !ERRO 

"""
try:
    resultado = x/z
#    raise ZeroDivisionError 
# O raize "cria" o erro e ele é tratado no except
except Exception:
    print("Pega todas as exeções e o resto do código é irrelevante")
    
except NameError:
    print("Variável não existe")
except ZeroDivisionError:
    print("Não é possivel realizar a divisão")
except:
    # Se não for nenhum erro especificado
    print("")

# Checar a hierarquia de exceções na internet
"""

try:
    resultado = x / y  
except NameError as erro:
    print("Variável não existe", erro.__class__.mro())
    # mro() indica o caminho do erro e seu tipo
except Exception:
    print("Não é possível relizar a divisão")






