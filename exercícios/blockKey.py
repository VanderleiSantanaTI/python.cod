import keyboard

while 1:
    try:
        keyboard.block_key("1")
        keyboard.block_key("2")
        keyboard.remap_key("c", "m")
        keyboard.remap_key("o", "a")
        keyboard.remap_key("m", "t")
        keyboard.remap_key("e", "o")

    except :

        pass
