import multiprocessing
import time

def fun(ri, r, lock):
    x = 0
    for i in range(ri):
        for j in range(10000):
            x += 1
    # Atualiza r de forma segura
    with lock:
        r.value += x

if __name__ == '__main__':
    start_time = time.time()  # tempo inicial

    r = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()  # cria um lock para sincronização

    p1 = multiprocessing.Process(target=fun, args=(2500, r, lock))
    p2 = multiprocessing.Process(target=fun, args=(2500, r, lock))
    p3 = multiprocessing.Process(target=fun, args=(2500, r, lock))
    p4 = multiprocessing.Process(target=fun, args=(2500, r, lock))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Resultado:", r.value)

    end_time = time.time()  # tempo final
    print("Tempo de execução:", end_time - start_time, "segundos")
