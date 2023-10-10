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
# from time import sleep  # Op deze manier kan je ook de code / het object 'sleep' importeren. Het verschil is dat wanneer je het op deze manier doet, hoef je verderop in je code geen 'punt' te gebruiken. Dus gewoon 'sleep' i.p.v. time.sleep.
import math
import sys

import greet  # Met deze code importeer ik het 'greet' bestand dat ik heb aangemaakt als nieuw bestand in de 'modules' map.


'''
Also import the 'datetime object' from the 'datetime module'. Use an alias here (like 'dt' for example).
'''

import datetime as dt # Met deze code importeer je de datetime module als alias 'dt'.


'''
Write a function called 'wait' that takes one argument called 'seconds' (int), that uses a function in the time module to make the computer wait for that number of seconds and then returns nothing.
'''

def wait(seconds: int):

    # return "Hallo" # Deze return statement doet het ook.

    time.sleep(seconds) # De 'sleep' code telt het aantal ingevoerde seconden af en returnd daarna alles wat je in de return statement zet. LET OP!!! Voor deze code (in deze functie) hoef je geen return statement te gebruiken.


'''
Write a function called 'my_sin' that takes one float as an argument and returns the 'sine' of that float. Use the math module.
'''

def my_sin(x: float):

    return math.sin(x) # LET OP!!! Per dinsdag 10-10-2023 weet ik nog niet wat deze code precies doet in Python. Ik heb deze vraag uitgezet in Slack en ik wacht dus nog op antwoord.


'''
Write a function called 'iso_now' that takes no arguments and returns a string containing the current date and time up to the minute in the ISO 8601 format. Use the datetime module.

Example: 2000-12-31T17:00.
'''

def iso_now():

    return dt.datetime.now().isoformat()    # Met deze code geef je de huidige 'datum' en 'tijd' inc. 'seconden' en 'honderdste' weer in het 'ISO 8601' formaat. Deze code heeft een gelaagde structuur dat als volgt werkt: 'dt' = de alias\
                                            # die ik heb gebruikt voor de 'datetime' module, '.datetime.now()' = een object / code binnnen de 'datetime' module en dit is tevens de code die je nodig hebt om de '.isoformat()' code te kunnen\
                                            # gebruiken, want de huidige datum en tijd in 'ISO 8601' formaat werkt alleen wanneer je deze 2 codes achter elkaar plaatst: dt.datetime.now().isoformat().
    
    # return dt.datetime.now().strftime("%Y-%m-%dT%H:%M") # Deze return statement keurt de 'Wincpy check' WEL goed omdat dit ook het 'ISO 8601' formaat lay-out heeft. LET OP!!! Het gebruik van de '%' tekens is noodzakelijk om deze code te\
    # laten werken.
    # return dt.datetime.now().strftime("%Y-%m-%d %H:%M") # Deze return statement is zoals ik het zou doen: met min tekens bij de datum en een spatie tussen de datum en het tijdstip.
    
    
'''
Write a function called 'platform' that takes no arguments and returns a string that shows which operating system (Linux, Windows, macOS, and so on) you are using. Use the sys module.
'''

def platform():

    return sys.platform  # De 'sys.platform' code laat zien op welke besturingssysteem je aan het werken bent.


def supergreeting_wrapper(name):

    return greet.super_greeting(name) # Met deze code gebruik ik de 'super_greeting' functie die ik in het 'greet.py' bestand heb aangemaakt. En dit bestand zit in dezelfde map als de 'modules' oefening.


if __name__ == "__main__":

    print(wait(1))
    
    print('\n')
    
    print(my_sin(5))

    print('\n')

    print(iso_now())

    print('\n')

    print(platform())

    print('\n')

    print(supergreeting_wrapper("Chuck D"))

    print('\n')