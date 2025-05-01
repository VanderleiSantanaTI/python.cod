import multiprocessing
import time  # importa o módulo de tempo

def fun1(f1):
    x = 0
    for i in range(5000):
        for j in range(10000):
            x += 1
    f1.value = x

def fun2(f2):
    x = 0
    for i in range(5000):
        for j in range(10000):
            x += 1
    f2.value = x

if __name__ == '__main__':
    start_time = time.time()  # marca o tempo inicial

    f1 = multiprocessing.Value('i', 0)
    f2 = multiprocessing.Value('i', 0)

    p1 = multiprocessing.Process(target=fun1, args=(f1,))
    p2 = multiprocessing.Process(target=fun2, args=(f2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    x = f1.value + f2.value
    print("Resultado:", x)

    end_time = time.time()  # marca o tempo final
    print("Tempo de execução:", end_time - start_time, "segundos")
