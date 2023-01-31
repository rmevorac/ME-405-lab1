import pyb
import encoder_reader, motor_driver

if __name__ == "__main__":
    moe = MotorDriver(Pin.board.PA10, Pin.board.PB4, Pin.board.PB5, 3)
    moe2 = MotorDriver(Pin.board.PC1, Pin.board.PA0, Pin.board.PA1, 5)
    moe.set_duty_cycle(-100)
    moe2.set_duty_cycle(100)

    encIn1 = Encoder(Pin.board.PB6, Pin.board.PB7, 4)
    encIn2 = Encoder(Pin.board.PC6, Pin.board.PC7, 8)
    real_time = pyb.millis()
    encIn1.dir_flag = 0 #depend on PWM input 1 = forward, 0 = backward
    encIn2.dir_flag = 1
    
    while(True):
        if pyb.elapsed_millis(real_time) >= 100:
            encIn1.read()
            encIn2.read()
            print(f"In1: {encIn1.position}")
            print(f"In2: {encIn2.position}")
            if encIn1.position > 10000:
                encIn1.zero()
            if encIn2.position > 10000:
                encIn2.zero()

            real_time = pyb.millis()
