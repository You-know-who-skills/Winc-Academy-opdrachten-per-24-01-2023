# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

print('\n')

# Question 1 - part 1:

class Player(): # Op deze manier definieer je een 'class' en in dit geval heet de class 'Player'.
    
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float) -> str:  # Met de 'init' code (ook wel 'initializer' or 'constructor' genoemd) 'initieer je een object van een class'. En de objecten zijn o.a.\
                                                                                            # de argumenten en de parameters.
        self.name = name            # Met de 'self' code definieer je deze argumenten voor deze 'class'. En met de 'self' code kan je deze variabelen / argumenten in onderstaande instances telkens weer oproepen. LET OP!!!\
        self.speed = speed          # De 'punt' achter de 'self' code gebruik je om attributen te benaderen én toe te wijzen. Verderop in deze oefening / instance zie je hoe dit werkt.
        self.endurance = endurance
        self.accuracy = accuracy

        for attribute in [speed, endurance, accuracy]: # Met de variabel 'attribute' loop / ittereer je door de lijst met attributen: 'speed', 'endurance', 'accuracy'.

            if attribute > 1 or attribute < 0: # Met deze code geef je aan dat als de variabel 'attribute' groter is dan 1 of kleiner is dan 0, onderstaande foutmelding vermeld moet worden.
                raise ValueError(F"Please make sure that {attribute} is between 0 and 1.\n") # Met de 'raise' code kan je een foutmelding genereren.


    def introduce(self): # Deze 'self' code refereert naar alle parameters / argumenten van de '__init__' code van de 'Player class'. Dit houdt in dat je binnen deze instance alle parameters / argumenten van de 'class Player' kunt gebruiken.
        
        return F"Hello everyone, my name is {self.name}.\n" # Deze code kan ook maar de wincpy check keurt de '\n' niet goed. In deze F-string gebruik je de 'name' parameter die in de 'class Player' staat. En je roept de naam aan\
                                                            # helemaal onderaand bij de 'if __name__ == "__main__":' code.
        # return F"Hello everyone, my name is {self.name}."
        

# Question 1 - part 2:

    def strength(self): # Deze 'self' code refereert ook naar alle parameters / argumenten van de '__init__' code van de 'Player class' omdat deze instance nog binnen de 'class Player()' valt. Ook hier houdt dit dus in dat je binnen deze\
                        # instance alle parameters / argumenten van de 'class Player' kunt gebruiken.
        
        best_results = (None, 0)    # Met de 'None' code (= een keyword) geef je aan dat een object in Python (nog) geen waarde heeft. Dus in deze code gebruik ik de 'None' code in een tuple omdat ik straks 2 items nodig ga hebbben\
                                    # om de naam van het attribuut en het getal / de float / de waarde weer te kunnen geven in de output. En de naam en de waarde kan ik zelf helemaal onderin bij de 'if __name__ == "__main__":' code invullen.
        
        for attribute in ["speed", "endurance", "accuracy"]: # Met de variabel 'attribute' ga ik itereren / loopen over de lijst met de 3 attributen.

            outcome_attribute = getattr(self, attribute)    # De variabel 'outcome_attribute' geeft alle waardes weer van de for loop van de lijst met de attributen hierboven en dit kan je checken met de print statement hieronder.
            print(outcome_attribute)                        # Met de 'self' code kan ik weer refereren naar één van de parameters die ik heb aangemaakt bij de 'Player' class. En met de 'getattr()' code i.c.m. de 'attribute' variabel\
                                                            # kan ik de 'waardes' van de attributen in de 'attribute' lijst selecteren. En met de print statement kan je checken of de variabel 'outcome_attribute' alle waardes van de\
                                                            # for loop van de lijst met de attributen hierboven daadwerkelijk weergeeft.

            if outcome_attribute > best_results[1]:         # Met deze code zeg je: als één van de waardes van de variabel 'outcome_attribute' groter is dan het getal '0' bij de variabel 'best results' hierboven.

                best_results = attribute, outcome_attribute # Met deze code geef je aan dat de variabel 'best results' vervangen moet worden voor de volgende gegevens: de naam van het attribuut (dus 1 van de attributen die in de lijst\
                                                            # bij de variable 'attribute' staat) en de waarde die je geplaatst hebt in de variabel 'outcome_attribute'.
            
        return best_results # Doordat ik de variabel 'best_result' nu heb aangepast naar de 2 variabelen 'attribute' en 'outcome_attribute', zal deze return statement het volgende weergeven: naam attribuut, komma getal\
                            # dus b.v.: ('accuracy', 0.9).


# Question 2 - part 1:

class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


# Question 2 - part 2:

    def sum_player(self, player):

        attributes =  ["speed", "endurance", "accuracy"]

        sum = 0 # Met deze code start je de optelsom van de 'sum_player' 'instance method' met het getal '0'.

        for attribute in attributes:    # Met de variabel 'attribute' ga ik itereren / loopen over de lijst / variable genaamd 'attributes'. LET OP!!! De getattr() code werkt NIET ‘direct’ op een lijst. Het werkt WEL wanneer je\
                                        # de variabelnaam van een lijst gebruikt. Het werkt dus alleen op 'variabelen' en 'strings'.
            sum += getattr(player, attribute) # Met deze code zeg ik: voeg aan de variabel 'sum' de naam van een speler toe én de waarde van een attribuut.

        return round(sum, 2)


# Question 2 - part 3:

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

    # rijkaard = Player("Frank Rijkaard", 0.6, 0.6, 0.6)
    # gullit = Player("Ruud Gullit", 0.6, 0.6, 0.6)
    # seedorf = Player("Clarence Seedorf", 0.6, 0.6, 0.6)

    rijkaard = Player("Frank Rijkaard", 0.1, 0.2, 0.3)
    gullit = Player("Ruud Gullit", 0.4, 0.5, 0.6)
    seedorf = Player("Clarence Seedorf", 0.7, 0.8, 0.9)


    print("Elaboration question 1 - part 1 = 'Introduce':\n")
    print(rijkaard.introduce()) # Deze code doet het.


    print("Elaboration question 1 - part 2 = 'Strength' :\n")
    print(rijkaard.strength())
    print(gullit.strength())
    print(seedorf.strength())

    print('\n')

    print("Elaboration question 2 - part 1 = 'Commentator':\n")
    winter = Commentator("Aron Winter")
    print(winter.name)

    print('\n')

    print("Elaboration question 2 - part 2 = 'Sum Player':\n")
    print(winter.sum_player(gullit))

    print('\n')

    print("Elaboration question 2 - part 3 = 'Compare Players':\n")
    print(winter.compare_players(gullit, seedorf, "speed"))

    print('\n')


    
    





