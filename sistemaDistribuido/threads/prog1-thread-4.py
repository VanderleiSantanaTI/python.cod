import threading
import time

r = 0
lock = threading.Lock()

def fun(ri):
    global r
    x = 0
    for i in range(ri):
        for j in range(10000):
            x += 1
    with lock:
        r += x

start_time = time.time()  # tempo inicial

t1 = threading.Thread(target=fun, args=(2500,))
t2 = threading.Thread(target=fun, args=(2500,))
t3 = threading.Thread(target=fun, args=(2500,))
t4 = threading.Thread(target=fun, args=(2500,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

end_time = time.time()  # tempo final

print("Resultado:", r)
print("Tempo de execução:", end_time - start_time, "segundos")
