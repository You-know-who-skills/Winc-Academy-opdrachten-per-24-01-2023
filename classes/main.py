# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

print('\n')

'''
# Question 1 - part 1:

In main.py, write a class Player that is going to represent a soccer player. 

Define the Player class' initialization method (__init__) so that it can receive these arguments, in this order:

- name (str)
- speed (float between 0 and 1)
- endurance (float between 0 and 1)
- accuracy (float between 0 and 1)
- If speed, endurance or accuracy is not between 0 and 1 (inclusive), a ValueError must be raised. Try using a for loop here to loop through those iterables and then define a valueError.

Save the given arguments as instance attributes under the names name, speed, endurance and accuracy.
'''

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


    '''
    # Question 1 - part 2:

    Define an instance method 'introduce' that takes no arguments (except self!) and returns a string like the following, where 'Bob' is replaced by the player's actual name: 'Hello everyone, my name is Bob.'
    '''

    def introduce(self): # Deze 'self' code refereert naar alle parameters / argumenten van de '__init__' code van de 'Player class'. Dit houdt in dat je binnen deze instance alle parameters / argumenten van de 'class Player' kunt gebruiken.
        
        return F"Hello everyone, my name is {self.name}.\n" # Deze code kan ook maar de wincpy check keurt de '\n' niet goed. In deze F-string gebruik je de 'name' parameter die in de 'class Player' staat. En je roept de naam aan\
                                                            # helemaal onderaan bij de 'if __name__ == "__main__":' code.
        # return F"Hello everyone, my name is {self.name}."


    '''
    Question 1 - part 3:

    Now we want a method that returns us the best attribute of a player between the 3 we just defined (speed, endurance and accuracy). Define an instance method 'strength' that takes no arguments and returns a tuple with the name of its\
    attribute and its value. Imagine that the highest one is speed and the value is 0.8. Then the expected result should be like this: 

    ('speed', 0.8)

    If multiple attributes share the same value, prioritize as follows:

    - speed > endurance > accuracy  LET OP!!! Doordat ik de volgorde al zo heb gezet in onderstaande code (for attribute in ["speed", "endurance", "accuracy"]), is de lijst al geprioriteerd zoals in de oefening wordt gevraagd\
    
    omdat de loop altijd eerst zal beginnen bij het eerste item in de lijst ('speed' in dit geval). Daarnaast zorgt de code 'if outcome_attribute > best_results[1]:' ervoor dat 
    '''

    def strength(self): # Deze 'self' code refereert ook naar alle parameters / argumenten van de '__init__' code van de 'Player class' omdat deze instance nog binnen de 'class Player()' valt. Ook hier houdt dit dus in dat je binnen deze\
                        # instance alle parameters / argumenten van de 'class Player' kunt gebruiken.
        
        best_results = (None, 0)    # Met de 'None' code (= een keyword) geef je aan dat een object in Python (nog) geen waarde heeft. Dus in deze code gebruik ik de 'None' code in een tuple omdat ik straks 2 items nodig ga hebbben\
                                    # om de naam van het attribuut en het getal / de float / de waarde weer te kunnen geven in de output. En de naam en de waarde kan ik zelf helemaal onderin bij de 'if __name__ == "__main__":' code invullen.
        
        for attribute in ["speed", "endurance", "accuracy"]: # Met de variabel 'attribute' ga ik itereren / loopen over de lijst met de 3 attributen.

            outcome_attribute = getattr(self, attribute)    # Met deze code zeg je: met de variabel 'outcome_attribute' pak ik met de 'getattr()' code alle / de attributen: "speed", "endurance", "accuracy" van het 'self' 'object' die ik\
            # print(outcome_attribute)                      # bij de 'class Player' heb aangemaakt én die ik nu weer gebruik voor de 'for loop' met de variabel genaamd 'attribute'. En dit kan je checken met de print statement:\
                                                            # 'print(outcome_attribute)' die enkel en alleen 'alle' 'waardes' / 'getallen' van de attributen als output weergeeft. LET OP!!! De 'getattr()' code moet 'altijd' 2 argumenten\
                                                            # bevatten: een 'object' en een 'naam' / 'eigenschap' / 'kenmerk' van dat object. In deze for loop verwijs ik met de 'self' code in de 'getattr()' code naar de parameters die ik\
                                                            # heb aangemaakt bij de 'Player' class hierboven.
            if outcome_attribute > best_results[1]:         # Met deze code zeg je: als één van de waardes van de variabel 'outcome_attribute' groter is dan het getal '0' bij de variabel 'best results' hierboven, laat dan onderstaande zien.

                # return attribute, outcome_attribute       # Op deze manier is het ook mogelijk om deze instance te returnen.
            
                best_results = attribute, outcome_attribute # Met deze code geef je aan dat de variabel 'best results' vervangen moet worden voor de volgende gegevens: de naam van het attribuut (dus 1 van de attributen die in de lijst\
                                                            # bij de variable 'attribute' staat) en de waarde die je geplaatst hebt in de variabel 'outcome_attribute'.
            
        return best_results # Doordat ik de variabel 'best_result' nu heb aangepast naar de 2 variabelen 'attribute' en 'outcome_attribute', zal deze return statement het volgende weergeven: naam attribuut, komma getal\
                            # dus b.v.: ('accuracy', 0.9).

'''
# Question 2 - part 1:

In main.py, create a new class 'Commentator'. Implement it in such a way that we can do this: 

- ray = Commentator('Ray Hudson')
- print(ray.name)
- Output = 'Ray Hudson'
'''


class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


    '''
    # Question 2 - part 2:

    Write an instance method 'sum_player' that takes an instance of a player and returns the sum of their 'speed', 'endurance' and 'accuracy' attributes.

    To do this define the method with two paramenters: 'self' and another one for the player (although we are not going to use self). Then make it return a sum (you can use the function sum()) of a list of values retrieved with getattr()\
    using the player as first parameter and the name of the attribute as a string as the second parameter.
    '''

    def sum_player(self, player):

        attributes = ["speed", "endurance", "accuracy"]

        sum = 0 # Met deze code start je de optelsom van de 'sum_player' 'instance method' met het getal '0'.

        for attribute in attributes: # Met de variabel 'attribute' ga je itereren / loopen over de lijst / variable genaamd 'attributes'. 
            sum += getattr(player, attribute)   # Met deze code zeg je: tel met de '+=' operator het getal / de waarde van één van de attributen op bij de variabel 'sum'. 'Player' is hier het 'object' dat verwijst naar de 'naam' van een\
            # print(sum)                        # speler in de 'class Player en deze roep je vervolgens aan bij de 'if __name__ == "__main__"' code helemaal onderaann. En 'attribute' is hier de 'eigenschap' van het object 'player' en deze\
                                                # verwijst naar de attributen in deze instance bij de variabel 'attributes' dat weer middels de code 'self' verwijst naar de attributen die in de 'class Player' staat. LET OP!!! De 'getattr()'\
                                                # code werkt NIET ‘direct’\ op een lijst. Het werkt WEL wanneer je de 'variabel naam' van een lijst gebruikt (dus door eerst een variabel / naam te geven aan een lijst). De 'getattr()' code\
                                                # werkt dus alleen 'direct' op 'variabelen' en 'strings'.

        return round(sum, 2) # Met deze code zeg je: laat de optelsom zien en rond de optelsom af met 2 decimalen.


    '''
    # Question 2 - part 3-a:
    Write an instance method 'compare_players' that takes two instances of the class Player (in no particular order) and one of 'speed', 'endurance' and 'accuracy' as its arguments and returns the name of the player that scores the highest
    on one of the 3 attributes.

    For example: 

    - alice = Player('Alice', 0.8, 0.2, 0.6)
    - bob = Player('Bob', 0.9, 0.2, 0.6)
    - print(ray.compare_players(alice, bob, 'speed'))
    - Output = 'Bob'

    If the players score equally on this attribute, return the name of the player that has the highest strength according to the strength function you just implemented.

    LET OP!!! De onderstaande instance 'compare_players' heeft meerdere vergelijkingen. Dus omdat Python altijd de code van boven naar beneden leest, zal dus altijd gekeken worden naar de eerste vergelijking. Als de eerste vergelijking\
    niet het geval blijkt te zijn, dan zal Python kijken naar de 2e vergelijking enz. En al deze vergelijkingen hangen af van welke getallen je invult bij het aanroepen van de 'class Player'.
    '''


    def compare_players(self, player_1, player_2, performance): # Doordat je hier de 'self' code gebruikt, kan je de 'parameters' van de 'Player class' weer gebruiken.

        performance_player_1 = getattr(player_1, performance)     # Met de variabel 'performance_player_1' zeg je = pak met de 'getattr()' code 'één van de attributen' ("speed", "endurance" of "accuracy", die je meegeeft / invult wanneer je\
        # print(player_1)                                         # deze 'functie' / 'instance' aanroept onderaan bij de 'if __name__ == "__main__":' code) en geef deze weer. En met deze 3 print statements kan je controleren welke variabel\
        # print(performance)                                      # wat doet.
        # print(performance_player_1)

        performance_player_2 = getattr(player_2, performance)   # Met de variabel 'performance_player_2' zeg je hetzelfde als bij de variabl 'performance_player_1'.
        # print(performance_player_2)

        if performance_player_1 > performance_player_2: # Met deze code zeg je: als de getallen van de variabel 'performance_player_1' groter zijn dan de getallen van de variabel 'performance_player_2', laat dan onderstaande zien.
                
            # return player_1.name
            return getattr(player_1, "name")    # Met deze code zeg je: laat de 'naam' van de speler zien waarvan 'de waardes van de attributen' hoger zijn dan de andere speler. En de waardes van de attributen kan je zelf invullen bij\
                                                # de speler genaamd 'gullit' die in de 'class' 'Player' zit bij de 'if __name__ == "__main__":' code helemaal onderaan bij bij het aanroepen van de 'compare_players' instance.
        
        if performance_player_2 > performance_player_1: # Met deze code zeg je: als de getallen van de variabel 'performance_player_2' groter zijn dan de getallen van de variabel 'performance_player_1', laat dan onderstaande zien.
                
            return player_2.name    # Met deze code zeg je: laat de 'naam' van de speler zien waarvan 'de waardes van de attributen' hoger zijn dan de andere speler. En de waardes van de attributen kan je zelf invullen bij\
                                    # de speler genaamd 'gullit' die in de 'class' 'Player' zit bij de 'if __name__ == "__main__":' code helemaal onderaan bij bij het aanroepen van de 'compare_players' instance.


        '''
        Question 2 - part 3-b

        If the players score equally on 1 of the 3 attributes, return the name of the player that has the highest 'strength' according to the strength function / instance you just implemented.
        '''

        performance_player_1 = player_1.strength()[1]   # Met deze code zeg je: de variabel 'performance_player_1' is nu de waarde / float / het getal dat in de 'return' statement van de instance 'strength' vermeld staat. Dit is vanwege\
                                                        # de index die ik heb gebruikt: [1], want met de index selecteer ik de 2e variabel van de variabel 'best_result': 'outcome_attribute' (en dit is alleen de waarde / float / het getal).

        performance_player_2 = player_2.strength()[1]   # Hier doe ik hetzelfde als wat bij 'performance_player_1' staat.
        # print(performance_player_1)

        if performance_player_1 > performance_player_2: # Met deze code zeg je: als de getallen van de variabel 'performance_player_1' groter zijn dan de getallen van de variabel 'performance_player_2', laat dan onderstaande zien.
            
            return getattr(player_1, "name")            # Met deze return statement kijk je met de 'getattr' code naar de waarde / float / het getal van de variabel 'player_1'. Maar omdat je variabel 'player_1' in combinatie met het argument "name"\
                                                        # van de 'class Player' gebruikt, krijg je alleen de 'naam' van de speler te zien in de output en niet de waarde / float / het getal + de naam van de speler. De 'name' in deze code\
        
                                                        # verwijst namelijk naar de 'naam van de speler' (b.v. 'gullit' helemaal onderaan bij het aanroepen van de betreffende instance) die in de 'class Player' zit.

        elif performance_player_2 > performance_player_1: # Hier doe ik hetzelfde als wat bij de vorige 'if' statement staat.
                
            return getattr(player_2, "name")            # Hier doe ik hetzelfde als wat bij de vorige 'return' statement staat.


        '''
        Question 2 - part 3-c:

        If the 'highest strength' is also equal, report the name of the player that has the highest total score according to the 'sum_player' function / instance you just implemented.
        '''

        performance_player_1 = self.sum_player(player_1) # Met deze code zeg je: 

        performance_player_2 = self.sum_player(player_2)
        
        if performance_player_1 > performance_player_2:
            
            return getattr(player_1, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.

        if performance_player_2 > performance_player_1:
                
            return getattr(player_2, "name") # Deze name verwijst naar de speler gullit die in de class Player zit.
        
            '''
            Question 2 - part 3-d:

            If the 'sum_player' is also equal, return the string: 'These two players might as well be twins!'.
            '''
        
        else:
            return 'These two players might as well be twins!'


if __name__ == "__main__":

# attributes = ["speed", "endurance", "accuracy"] LET OP!!! Deze attributen lijst heb ik ook hier gezet zodat je niet telkens naar boven hoeft te scrollen om te kijken welke attributen er in de lijst zitten.

# Antwoord op vraag 3: a t/m d. LET OP!!! Je kan hier met de getallen spelen aan de hand van de 'compare_players' instance om verschillende uitkomsten te krijgen / te zien welke uitkomsten je krijgt.
    rijkaard = Player("Frank Rijkaard", 0.1, 0.2, 0.3)
    seedorf = Player("Clarence Seedorf", 0.4, 0.5, 0.6)

    # rijkaard = Player("Frank Rijkaard", 0.1, 0.1, 0.1)
    # seedorf = Player("Clarence Seedorf", 0.1, 0.1, 0.1)

    '''
    Bovenstaande code kan je als volgt gebruiken bij de 'compare_player' instance code helemaal onderaan. LET OP!!! Bij de 'compare_player' instance code helemaal onderaan kan je de attribuut (dit is het 3e argument) ook wijzigen.\
    En hierdoor worden de uitkomsten van je code ook anders.

    - Bij antwoord a = This code returns the name of the player that scores the highest on 1 of the 3 attributes.
    - Bij antwoord b = If the players score equally on 1 of the 3 attributes, this code returns the name of the player that scores the highest 'strength' according to the 'strength' function / instance (met 'strength' wordt\
      de beste / hoogste score van één attribuut bedoeld).
    - Bij antwoord c = If the players also score equally on the 'strength' function / instance, this code reports the name of the player that has the highest total score according to the 'sum_player' function / instance.
    - Bij antwoord d = If the players score is equal on all 3 attributes, this code returns the string: "These two players might as well be twins!"
    '''


    print("Elaboration question 1 - part 1 = 'ValueError':\n")
    print("This 'value error' is only 'raised' if you enter an attribute value which is higher than 1.\n")

    print("Elaboration question 1 - part 2 = 'Introduce':\n")
    print(rijkaard.introduce())

    print("Elaboration question 1 - part 3 = 'Strength' (return a tuple with the name of its attribute and its value):\n")
    print(rijkaard.strength())
    print(seedorf.strength())

    print('\n')

    print("Elaboration question 2 - part 1 = 'Commentator':\n")
    winter = Commentator("Aron Winter")
    print(winter.name)

    print('\n')

    print("Elaboration question 2 - part 2 = 'Sum Player':\n")
    print(winter.sum_player(seedorf))

    print('\n')

    print("Elaboration question 2 - part 3: a - d = 'Compare Players':\n")
    print(winter.compare_players(rijkaard, seedorf, "accuracy")) # attributes = ["speed", "endurance", "accuracy"]

    print('\n')
