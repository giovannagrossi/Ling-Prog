""" Documentação do módulo

blá-blá-blá

"""

# Função que calcula montante e juros em um regime de juros simples

# Type hint: MyPy (programa que te avisa onde tá estranho)
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple:
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    # TODO: Alterar estrutura de dados de retorno para lista
    # TODO: Limitar motante e capital a dois dígitos decimais
    # BUG/FIXME:
    return(montante, juros)    


def juros_compostos(capital, taxa, tempo):
    """Cálculo de Juros Compostos
    Parameters
    ----------
    capital : int
        blá-blá-blá
    taxa : float
        blá-blá-blá
    tempo : int
        blá-blá-blá

    Returns
    -------
    tuple
        blá-blá-blá

    """
    montante = capital * (pow((1 + taxa / 100), tempo))
    juros = montante - capital

    return(round(montante,2), round(capital,2))




