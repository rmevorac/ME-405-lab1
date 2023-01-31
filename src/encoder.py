import pyb
from pyb import Pin as Pin

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
        
        
    def read
#         a = self.tim.counter()
#         b = self.tim.counter()
#         delta = b - a
#         if delta > 32768:
#             print("backwards")
#             
#         elif delta < 0:
#             print("backward")
        
            
        
if __name__ == "__main__":
    encIn1 = Encoder(Pin.board.PB6, Pin.board.PB7, 4)
    #encIn2 = Encoder(Pin.board.PC6, Pin.board.PC7, 8)
    old_delta_1, old_delta_2 = 0, 0 #make zero function
    real_time = pyb.millis()
    dir_flag = 1 #depend on PWM input 1 = forward, 0 = backward
    delta = 0
    
    while(True):
        if pyb.elapsed_millis(real_time) >= 10:
            new_delta_1 = encIn1.get_pos()
            delta_1 = new_delta_1 - old_delta_1
            
#             if new_delta_1 < old_delta_1: #big drop
#                 delta_1 = new_delta_1 + 65536 - old_delta_1
#             elif new_delta_1 > old_delta_1: #jump
#                 delta_1 = new_delta_1 - 65536 - old_delta_1
            
            
            if delta_1 >= 32768: #changes to backwards
                delta_1 -= 65536
                dir_flag = 0
                if new_delta_1 < old_delta_1 and dir_flag: #big drop
                    delta_1 = new_delta_1 + 65536 - old_delta_1
            if delta_1 <= -32768: #changes to forwards
                delta_1 += 65536
                dir_flag = 1
                if new_delta_1 > old_delta_1 and not dir_flag: #jump
                    delta_1 = new_delta_1 - 65536 - old_delta_1

 
                
                
#             else: #going backwards
#                 if delta_1 <= -32768: #changes to forwards
#                     #delta_1 += 65536
#                     dir_flag = 1
#                 elif new_delta_1 > old_delta_1: #jump
#                     delta_1 = new_delta_1 - 65536 - old_delta_1
                
            old_delta_1 = new_delta_1
            encIn1.position += delta_1
            print(f"delta1: {encIn1.position}")
            real_time = pyb.millis()
            





    
    
    


