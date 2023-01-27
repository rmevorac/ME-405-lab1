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


ena = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OD, pyb.pin.PULL_UP)
ena = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OD, pyb.pin.PULL_UP)

in1a = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.PP)
in2a = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.PP)
in1b = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.PP)
in2b = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.PP)

timer_3 = pyb.Timer(3, prescaler=0, period=0xFFFF)

enc_channel_PB1 = timer_3.channel(1, pyb.Timer.ENC_AB, pin = in1a)
enc_channel_PB2 = timer_3.channel(2, pyb.Timer.ENC_AB, pin = in2a)

timer_5 = pyb.Timer(5, prescaler=0, period=0xFFFF)

enc_channel_PA1 = timer_5.channel(1, pyb.Timer.ENC_AB, pin = in1b)
enc_channel_PA2 = timer_5.channel(2, pyb.Timer.ENC_AB, pin = in2b)






    