"""	!@file		motor_driver.py
    @brief		This class handles the pwm input from the user to each specific motor.
                This class specifically sets up the timers and channels for the motors
    
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


# yellow (channel A) leads for clockwise
# Blue (channel B) leads for clockwise

class MotorDriver:
    """!@brief	 This class implements a motor driver for a generic motor attached to the nucleo and its H bridge shield.
        @details	This class takes pins put in by the user to set up a motor timer and motor channel. The pins used by this version
                    are PA10, PB4 and PB5 with timer channel 3 for motor 1 and PC1, PA0 and PA1 with timer channel 5 for motor 2 .
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer_num):
    """!@brief 			Creates a motor driver by initializing GPIOpins and turning off the motor for safety.
        @param self		This paramater represents the chosen motor by the user. The user can in this verion only utilize two possible motors.
        @param en_pin	This pin is reserved for the motor driver pin and handles the connection between the CPU and the H bridge.
        @param in1pin	This pin along side in2pin handles the direction of the motors spin.
        @param in2pin	This pin along side in1pin handles the direction of the motors spin.
        @param timer_num	This paramter is the timer assigned by the user to run the motor. For this version of the driver to work, the pins and timer they represent must match.
    """
        ##Setting pin1 for the motor controller to the in1pin
        #
        pin1 = Pin(in1pin, Pin.OUT_PP)
        ##Setting pin2 for the motor controller to the in2pin
        #        
        pin2 = Pin(in2pin, Pin.OUT_PP)
        ##Creating the timer for which the motor runs off of. The prescaler and frequency default to 0 and 0xFFFF in order to align with our encoder code
        #        
        timer = pyb.Timer(timer_num, freq=0xFFFF)
        ##The following variables set up the ENx pin for H bridge communication and additional set up timer channels to recieve the PWM signals
        #        
        self.pin_en = Pin(en_pin, Pin.OUT_OD, Pin.PULL_UP)
        self.ch1 = timer.channel(1, pyb.Timer.PWM, pin=pin1)
        self.ch2 = timer.channel(2, pyb.Timer.PWM, pin=pin2)
        print("Creating a motor driver")
        
    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param	self	This paramater represents the chosen motor by the user. The user can in this verion only utilize two possible motors.
        @param	level	A signed integer holding the duty cycle of the voltage sent to the motor
        """
        ##Setting the ENx pin to high in order to activate the motor
        #    
        self.pin_en.value(1)
        ##Parsing user input for the PWM duty cycle for a positive spin
        #
        if level < 0:
            self.ch1.pulse_width_percent(-1 * level)
            self.ch2.pulse_width_percent(0)
        ##Parsing user input for the PWM duty cycle for a negative spin
        #
        elif level > 0:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(level)
        ##Parsing user input for the PWM duty cycle for a 0 input pwm signal
        #
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(0)
            
        print (f"Setting duty cycle to {level}")