import time


x = 0

def fun1():
    global x
    for i in range(5000):
        for j in range(10000):
            x = x + 1

def fun2():
    global x
    for i in range(5000):
        for j in range(10000):
            x = x + 1


inicio = time.time()

fun1()
fun2()


fim = time.time()

print("Resultado de x:", x)
print("Tempo de execução:", fim - inicio, "segundos")
