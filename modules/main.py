# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# Modules

# import this

import time
import math
import sys
import datetime as dt
# from datetime import datetime



def wait(seconds: int):

    from time import sleep # De sleep code telt het aantal ingevoerd seconden af en returnd dan wat 

    time.sleep(seconds) # Deze code met onderstaande "Hallo" return statement doen het ook.

    return "Hallo" 

    # return time.sleep("seconds") # Deze code doet het.


def my_sin(float: float):

    from math import sin

    return math.sin(float)


def iso_now():

    from dt import sin

    return math.sin(float)





if __name__ == "__main__":

    print(wait(3)) # Deze code doet het.
    print(my_sin(1.2))
