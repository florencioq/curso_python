def soma_ate(n: int) -> int:
    """Soma de zero até um certo número"""
    print("Anotações", soma_ate.__annotations__)
    soma = 0
    print("id n", id(n))
    for i in range(n + 1):
        soma = soma + i
    print("id soma", id(soma))
    return soma


def fib(n: int) -> list:
    """Gera uma lista com números de Fibonacci"""
    print("Anotações", fib.__annotations__)
    lista_fib = []
    a, b = 0, 1
    while a <= n:
        lista_fib.append(a)
        c = a + b
        a = b
        b = c
    return lista_fib