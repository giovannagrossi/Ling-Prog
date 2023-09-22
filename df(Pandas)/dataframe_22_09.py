import numpy as np
import pandas as pd

print("##### Criando DATAFRAMES #####")

indices = ["Bridgerton", "B99", "The Office", "Gotham", "Community"]
colunas = ["Nota", "Temporadas","Episódios"]
dados = [[7.4, 2, 16],[8.4,8,153],[9.0,9,201],[7.8,5,100],[8.5,6,100]]

df = pd.DataFrame(dados, index = indices, columns = colunas)

print(df, end = "\n\n")


print("##### SELEÇÃO #####", end = "\n\n")
print("Notas:")
print(df["Nota"],end = "\n\n")
# print(df.Nota, end = "\n\n") #SQL !!Não fazer assim!!

print("Temporadas e episódios:")
print(df[["Temporadas","Episódios"]], end = "\n\n")

print("##### Loc ILOC #####", end = "\n\n")
print("Gotham:")
print(df.loc["Gotham"] ,end = "\n\n")
print(df.iloc[3] ,end = "\n\n")

print("Gotham, Temporadas:", end = " ")
print(df.loc["Gotham","Temporadas"] ,end = "\n\n")

print("##### SELÇÃO COMBINADA #####", end = "\n\n")
print(df.loc[["Gotham", "The Office"],"Episódios"] ,end = "\n\n")

# Tudo no slycing funciona em loc/iloc
print(df.loc[:,["Temporadas", "Nota"]] ,end = "\n\n")

print("##### TYPES #####", "\n\n")
print(type(df.loc[:,["Temporadas", "Nota"]]))
print(type(df["Nota"]))
print(type(df.loc["Bridgerton"]))

print("\n")

print(df.columns) 
print(type(df.columns)) #Tipo especial que pode ser tratado como série
print(df.columns.values)
print(type(df.columns.values))

print("\n")

print(df.index) 
print(type(df.index)) #Tipo especial que pode ser tratado como série
print(df.index.values)
print(type(df.index.values))

print("\n")

print("##### ALTERANDO O DF #####", "\n\n")
df["Coluna Extra"] = df["Nota"]
print(df, end = "\n\n")

# df.drop("Coluna Extra", axis=1, inplace = True) !! Perigoso
df2 = df.drop("Coluna Extra", axis=1)
print(df2, end = "\n\n")

df2 = df.drop("Gotham", axis=0)
print(df2, end = "\n\n")

# print(df.shape) !O valor do axis vem daqui

print("##### SELEÇÃO CONDICIONAL #####", "\n\n")
print(df[df["Nota"]>8], end = "\n\n")

print(df>3, end= "\n\n") #retorna boleano
# print(df[df>3]) #meio inútil mas pode ser usado dependendo

print("##### SELEÇÃO CONDICIONAL + MÚLTIPLA #####", "\n\n")
print(df[df["Nota"]>8]["Temporadas"])




