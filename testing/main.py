
'''
In main.py, write the function get_none that should take no arguments and always return None.
'''
print('\n')

def get_none():

    return None


'''
In main.py, implement the function flatten_dict so that it passes the tests you wrote in test_flatten_dict.

Another example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [{'inner_a': 42, 'inner_b': 350}, 3.14]
'''


def flatten_dict(dictionary) -> list:

    flatten = [] # Dit is de lijst de gereturnd moet worden.

    for value in dictionary.values():   # Met de variabel 'value' ga ik itereren over de 'values' van de variabel 'dictionary'. LET OP!!! Met de '.values()' code selecteer je alleen de values / waardes van een dictionary (een dictionary\
                                        # bestaat namelijk uit een 'key' en een 'value' / 'waarde'). Dus doordat ik '.values()' aan de variabel 'dictionary' heb vastgemaakt, itereer ik alleen over de values / waardes van de dictionary/

        print(F"Dit is de print statement van de varibale 'value': {value}\n")

        flatten.append(value) # Met deze code voeg ik de uitkomst van de variabel 'value' (bestaande uit enkel en alleen de values / waardes van de dictionary door de code 'dictionary.values()') toe aan de variabel / lijst 'flatten'.
        
    print(F"Dit is de print statement van de variabel 'dictionary': {dictionary}\n")

    
    print(F"Dit is de print statement van de varibale 'dictinary' inc. de '.keys()' code: {dictionary.keys()}\n")       # Met de '.keys()' code selecteer je alleen de keys / sleutels van een dictionary (een dictionary bestaat namelijk uit\
                                                                                                                        # een key en een value / waarde).
    print(F"Dit is de print statement van de varibale 'dictinary' inc. de '.values()' code: {dictionary.values()}\n")   
    flatten = list(dictionary.values()) # Met de variabel 'flatten' zet ik de variabel 'dictionary' in een lijst. En met de variabl 'dictionary' in combinatie met de code '.values' zorg ik ervoor dat alleen de 'values' / 'waardes' van de\
                                        # dictionary zichtbaar zijn. En de dictinary staat helemaal onderaan bij de 'if __name__ == "__main__": code' waar ik de functie 'flatten_dict' aanroep met een dictionary.
    return flatten # Met deze code return ik de variabel 'flatten' dat nu bestaat uit een 'lijst' met enkel en alleen de 'values' / 'waardes' van de dictionary.
    
    
'''
Run the tests you wrote with pytest as you are working on the implementation of the flatten_dict function. 

For an extra challenge, see if you can implement flatten_dict in such a way that the dictionary is flattened all the way down regardless of how many nested levels the original dictionary contains. 

For example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})

# [42, 350, 3.14]

flatten_dict({'a': [{'inner_inner_a': 42}]})

# [42]


Note:
To be able to do this, you may want to look into a technique called recursion.
'''
# Deze vraag heb ik niet gemaakt omdat ik er geen zin in én tijd voor had, want ik wilde gewoon snel starten met de eindopdracht: Superpy.


if __name__ == "__main__":

    print(get_none())
    print('\n')
    print(flatten_dict({'a': 42, 'b': 3.14}))
    print('\n')
