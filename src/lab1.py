import pyb

pinb6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
pinb7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)

timer_4 = pyb.Timer(4, prescaler=0, period=0xFFFF)

enc_channel_B1 = timer_4.channel(1, pyb.Timer.ENC_AB, pin = pinb6)

enc_channel_B2 = timer_4.channel(2, pyb.Timer.ENC_AB, pin = pinb7)


    


pinc6 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.IN)
pinc7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN)

timer_8 = pyb.Timer(8, prescaler=0, period=0xFFFF)

enc_channel_C1 = timer_8.channel(1, pyb.Timer.ENC_AB, pin = pinc6)

enc_channel_C2 = timer_8.channel(2, pyb.Timer.ENC_AB, pin = pinc7)


ENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OD, pyb.pin.PULL_UP)
pinc7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.IN)




    