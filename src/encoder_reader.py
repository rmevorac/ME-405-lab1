import pyb
from pyb import Pin as Pin
import motor_driver.py
class Encoder:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__(self, Apin, Bpin, timer):
        """! 
        Creates aencoder channels by initializing GPIO
        pins. 
        @param en_pin (There will be several pin parameters)
        """
        self.enc_chA = Pin(Apin, Pin.OUT_PP)
        self.enc_chB = Pin(Bpin, Pin.OUT_PP)
        self.tim = pyb.Timer(timer, prescaler=0, period=0xFFFF)
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=self.enc_chA)
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=self.enc_chB)
        self.position = 0
        self.old_delta = 0
        self.dir = 0 #need to set using PWM 
        print ("Creating Encoder")


    def get_pos(self):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        #print (f"Setting duty cycle to {level}")
        return self.tim.counter()
        
        
    def read(self):
        new_delta = self.get_pos()
        delta_1 = new_delta - self.old_delta

        if delta_1 >= 32768: #changes to backwards
            delta_1 -= 65536
            self.dir_flag = 0
            if new_delta < self.old_delta and self.dir_flag: #big drop
                delta_1 = new_delta + 65536 - self.old_delta
        if delta_1 <= -32768: #changes to forwards
            delta_1 += 65536
            self.dir_flag = 1
            if new_delta > self.old_delta and not self.dir_flag: #jump
                delta_1 = new_delta - 65536 - self.old_delta
        self.old_delta = new_delta
        self.position += delta_1

if __name__ == "__main__":
    encIn1 = Encoder(Pin.board.PB6, Pin.board.PB7, 4)
    encIn2 = Encoder(Pin.board.PC6, Pin.board.PC7, 8)
    real_time = pyb.millis()
    encIn1.dir_flag = 1 #depend on PWM input 1 = forward, 0 = backward
    encIn2.dir_flag = 1
    
    while(True):
        if pyb.elapsed_millis(real_time) >= 100:
            encIn1.read()
            encIn2.read()
            print(f"In1: {encIn1.position}")
            print(f"In2: {encIn2.position}")

            real_time = pyb.millis()