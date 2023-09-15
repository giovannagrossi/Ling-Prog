# O Doctest confere a documentação e testa se tudo está nos conformes.

import doctest 

def soma(num1,num2):
    """
    Texto incrível
    
    Parameters
    ----------
    num1 : int
        Número 1.
    num2 : int
        Número 2.

    Returns
    -------
    int
        Soma dos números.
        
    Explicação incrível do teste...
    >>> soma(42, 666)
    708
    
    Texto do teste 2...
    >>> soma(7,0)
    7.0
    
    Texto do teste 3...
    >>> soma(-13, 10)
    -3
    
    Texto do teste 4...
    >>> soma(1, "Yuri")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return num1+num2

#if __name__ == "__main__":
#    doctest.testmod(verbose = True)
#    print("Eu sou main!!!")


if __name__ == "__main__":
    doctest.testfile("teste.txt",verbose = True)
    print("Eu sou main!!!")












