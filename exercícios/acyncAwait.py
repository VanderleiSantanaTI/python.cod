"""
Programação assíncrona: este programa executa duas funções simultaneamente.
Quando iniciadas, o resultado será retornado conforme o tempo de processamento de cada uma delas.
"""

import asyncio
import time


async def acao_1():
    await asyncio.sleep(2)
    cont = 0
    for i in range(10_000_000):
        cont += i
    print(f"momento funcao_1 {time.strftime('%X')}")
    print("Minha mensagem 1")


async def acao_2():
    await asyncio.sleep(1)
    cont = 0
    for i in range(10_000_000):
        cont += i

    print(f"momento funcao_2 {time.strftime('%X')}")
    print("Minha mensagem 2")


async def funcao_main():
    print(f"momento funcao_main {time.strftime('%X')}")
    task = asyncio.create_task(acao_1())
    task2 = asyncio.create_task(acao_2())
    await asyncio.gather(task, task2)
    # await task
    # await task2


asyncio.run(funcao_main())

