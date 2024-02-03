from schedule import every, repeat, run_pending, CancelJob
import time
import pyautogui


@repeat(every(4).seconds)
def job():
    print("I am a scheduled job")
    # return CancelJob # para rodar uma única vez


@repeat(every(8).seconds)
@repeat(every(2).seconds)
def job2():
    print("I am a scheduled job 2")


@repeat(every(3).seconds, 'não')
def job3(nome, defaul=12):
    print(f"I am a scheduled job 3 {nome}")


while True:
    run_pending()
    time.sleep(1)
