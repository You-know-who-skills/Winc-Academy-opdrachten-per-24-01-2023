# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# Modules

'''
Question 1 = At the top of this file, import a module that prints the 'Zen of Python'.
'''

print('\n')

import this

print('\n')

'''
Import the following modules: time, math and sys.
'''

import time
import math
import sys

import greet as sp



'''
Also import the 'datetime object' from the 'datetime module'. Use an alias here (like 'dt' for example).
'''

import datetime as dt


'''
Write a function called 'wait' that takes one argument called 'seconds' (int), that uses a function in the time module to make the computer wait for that number of seconds and then returns nothing.
'''

def wait(seconds: int):

    # return "Hallo" # Deze return statement doet het dus ook.

    return time.sleep(seconds) # Deze code doet het ook. De sleep code telt het aantal ingevoerde seconden af en returnd daarna alles wat je in de return statement zet.


'''
Write a function called 'my_sin' that takes one float as an argument and returns the 'sine' of that float. Use the math module.
'''

def my_sin(float: float):

    return math.sin(float)


'''
Write a function called 'iso_now' that takes no arguments and returns a string containing the current date and time up to the minute in the ISO 8601 format. Use the datetime module.

Example: 2000-12-31T17:00.
'''

def iso_now():

    # return dt.datetime.now().isoformat()
    # return dt.datetime.isoformat(now)
    # return dt.datetime.isoformat()
    return dt.datetime.now()


'''
Write a function called 'platform' that takes no arguments and returns a string that shows which operating system (Linux, Windows, macOS, and so on) we are on. Use the sys module.
'''

def platform():

    return sys.platform



def supergreeting_wrapper(name):

    return from sp import greet.name




if __name__ == "__main__":

    print(wait(1)) # Deze code doet het.
    
    print('\n')
    
    print(my_sin(1.2))

    print('\n')

    print(iso_now())

    print('\n')

    print(platform())

    print('\n')

    print(supergreeting_wrapper)

    print('\n')