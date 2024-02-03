import schedule
import time

nome = "vazio"
def job1(nome):
    # Do some work that only needs to happen once...
    print(nome)

def job2(nome="vazio" if nome=="" else None):

    # Do some work that only needs to happen once...
    print(f'sou eu agora {nome}')


schedule.every().day.at('17:13').do(job1, nome= "qualque")
schedule.every(1).hours.until("2030-01-01 18:33").do(job1)
schedule.every(1).seconds.do(job2, nome="")
schedule.every(5).to(10).seconds.do(job1, nome='nome1')

while True:
    schedule.run_pending()
    time.sleep(1)
