import asyncio






async def main():
    print('Hello 1 ...')
    # await asyncio.sleep(1)
    print('... World! 1')


async def main2():
    print('Hello 2 ...')
    # await asyncio.sleep(1)
    print('... World! 2')


async def main3(nome=None):
    if nome is None:
        nome = ""
    print('Hello 3...')
    # await asyncio.sleep(1)
    print(f'... World! 3 {nome}')


def exe():
    print("fun1")


def exe_2():
    print("fun2")


# exe()

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main2())
    asyncio.run(main3(nome=13))
    exe()
