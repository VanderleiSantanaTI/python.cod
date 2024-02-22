lista = []


def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):  # Use _ pois não estamos usando o valor de 'i'
        lista.append(a)
        a, b = b, a + b  # Atualiza 'a' e 'b' para os próximos números da sequência


fibonacci(6)
print(lista)