import documentation_module as dm


print(dm.juros_simples(1000, 15.18, 12))
print(dm.juros_compostos(10000, 15.18, 12))

help(dm)
print("__main__")

print(f"__degub__ = {__debug__}")
# Ver se tá on
# O debug é o código depurado, com um módulo de asserts
# Nunca passe para o cliente o código depurado pois ele é mais pesado e também tem errinhos

if __debug__:
    print("Execução em modo normal")
else:
    print("Execução em modo otimizado")








