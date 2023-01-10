from pyfirmata import Arduino

def led_islemleri(deger):
    board = Arduino("COM4")
    board.get_pin("d:2:o")
    board.get_pin("d:3:o")
    board.get_pin("d:4:o")
    if deger == 1:
        board.digital[2].write(1)
        board.digital[3].write(1)
        board.digital[4].write(1)
        board.exit()
    elif deger == 0:
        board.digital[2].write(0)
        board.digital[3].write(0)
        board.digital[4].write(0)
        board.exit()
