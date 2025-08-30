from numba import njit
import time
x=0

# @njit
def increment():
  x=0
  for i in range(10377483010):
    for j in range(9999999):
      x += 1
      if x > 488398989483:
        return x
      
  return x

inicio = time.time()
x = increment()
fim = time.time()

print("Resultado de x:", x)
print("Tempo de execução:", fim - inicio, "segundos")