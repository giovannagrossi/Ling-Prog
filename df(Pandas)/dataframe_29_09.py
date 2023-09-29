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
print(df[df["Nota"]>8]["Temporadas"], end = "\n\n")

print(df[df["Nota"]>8][["Temporadas","Episódios"]], end = "\n\n")

print(df[(df["Nota"]>8) & (df["Temporadas"]>3)])

#INSERIR MATERIA FALTANTE
print("\n\n ############ MULTI index ###########")
plataforma = ["HBO", "HBO", "Netfilx", "Netfilx", "Prime"]
lancamento = ["2023", "2021", "2020", "2021", "2023"]
indices = pd.MultiIndex.from_arrays([plataforma, lancamento], names= ("Plataforma", "Lançamento"))


print("\n\nÍndices: ")
print(indices)
df.reset_index(inplace=True)
print(df)

print("Informar Índice")
df.rename(columns={"index" : "Nome"}, inplace = True)
print(df)

print("\nConfidgurar índice: ")
df.set_index(indices, inplace=True)
print(df)


print("\n######## Seleção Multiíndex #####")
selecionado = df.loc["HBO"]
selecionado_2 = df.loc["HBO"].loc["2021"]

print(selecionado)
print(selecionado_2)

print("\nCross Selection: ")
# Mesmo que loc
cross_1 = df.xs("HBO")
print(cross_1)

# Mesmo que loc
cross_2 = df.xs(("HBO", "2021"))
print(cross_2)

# Filtrando num level diferente
cross_3 = df.xs("2020", level="Lançamento")
print(cross_3)
# FIM DA MATÉRIA FALTANTE

print("##### OPERAÇÕES #####", "\n\n")

print("Unique: ", df["Nota"].unique())
print("Nunique: ", df["Nota"].nunique())
print("Count: ", df["Nota"].count())
print("\n")
print(df)

# edita a linha correspondente
df.at[("Netflix", 2023), "Nota"] = 7.8

print("Unique: ", df["Nota"].unique())
print("Nunique: ", df["Nota"].nunique())
print("Count: ", df["Nota"].count())

print("\n\n")


print("##### OPERAÇÕES AGREGADAS #####", "\n\n")

print("Mín.: ", df["Nota"].min())
print("Máx.: ", df["Nota"].max())
print("Median: ", df["Nota"].median())
print("Var.: ", df["Nota"].var())


print("##### DROP & FILL #####", "\n\n")

indices = ["Aluno 1", "Aluno 2", "Aluno 3"]
colunas = ["Nome", "Altura", "Sono Médio"]
dados = [["Giovanna Grossi", 173, 7],["Uriel Liann", 180, np.nan],["Pedro Tokar", 182, 6]]
df = pd.DataFrame(dados, index = indices, columns= colunas)
print(df, "\n\n")

print("Is Null:", df.isnull(), sep="\n")
print("\n", "Is Null:", df["Sono Médio"].isnull(), sep="\n")

# df.fillna(5, inplace = True) muda todos os na do df
# df["Sono Médio"].fillna(5, inplace = True) preenche na coluna

# ! O padrão do drop é alterar linhas
# df.dropna(inplace= True) dropa das linhas com na
df.dropna(thresh=2, inplace= True) # dropa os que tem mais que 2
print(df) 








