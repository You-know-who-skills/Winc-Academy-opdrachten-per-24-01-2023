from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

""" Write your functions here. """

"""" Ik heb onderstaande code zo universeel mogelijk proberen te maken"""

# Vraag 1 = kortste namen

def shortest_names (sc_names: list) -> list: # sc = shortest countries
    
    longest_country_name = [max(sc_names, key=len)] # Deze code zoekt altijd naar het land met de meeste karakters in de countries lijst.
    print(longest_country_name)

    total_characters_lcn = len(longest_country_name) # Deze code geeft altijd het totaal aantal karakters van het het land met de meeste karakters in de countries lijst (lcn = longest country name).
    print(total_characters_lcn)
    
    shortest_country_name = [min(sc_names, key=len)] # Deze code zoekt altijd naar het land met de minste karakters in de countries lijst.
    print(shortest_country_name)
    
    total_characters_scn = len(shortest_country_name) # Deze code geeft altijd het totaal aantal karakters van het het land met de minste karakters in de countries lijst (scn = shortest country name).
    print(total_characters_scn)
    
    shortest_countries_list = [] # Dit is een lijst van alle landen met de minste karakters in de countries lijst.
    

    for shortest_countries in sc_names: # Dit is een loop van de countries lijst.
        # print(shortest_countries)
        # print(len(shortest_countries))
        # print(total_characters_lcn)

        if len(shortest_countries) == total_characters_scn: # lcn = longest country name
            print(shortest_countries)
            
            # total_characters_lcn = len(shortest_countries)
            # print(total_characters_lcn)

            # shortest_countries_list = [shortest_countries]
            # print(shortest_countries_list)

        elif shortest_countries_list.append(shortest_countries):
    
            print(shortest_countries_list)
    
            return shortest_countries_list


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

