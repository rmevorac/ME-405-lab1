"""	!@file		encoder_reader.py
    @brief		This class handles the data coming in from the encoder and parses it for user readability and motor control
                
    
    @author		Ben Elkayam
    @author		Roey Mevorach
    @author		Ermias Yemane
    @date		January 1 30 2023


"""
"""
@package Python inferface for micro-controller board utilities and tools. Necessary for pin and timer access
"""
import pyb
##Used as a shorthand for pyb.pin inside logic
from pyb import Pin as Pin

class Encoder:
    """!@brief		This class implements a motor driver for an ME405 kit.
        @details	This class handles the set up and data managment of the encoders through utilzing the B7/B6 and C7/C6 pins and their respective and corresponding timers, timers 4 and 8.
                    This class also handles the encoder logic math to handle overflow, underflow and detection of directional changes from the motor.
    """

    def __init__(self, Apin, Bpin, timer):
    """!@brief			Creates an encoder object which contains the relevant pins and related timer to make the encoder functions.
        @param self		This paramater represents the chosen encoder by the user. The user can in this verion only utilize two possible encoders corresponding to 2 motors.
        @param Apin		This pin is used for one of the 2 channels which the quadrature encoder outputs to in order to determine direction.
        @param Bpin		This pin is used for one of the 2 channels which the quadrature encoder outputs to in order to determine direction.
        @param in2pin	This pin along side in1pin handles the direction of the motors spin.
        @param timer	This paramter is the timer assigned by the user to run the encoder counter. For this version of the driver to work, the pins and timer they represent must match.
    """
        ##Setting up the pin attribute for encoder's channel 1 
        #
        self.enc_chA = Pin(Apin, Pin.OUT_PP)
        ##Setting up the pin attribute for encoder's channel 2 
        #        
        self.enc_chB = Pin(Bpin, Pin.OUT_PP)
        ##Creating encoder attribute timer which will count the position of the motor in ticks
        #        
        self.tim = pyb.Timer(timer, prescaler=0, period=0xFFFF)
        ##Creating the channel off the encoders first pin to get readings to update the timer 
        #
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=self.enc_chA)
        ##Creating the second channel off the encoders second pin to get readings to update the timer
        #
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=self.enc_chB)
        ##Creating an attribute for the encoder which tracks total displacement
        #
        self.position = 0
        ##Creating an attribute for the encoder which tracks the previous delta from each sampling period
        #
        self.old_delta = 0
        ##Creating an attribute which is used as a flag to indicate direction of the motor spinning 
        #
        self.real_time = pyb.millis()
        print ("Creating Encoder")

        
    def read(self):
        """!@brief	This method handles the math and logic necessary to process and print the readings from the encoder and store them into counter
            @details	This method handles the encoder logic by appropriatley handling underflow and overflow when it detects a possible direction change
            @params	self	This paramater represents the chosen encoder by the user. The user can in this verion only utilize two possible encoders corresponding to 2 motors.


        """
        
        #if pyb.elapsed_millis(self.real_time) >= 100: ------- old code for debugging
        
        ##Handles the encoder sampling time. Set to 100 Hz to ensure rapid and accurate readings
        #
        pyb.delay(10)
        ##Gets new encoder value and calculates the delta value to run the filtering for under/over/direction
        #
        new_delta = self.tim.counter()
        delta_1 = new_delta - self.old_delta

        ##Checking for Overflow in the encoder readings and then sub-checking if the direction changed to backwards
        #
        if delta_1 <= 32768:
            delta_1 += 65536
            if new_delta > self.old_delta: #big drop
                delta_1 = new_delta - 65536 - self.old_delta
        ##Checking for Underflow in the encoder readings and then sub-checking if the direction changed to forwards
        #
        if delta_1 >= -32768:
            delta_1 -= 65536
            if new_delta < self.old_delta: #jump
                delta_1 = new_delta + 65536 - self.old_delta
        ## reassigning encoders attributes to updated values 
        #
        self.old_delta = new_delta
        self.position += delta_1
        ##antiquiated debugging code: leaving for future debugging use
        self.real_time = pyb.millis()
        
        
    def zero(self):
        """!@brief	This method sets the encoders zero position to the current position
            @params self	This paramater represents the chosen encoder by the user. The user can in this verion only utilize two possible encoders corresponding to 2 motors.

        """
        ##Sets the position attribute of the encoder to 0
        #
        self.position = 0