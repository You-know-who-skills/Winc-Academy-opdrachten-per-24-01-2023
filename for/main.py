from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

""" Write your functions here. """

"""" Ik heb onderstaande code zo universeel mogelijk proberen te maken"""

# Vraag 1 = kortste land namen

# def shortest_names (sc_names: list) -> list: # sc = shortest countries
        
#     shortest_country_name = min(sc_names, key=len) # Deze code zoekt naar het land met de minste karakters in de countries lijst.
#     print(f'{shortest_country_name} = het land met de minste karakters.')
#     print('\n')
    
#     total_characters_scn = len(shortest_country_name) # Deze code geeft het totaal aantal karakters van het het land met de minste karakters in de countries lijst (scn = shortest country name).
#     print(f'{total_characters_scn} = het totaal aantal karakters van het land met de minste karakters.')
#     # print(total_characters_scn )
#     print('\n')
#     print('Dit zijn alle landen met de kortste naam in de \'countries\' lijst:')
    
#     shortest_country_list = [] # In deze lijst komen alle landen die even veel karakters hebben als het land met de minste karakters.
#     # print(shortest_country_list) Deze print statement heb ik erin gezet om te checken of de lijst inderdaad nog leeg is voordat ik deze variabel weer binnen de for loop ga gebruiken.

#     for country in sc_names: # Dit is een loop op de countries lijst met de variabel genaamd 'country'.
        
#         if len(country) == len(shortest_country_name): # Met de 'len' en de '==' (= is gelijk aan) code zoekt de variabel 'country' naar alle landen die dezelfde lengte hebben als het land met de minste karakters (= de variabel total_characters_scn) (scn = shortest country name).
#         # if len(country) == total_characters_scn: # Op deze manier kan je ook zoeken naar alle landen die dezelfde lengte hebben als het land met de minste karakters, maar met deze code kijk je dan letterlijk naar het aantal karakters die ik met een tussenstap met variabel 'total_characters_scn' heb aangemaakt i.p.v. het gevonden land met variabel 'shortest_country_name'.
            
#             shortest_country_list.append(country) # Hier heb ik de variabel 'shortest_country_list' weer gebruikt om met de '.append' code alle andere landen met even veel karakters als in de variabel 'total_characters_scn' aan de lijst toe te voegen.
#             # print(country)

#     return shortest_country_list # Deze return geeft als output de uiteindelijke lijst met alle landen die even veel karakters hebben als het land met de minste karakters in de countries lijst.


# Vraag 2 = meeste klinkers
# def most_vowels (top_three: list) -> list:

    # vowels = 'aeiou' + 'AEIOU' # Deze variabel definiëert de klinkers. LET OP!!! De variabel 'vowels_in_country' in de for loop 'country_name' en 'vowel_search' is hoofdlettergevoelig. Daarom heb ik aan deze variabel (vowels) de klinkers 'ook' in hoofdletters toegevoegd (dit kan ook met de plus (+) operator, maar ik heb het op advies van een mentor zonder de + operator gedaan), want anders worden de landnamen die met een klinker hoofdletter beginnen niet meegeteld.

    # ranking_vowels = [] # In deze lijst komt een gesorteerde lijst van alle landen inclusief het aantal klinkers per land en deze lijst is gesorteerd op de klinkers van hoog naar laag.
    # ranking_top_three = [] # In deze lijst komt de top 3 van de landen met de meeste klinkers.

    # for country_name in top_three: # Deze for loop loopt door alle landen heen (= de countries lijst die ik nu top_three heb genoemd). En de variabele 'country_name' bevat de namen van de landen waar ik mee ga werken.
        # print(country_name)

        # vowels_in_country = 0  # Deze variabel geeft aan dat de telling van de zoektocht naar klinkers in de landnamen bij 0 (nul) moet beginnen.
        # print(vowels_in_country)

        # for vowel_search in country_name: # Deze for loop kijkt naar elke letter van een landnaam.
            
        #     if vowel_search in vowels:  # Deze 'if' statement met de variable 'vowel_search' kijkt of er klinkers in een land zitten.
                
        #         vowels_in_country += 1  # Deze variabel selecteert alle klinkers die in een landnaam voor komen.

        # print(country_name, vowels_in_country)
        # print(f'{country_name} heeft {vowels_in_country} klinker(s)')
        

        # ranking_vowels.append([vowels_in_country, country_name]) # Met deze code zet ik 2 validaties in de 'ranking_vowels' lijst: 1= het aantal klinkers én 2= de naam van het land.
    # print(ranking_vowels)
    # print('\n')

    # ranking_vowels.sort(reverse = True) # Met deze code sorteer ik de ranking_vowels lijst van hoog naar laag.

    # print('Hieronder staat een lijst met het aantal klinkers in een landnmaam inclusief de landnaam. De lijst is gesorteerd op klinkers: van meeste klinkers naar minste klinkers.')
    # print('\n')

    # print(ranking_vowels)
    # print('\n')

    # print('Hieronder staat een lijst met de top 3 van landen met de meeste klinkers:')
    # print('\n')

    # for ranking in ranking_vowels[:3]: # Deze code selecteert de eerste 3 items in de 'ranking_vowels' lijst en de 3 items bestaan uit: de hoeveelheid klinkers (uitgedrukt in een getal) én de landnaam.
        
    #     ranking_top_three.append(ranking[1]) # Deze code selecteert alleen de landnamen van de top 3 door de [1] index waarbij de 1 staat voor: selecteer uit de top 3 alleen de item na de komma, want de hoeveelheid klinkers = 0 en de landnaam = 1.

    # return ranking_top_three


# Vraag 3 = alfabet vormen
def alphabet_set(countries: list) -> list:

    alphabet = list('abcdefghijklmnopqrstuvwxyz') # Ik heb deze string gecast door er 'list' voor te zetten zodat de string itereerbaar / herhaalbaar wordt voor de for loop. Door deze string te casten met de 'list' object, zorg je ervoor dat Python van elke letter in deze string een aparte item maakt én de string dus itereerbaar wordt.
    print(alphabet)
    print('\n')

    used_countries = [] # In deze lijst komen alle landen die ik heb gebruikt voor het alfabet.
    countries.sort(key = len, reverse = True) # Deze code sorteert de countries lijst aflopend van het land met de meeste karakters naar het land met de minste karakters. En ik heb deze variabel buiten de for loop aangemaakt, want als je het binnen de for loop aanmaakt pakt hij Afghanistan als eerste land met de meeste karakters.
    
    for country in countries: # De variabel 'country' itereert / loopt door de countries lijst heen en kijkt dus naar alle landen in deze lijst.
        
        for letter in country.lower(): # De variabel 'letter' itereert / loopt door alle letters van een landnaam heen en kijkt dus naar elke letter van een landnaam.
            if letter in alphabet: # Deze code zegt het volgende: als een letter van een landnaam voor komt in het alfabet, doe dan onderstaande.
                alphabet.remove(letter) # Met de '.remove' code verwijder ik de gevonden alfabet letter (die de variabel 'letter' dus zoekt) uit de alfabet lijst zodat de loop / iteratie deze niet nog een keer gaat zoeken in een landnaam.   geef ik aan 
                if country not in used_countries: # Deze code zegt het volgende: als een land met de nodige alfabet letters niet voor komt in de lijst / variabel 'used countries', doe dan onderstaande.
                    used_countries.append(country) # Met de '.append' code voeg ik de landen die ik gebruikt heb om het alfabet te vormen toe aan de lijst / variabel 'used_countries'.
    # print(used_countries)

    return used_countries


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """

    # print(shortest_names(countries))
    # print('\n')
    # print(most_vowels(countries))
    print('\n')
    print(alphabet_set(countries))

