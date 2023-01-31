from encoder_reader import Encoder
from motor_driver import MotorDriver
from pyb import Pin as Pin
import pyb


if __name__ == "__main__":
    moe = MotorDriver(Pin.board.PC1, Pin.board.PA0, Pin.board.PA1, 5)
    moe2 = MotorDriver(Pin.board.PA10, Pin.board.PB4, Pin.board.PB5, 3)
    moe.set_duty_cycle(100)
    moe2.set_duty_cycle(100)

    encIn1 = Encoder(Pin.board.PB6, Pin.board.PB7, 4)
    encIn2 = Encoder(Pin.board.PC6, Pin.board.PC7, 8)
    
    while(True):
#         if encIn1.position >= 2400000:
#             moe.set_duty_cycle(-100)
        if encIn1.position >= 24000000:
            encIn1.zero()
            moe.set_duty_cycle(0)
            print(f"In1: {encIn1.position}")
            break
    
#         if encIn2.position >= 2400000:
#             moe2.set_duty_cycle(-100)
        if encIn2.position >= 24000000:
            encIn2.zero()
            moe2.set_duty_cycle(0)
            print(f"In2: {encIn2.position}")
            
            
        encIn1.read()
        encIn2.read()
        print(f"In1: {encIn1.position}")
        print(f"In2: {encIn2.position}")
        