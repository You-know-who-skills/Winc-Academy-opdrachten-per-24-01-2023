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


# # Vraag 2 = meeste klinkers
# def most_vowels (top_three: list) -> list:

#     vowels = 'aeiou' + 'AEIOU' # Deze variabel definiëert de klinkers. LET OP!!! De variabel 'vowels_in_country' in de for loop 'country_name' en 'vowel_search' is hoofdlettergevoelig. Daarom heb ik aan deze variabel (vowels) de klinkers 'ook' in hoofdletters toegevoegd (dit kan ook met de plus (+) operator, maar ik heb het op advies van een mentor zonder de + operator gedaan), want anders worden de landnamen die met een klinker hoofdletter beginnen niet meegeteld.

#     ranking_vowels = [] # In deze lijst komt een gesorteerde lijst van alle landen inclusief het aantal klinkers per land en deze lijst is gesorteerd op de klinkers van hoog naar laag.
#     ranking_top_three = [] # In deze lijst komt de top 3 van de landen met de meeste klinkers.

#     for country_name in top_three:  # 'Country_name' is een loop door alle landen heen (= de countries lijst die ik nu top_three heb genoemd). En de variabele 'country_name' bevat de namen van de landen waar ik mee ga werken.
#         # print(country_name)

#         vowels_in_country = 0  # Met deze variabel geef ik aan dat de telling van de zoektocht naar klinkers in de landnamen bij het getal 0 (nul) moet beginnen.
#         # print(vowels_in_country)

#         for vowel_search in country_name: # Dit is een loop die naar elke letter van een landnaam gaat kijken.
            
#             if vowel_search in vowels:  # Deze 'if' statement met de variable 'vowel_search' kijkt of er klinkers in een land zitten.
                
#                 vowels_in_country += 1  # Deze variabel selecteert alle klinkers die in een landnaam voor komen.

#         # print(country_name, vowels_in_country)
#         print(f'{country_name} heeft {vowels_in_country} klinker(s)')
        

#         ranking_vowels.append([vowels_in_country, country_name]) # Met deze code zet ik 2 validaties: het aantal klinkers én de naam van het land, in de 'ranking_vowels' lijst.
#     # print(ranking_vowels)
#     print('\n')
#     ranking_vowels.sort(reverse = True)
#     print('Hieronder staat een lijst met het aantal klinkers in een landnmaam inclusief de landnaam. De lijst is gesorteerd op klinkers: van meeste klinkers naar minste klinkers.')
#     print('\n')
#     print(ranking_vowels)
#     print('\n')
#     print('Hieronder staat een lijst met de top 3 van landen met de meeste klinkers:')
#     print('\n')

#     for ranking in ranking_vowels[:3]:
        
#         ranking_top_three.append(ranking[1])

#     return ranking_top_three


# Vraag 3 = alfabet vormen
def alphabet_set(complete_alphabet: list) -> list:

    letters = 'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Nn', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Mm', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz' # Deze variabel definiëert de klinkers. LET OP!!! De variabel 'vowels_in_country' in de for loop 'country_name' en 'vowel_search' is hoofdlettergevoelig. Daarom heb ik aan deze variabel (vowels) de klinkers 'ook' in hoofdletters toegevoegd (dit kan ook met de plus (+) operator, maar ik heb het op advies van een mentor zonder de + operator gedaan), want anders worden de landnamen die met een klinker hoofdletter beginnen niet meegeteld.

    country_names = [] # In deze lijst komen alle landen die ik kan gebruiken voor het alfabet.
    alphabet_countries = [] # In deze komt de alfabet letter én het land waaruit ik de betreffende letter heb gehaald.

    for countries in complete_alphabet:  

        if countries == letters:  
            print(countries)

        # for letter_search in countries: # Dit is een loop die naar elke letter van een landnaam gaat kijken.
            
        #     if letter_search in letters:  # Deze 'if' statement met de variable 'vowel_search' kijkt of er klinkers in een land zitten.
                
        #         letters_in_country += 1  # Deze variabel selecteert alle klinkers die in een landnaam voor komen.

        # print(country_name, vowels_in_country)
        # print(f'{countries} heeft deze letter voor het alfabet:')
        

    #     ranking_vowels.append([vowels_in_country, country_name]) # Met deze code zet ik 2 validaties: het aantal klinkers én de naam van het land, in de 'ranking_vowels' lijst.
    # # print(ranking_vowels)
    # print('\n')
    # ranking_vowels.sort(reverse = True)
    # print('Hieronder staat een lijst met het aantal klinkers in een landnmaam inclusief de landnaam. De lijst is gesorteerd op klinkers: van meeste klinkers naar minste klinkers.')
    # print('\n')
    # print(ranking_vowels)
    # print('\n')
    # print('Hieronder staat een lijst met de top 3 van landen met de meeste klinkers:')
    # print('\n')

    # for ranking in ranking_vowels[:3]:
        
    #     ranking_top_three.append(ranking[1])

    # return ranking_top_three



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

