import time
x=0
inicio = time.time()

for i in range(10000):
  for j in range(10000):
    x=x+1

fim = time.time()

print("Resultado de x:", x)
print("Tempo de execução:", fim - inicio, "segundos")