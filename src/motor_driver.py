"""! @file lab1.py Motor Driver  """
import pyb
import time

# yellow (channel A) leads for clockwise
# Blue (channel B) leads for clockwise

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        pin1 = pyb.Pin (in1pin, pyb.Pin.OUT_PP)
        pin2 = pyb.Pin (in2pin, pyb.Pin.OUT_PP)
        self.pin_en = pyb.Pin (en_pin, pyb.Pin.OUT_OD,pyb.Pin.PULL_UP)
        timer3 = pyb.Timer (3, freq=65535)
        timer3 = pyb.Timer (3, freq=65535)
        self.ch1 = timer3.channel (1, pyb.Timer.PWM, pin=pin1)
        self.ch2 = timer3.channel (2, pyb.Timer.PWM, pin=pin2)
        print ("Creating a motor driver")
        
    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        self.pin_en.value(True)
        if(level > 0):
            self.ch1.pulse_width_percent (0)
            self.ch2.pulse_width_percent (level)
            # do something
        elif(level < 0):
            self.ch1.pulse_width_percent (level)
            self.ch2.pulse_width_percent (0)
            
        print (f"Setting duty cycle to {level}")
        
if __name__ == "__main__":
    moe = MotorDriver (pyb.Pin.board.PA10,pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    moe.set_duty_cycle (-100)
        
        
        
        
        