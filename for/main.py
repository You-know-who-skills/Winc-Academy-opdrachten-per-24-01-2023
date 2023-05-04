from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

""" Write your functions here. """

"""" Ik heb onderstaande code zo universeel mogelijk proberen te maken"""

# Vraag 1 = kortste land namen

def shortest_names (sc_names: list) -> list: # sc = shortest countries
        
    shortest_country_name = min(sc_names, key=len) # Deze code zoekt naar het land met de minste karakters in de countries lijst.
    print(shortest_country_name)
    print('\n')
    
    total_characters_scn = len(shortest_country_name) # Deze code geeft het totaal aantal karakters van het het land met de minste karakters in de countries lijst (scn = shortest country name).
    print(total_characters_scn)
    print('\n')
    print('Dit zijn alle landen met de kortste naam in de \'countries\' lijst:')
    
    shortest_country_list = [] # In deze lijst komen alle landen die even veel karakters hebben als het land met de minste karakters.
    
    for country in sc_names: # Dit is een loop op de countries lijst met de validatie genaamd 'country'.
        
        if len(country) == total_characters_scn: # Met de 'len' en de '==' (= is gelijk aan) code zoekt de variabel 'country' naar alle landen die dezelfde lengte hebben als het land met de minste karakters (= de variabel total_characters_scn) (scn = shortest country name).
            
            shortest_country_list.append(country) # Met de '.append' code voegt 
            # print(country)

    return shortest_country_list


# Vraag 2 = meeste klinkers
# def most_vowels (most_vowels: list) -> list:
    

# Vraag 3 = alfabet vormen
# def alphabet_set(complete_alphabet: list) -> list:



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """

    print(shortest_names(countries))


# sc_names = [min(countries, key=len)]

# print(sc_names)

