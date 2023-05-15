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
    # print(shortest_country_list) Deze print statement heb ik erin gezet om te checken of de lijst inderdaad nog leeg is voordat ik deze variabel weer binnen de for loop ga gebruiken.

    for country in sc_names: # Dit is een loop op de countries lijst met de variabel genaamd 'country'.
        
        if len(country) == total_characters_scn: # Met de 'len' en de '==' (= is gelijk aan) code zoekt de variabel 'country' naar alle landen die dezelfde lengte hebben als het land met de minste karakters (= de variabel total_characters_scn) (scn = shortest country name).
            
            shortest_country_list.append(country) # Hier heb ik de variabel 'shortest_country_list' weer gebruikt om met de '.append' code alle andere landen met even veel karakters als in de variabel 'total_characters_scn' aan de lijst toe te voegen.
            # print(country)

    return shortest_country_list # Deze return geeft als output de uiteindelijke lijst met alle landen die even veel karakters hebben als het land met de minste karakters in de countries lijst.


# Vraag 2 = meeste klinkers
def most_vowels (top_three: list) -> list:
    
    vowels = 'aeiouAEIOU' # Dez variabel definiëert de klinkers. LET OP!!! De variabel 'vowels_in_country' in de for loop 'country_name' en 'vowel_search' is hoofdlettergevoelig. Daarom heb ik aan deze variabel (vowels) de klinkers 'ook' in hoofdletters toegevoegd met de plus (+) operator, want anders worden de landnamen die met een klinker hoofdletter beginnen niet meegeteld.
    
    ranking_vowels = []
    top_drie = []

    for country_name in top_three:  # 'Country_name' is een loop door alle landen heen (= de countries lijst die ik nu top_three heb genoemd). En de variabele 'country_name' bevat de namen van de landen waar ik mee ga werken.
        # print(country_name)

        vowels_in_country = 0  # Met deze variabel geef ik aan dat de telling van de zoektocht naar klinkers in de landnamen bij het getal 0 (nul) moet beginnen.
        # print(vowels_in_country)

        for vowel_search in country_name: # Dit is een loop die naar elke letter van een landnaam gaat kijken.

            if vowel_search in vowels:  # Deze 'if' statement met de variable 'vowel_search' kijkt of er klinkers in een land zitten.
                
                vowels_in_country += 1  # Deze variabel selecteert alle klinkers die in een landnaam voor komen.

        # print(country_name, vowels_in_country)
        # print(f'{country_name} heeft {vowels_in_country} klinker(s)')

        ranking_vowels.append([vowels_in_country, country_name])
        # print(ranking_vowels)

        ranking_vowels.sort(reverse = True)
        # print(ranking_sorted_reversed)


            for top_drie in ranking_vowels:
                
                
        # top_drie = ranking_vowels.sort(reverse = True, [0:3])
        # print(top_drie)
        # break
        

            

    return ranking_vowels




        
        
                # vowels_in_country = sorted(str(vowels_in_country, reverse = True))
                # print(vowels_in_country)

                

                

                # vowels_in_country = sorted(str(vowels_in_country, reverse = True))
                # print(vowels_in_country)

                # country_and_vowels =  country_name + str(vowels_in_country) # country_name + str(vowels_in_country)
                # ranking.append(country_and_vowels)
                # print(sorted(ranking, reverse=True))
                # break

        # print(country_name, vowels_in_country)
        # print(f'{country_name} heeft {vowels_in_country} klinker(s)')

                
                
                # ranking = [country_name + vowels_in_country]
                
                # ranking = (f'{list[ranking.append(country_name)]} + {list[ranking.append(vowels_in_country)]}')
                # print(ranking)
                # break

                # ranking = (f'{country_name} + {vowels_in_country}')


                # NIET VERGETEN OM DE .SPLIT CODE TE GEBRUIKEN OM VAN DE LANDNAAM EN HET AANTAL KLINKERS 1 LIJST TE MAKEN


        # ranking.append(vowels_in_country)
        # print(ranking)
        
        # ranking.sort(reverse = True)

        # ranking.split()
        # print(ranking)

        

        


        # for top_three_list in range[0:2]:
        #     print(top_three_list)



        
        
        #     top_three_list.sort(reverse = True)
        
        # print(ranking)
        
        
        # for ranking in vowels_in_country: # position = geeft de positie van de item in de lijst aan, range = geeft aan welke waardes er tussen de nul de opgegeven getal zitten.

        #     if ranking
            

        #     if vowels_in_country >= leaderboard[position][1]: 
        #     #    print("leaderboard land:", leaderboard[position][1])

        #         leaderboard.insert(position, (country_name, vowels_in_country))
        #         break

        #     if position >2:
        #         break

        # print(leaderboard)
        # print(leaderboard[:10], 'uitslag')
        
        # definitieve_lijst = []


        # for i in leaderboard[:10]:
        #     definitief_land = i[0]
        #     definitieve_lijst += [definitief_land]
        
        # definitieve_lijst = definitieve_lijst [:-1]
            # print(definitieve_lijst)



            # print(position, 'postitie')
            # print(leaderboard[position], 'test')
        # print(leaderboard)
        # print(range(len(leaderboard)))
        # print(len(leaderboard))
        # return definitieve_lijst






# Vraag 2 = meeste klinkers
# def most_vowels (top_three: list) -> list:
    
#     number_of_vowels = 'aeiou'
    

#     for number_of_vowels in top_three:
#         print(number_of_vowels)
        
#         for char in number_of_vowels:



        # for number_of_vowels in top_three:

        # if number_of_vowels == 'a' 'e' 'i' 'o' 'u':
            
            
        # if number_of_vowels == 'a' 'e' 'i' 'o' 'u':
        
            # print(top_three, aantal_klinkers)
            # print('\n')

    # return top_three

    

# Vraag 3 = alfabet vormen
# def alphabet_set(complete_alphabet: list) -> list:



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    
    """ Write the calls to your functions here. """

    print(shortest_names(countries))
    print('\n')
    print(most_vowels(countries))


# sc_names = [min(countries, key=len)]

# print(sc_names)

