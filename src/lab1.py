"""	!@file		lab1.py
    @brief		This file runs the motor driver and encoder system. Testing every function and class.
    
    @author		Ben Elkayam
    @author		Roey Mevorach
    @author		Ermias Yemane
    @date		January 1 30 2023


"""
"""
@package Python inferface for micro-controller board utilities and tools. Necessary for pin and timer access
"""

from encoder_reader import Encoder
from motor_driver import MotorDriver
from pyb import Pin as Pin
import pyb

if __name__ == "__main__":
    """!@brief 			This is the python script that initializes 2 motors and 2 encoders and operates them.
                        These is an example of how the user would use the MotorDriver and Encoder classes.
    """
    ##Initializes motor 1 and its respective timer 5.
    #
    moe = MotorDriver(Pin.board.PC1, Pin.board.PA0, Pin.board.PA1, 5)
    ##Initializes motor 2 and its respective timer 3.
    #
    moe2 = MotorDriver(Pin.board.PA10, Pin.board.PB4, Pin.board.PB5, 3)

    #Sets motor 1's duty cycle to 100%.
    moe.set_duty_cycle(100)
    #Sets motor 2's duty cycle to 100%.
    moe2.set_duty_cycle(100)

    ##Initializes encoder 1 its respective timer 4.
    #
    encIn1 = Encoder(Pin.board.PB6, Pin.board.PB7, 4)
    ##Initializes encoder 2 its respective timer 4.
    #
    encIn2 = Encoder(Pin.board.PC6, Pin.board.PC7, 8)
    
    while(True):
#         if encIn1.position >= 2400000:
#             moe.set_duty_cycle(-100)

        #If encoder 1's position is >= 24000000, encoder 1's position is reset to 0 and the motor 1's duty cycle is set to 0%
        if encIn1.position >= 24000000:
            encIn1.zero()
            moe.set_duty_cycle(0)
            print(f"In1: {encIn1.position}")
            break
    
#         if encIn2.position >= 2400000:
#             moe2.set_duty_cycle(-100)

        #If encoder 2's position is >= 24000000, encoder 2's position is reset to 0 and the motor 2's duty cycle is set to 0%
        if encIn2.position >= 24000000:
            encIn2.zero()
            moe2.set_duty_cycle(0)
            print(f"In2: {encIn2.position}")

        #Calls encoder 1's and 2's read() and prints out each one's position
        encIn1.read()
        encIn2.read()
        print(f"In1: {encIn1.position}")
        print(f"In2: {encIn2.position}")
        