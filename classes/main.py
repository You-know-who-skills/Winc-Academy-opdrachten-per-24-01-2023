# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

print('\n')

class Player(): # Op deze manier definieer je een 'class'.
    
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float) -> str:

        self.name = name            # Op deze manier definieer je deze argumenten voor deze 'class' met de 'self' code.
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        for attribute in [speed, endurance, accuracy]: # Met de variabel 'attribute' loop / ittereer je door de lijst met attributen: 'speed', 'endurance', 'accuracy'.

            if attribute > 1 or attribute < 0: # Met deze code geef je aan dat als de variabel 'attribute' groter is dan 1 of kleiner is dan 0, onderstaande foutmelding vermeld moet worden.
                raise ValueError(F"Please make sure that {attribute} is between 0 and 1.\n") # Met de 'raise' code kan je een foutmelding genereren.


    def introduce(self): # Deze 'self' code refereert naar alle parameters / argumenten van de '__init__' van de 'Player class'. Dit houdt in dat je binnen deze instance alle parameters / argumenten van de 'class Player' kunt gebruiken.
        
        return F"Hello everyone, my name is {self.name}.\n" # Deze code kan ook maar de wincpy check keurt de '\n' niet goed. In deze F-string gebruik je de 'name' parameter die in de 'class Player' staat. En je roept de naam aan
                                                            # helemaal onderaand bij de 'if __name__ == "__main__":' code.
        # return F"Hello everyone, my name is {self.name}."
        


    def strength(self):
        
        best_results = (None, 0) # Hier gebruik je een tuple omdat je nog niet weet welke resultaten het beste zijn.
        
        for attribute in ["speed", "endurance", "accuracy"]:

            outcome_attribute = getattr(self, attribute)

            if outcome_attribute > best_results[1]:
                
                best_results = attribute, outcome_attribute
                
            # if outcome_attribute > 1 or outcome_attribute < 0:
            #     raise ValueError(F"Please make sure that {attribute} is between 0 and 1.\n")
            
        return best_results


class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


    def sum_player(self, player):

        attributes =  ["speed", "endurance", "accuracy"]

        sum = 0

        for attribute in attributes:

            sum += getattr(player, attribute)

        return round(sum, 2)


    def compare_players(self, player_1, player_2, performance):

        # highest_score = (None, 0)
        
        performance_player_1 = getattr(player_1, performance)

        performance_player_2 = getattr(player_2, performance)

        if performance_player_1 > performance_player_2:
                
            # return player_1.name
            return getattr(player_1, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.
        
        if performance_player_2 > performance_player_1:
                
            return player_2.name
        

        performance_player_1 = player_1.strength()[1]

        performance_player_2 = player_2.strength()[1]
        # print(performance_player_1)

        if performance_player_1 > performance_player_2:
            
            return getattr(player_1, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.

        if performance_player_2 > performance_player_1:
                
            return getattr(player_2, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.
        

        performance_player_1 = self.sum_player(player_1)

        performance_player_2 = self.sum_player(player_2)
        
        if performance_player_1 > performance_player_2:
            
            return getattr(player_1, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.

        if performance_player_2 > performance_player_1:
                
            return getattr(player_2, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.

        return "These two players might as well be twins!"



if __name__ == "__main__":

    rijkaard = Player("Frank Rijkaard", 0.6, 0.6, 0.6)
    gullit = Player("Ruud Gullit", 0.6, 0.6, 0.6)
    seedorf = Player("Clarence Seedorf", 0.6, 0.6, 0.6)

    # rijkaard.introduce() # Deze code doet het.
    print(rijkaard.introduce()) # Deze code doet het.

    
    print(rijkaard.strength())
    print(gullit.strength())
    print(seedorf.strength())

    print('\n')

    winter = Commentator("Aron Winter")
    
    print(winter.sum_player(gullit))
    
    print(winter.compare_players(gullit, seedorf, "speed"))

    print('\n')


    
    





