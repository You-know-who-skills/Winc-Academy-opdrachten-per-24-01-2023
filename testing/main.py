
'''
In main.py, write the function get_none that should take no arguments and always return None.
'''

def get_none():

    # return "This is not 'None'."
    return None

    # try:
    #     if get_none() == None:
    #         return True

    # except TypeError:             # Deze foutmelding komt niet tevoorschijn wanneer ik iets anders dan 'None' invul bij de 'return' statement in het 'main.py' bestand. LET OP!!! DIT FF NAVRAGEN BIJ EEN WINC MENTOR.
    #     return "Ceck again"

'''
In main.py, implement the function flatten_dict so that it passes the tests you wrote in test_flatten_dict.

Another example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [{'inner_a': 42, 'inner_b': 350}, 3.14]


'''


def flatten_dict(dictionary) -> list:

    # dictionary = {
    #     'a': a,
    #     'b': b
    # }
    
    # flatten = dictionary.values()

    flatten = []

    for value in dictionary.values():

        flatten.append(value)
        
    # print(dictionary)

    # nieuw_flatten = [dictionary]

    return flatten
    
    # print(waarde)
    # print(waarde.keys())
    # print(waarde.values())
    # nieuwe_waarde = list(waarde.values())


    # print(waarde)
    # print(waarde.keys())
    # print(waarde.values())
    # nieuwe_waarde = list(waarde.values())
    
    
    # print(flatten_dict(nieuwe_waarde))



    # return nieuwe_waarde

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


# def add_numbers(a, b): # Dit is een voorbeeld functie die ik van mentor Yordy heb gekregen en is dus geen vraag van de 'testing' oefening.

#     return a * b

    # try:  
    #     return a / b  
    # except ZeroDivisionError:  
    #     raise ZeroDivisionError("Division by zero is not allowed")

if __name__ == "__main__":

    print(get_none())
    # print(add_numbers(5, 10))
    # print(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))  # Deze code geeft een foutmelding waneer je de pytest runt, maar dit is wel de 'For an extra challenge'. Om deze code uit te kunnen voeren moet je waarschijnlijk\
                                                                            # eerst nog een functie schrijven om de lijst uit de dictionary te halen, of iets dergelijks. De mentor had geen tijd meer om dit goed uit te leggen.
    # print(flatten_dict({'a': 6}))
    # print(flatten_dict({42, 3.14}))
    print(flatten_dict({42, 3.14}))
