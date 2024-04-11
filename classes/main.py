# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

print('\n')

'''
# Question 1 - part 1 = 'ValueError':

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
                                                                                            # de argumenten en de parameters. LET OP!!! Je moet altijd de '__init__' code aanmaken binnen een 'class' om de 'self' code te kunnen gebruiken.
        self.name = name            # Met de 'self' code definieer je deze argumenten voor deze 'class'. En met de 'self' code kan je deze variabelen / argumenten in onderstaande instances telkens weer oproepen. LET OP!!!\
        self.speed = speed          # De 'punt' achter de 'self' code gebruik je om attributen te benaderen én toe te wijzen. Verderop in deze oefening / instance zie je hoe dit werkt.
        self.endurance = endurance
        self.accuracy = accuracy

        for attribute in [speed, endurance, accuracy]: # Met de variabel 'attribute' loop / ittereer je door de lijst met attributen: 'speed', 'endurance', 'accuracy'.
            
            if attribute > 1 or attribute < 0: # Met deze code geef je aan dat als de variabel 'attribute' groter is dan 1 of kleiner is dan 0, onderstaande foutmelding vermeld moet worden.
                raise ValueError(F"Please make sure that {attribute} is between 0 and 1.\n") # Met de 'raise' code kan je een foutmelding genereren.


    '''
    # Question 1 - part 2 = 'Introduce':

    Define an instance method 'introduce' that takes no arguments (except self!) and returns a string like the following, where 'Bob' is replaced by the player's actual name: 'Hello everyone, my name is Bob.'
    '''

    def introduce(self):    # Deze 'self' code refereert naar alle parameters / argumenten van de '__init__' code van de 'Player class'. Dit houdt in dat je binnen deze instance alle parameters / argumenten van de 'class Player'\
                            #  kunt gebruiken zolang je de 'self' code in de definitie van deze 'instance' zet.
        
        return F"Hello everyone, my name is {self.name}.\n" # Deze code kan ook maar de wincpy check keurt de '\n' niet goed. In deze F-string gebruik je de gedefinieerde 'self.name' code die in de 'class Player' staat. En je roept deze\
                                                            # 'instance' aan door een naam van een speler in te vullen helemaal onderaan bij de 'introduce' code / instance bij de 'if __name__ == "__main__":' code.
        # return F"Hello everyone, my name is {self.name}."


    '''
    Question 1 - part 3 = 'Strength':

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

            outcome_attribute = getattr(self, attribute)    # Met deze code zeg je: met de variabel 'outcome_attribute' pak ik met de 'getattr()' code de 'waarde(s)' van één van de attributen van de variabel 'attribute' in de for loop.\
                                                            # En met deze 'self' code geef ik weer aan dat ik één van de variabelen wil gebruiken uit de 'class Player', maar omdat de 'getattr()' code alleen maar kijkt naar de\
                                                            # waardes / getallen ÉN omdat de 'getattr()' altijd 2 argumenten moet bevatten (een 'object' en een 'naam' / 'eigenschap' / 'kenmerk' van dat object), laat deze code alleen maar de\
                                                            # getallen / 1 ding (i.p.v. 2) zien in de output. En dit kan je checken met de print statement 'print(outcome_attribute)' die enkel en alleen 'alle' 'waardes' / 'getallen' van de\
                                                            # attributen als output weergeeft. LET OP!!! De getallen / waardes kan je helmaal onderaan bij de 'if __name__ == "__main__ code invullen.
            
            # print(F"Dit is de print statement bij de 'strength' instance: {outcome_attribute}")
            
            if outcome_attribute > best_results[1]:         # Met deze code zeg je: als één van de waardes van de variabel 'outcome_attribute' groter is dan het getal '0' bij de variabel 'best results' hierboven, voer dan onderstaande uit.

                # return attribute, outcome_attribute       # Op deze manier is het ook mogelijk om deze instance te returnen.
            
                best_results = attribute, outcome_attribute # Met deze code geef je aan dat de variabel 'best results' vervangen moet worden voor de volgende gegevens: de 'naam van het attribuut' (dus 1 van de attributen die in de lijst\
                                                            # bij de variable 'attribute' staat) en 'de waarde' die je geplaatst hebt in de variabel 'outcome_attribute'.
            
        return best_results # Doordat ik de variabel 'best_results' nu heb vervangen door 2 variabelen: 'attribute' (= 1 van de namen van het attribuut in de lijst 'attribute') en 'outcome_attribute' (= het getal / de waarde die ik heb\
                            # verkregen met de 'getattr()' code), zal deze return statement het volgende weergeven: 'naam attribuut' + een komma getal (dus b.v.: 'accuracy', 0.9). En dit zal even vaak weergegeven worden als het aantal\
                            # spelers dat je invult (in deze code zijn dat 2 spelers: Rijkaard en Seedorf).

'''
# Question 2 - part 1 = 'Commentator':

In main.py, create a new class 'Commentator'. Implement it in such a way that we can do this: 

- ray = Commentator('Ray Hudson')
- print(ray.name)
- Output = 'Ray Hudson'
'''


class Commentator():

    def __init__(self, name: str) -> str:   # Met deze code creëer ik een nieuwe 'self' code in deze nieuwe class én geef ik een nieuwe argument op.
                            

        self.name = name    # Met deze code definieer ik een nieuwe 'self' code in de nieuwe class genaamd 'Commentator'. LET OP!!! Deze 'self' code is dus GEEN verwijzing naar de self code in de class 'Player'. Deze 'self' code is dus\
                            # alleen bruikbaar binnen deze 'class' / de class 'Commentator'. De nieuwe 'self' code heb ik hier nu ook gekoppeld aan het argument 'name'.

    '''
    Question 2 - part 2 = 'Sum player':

    Write an instance method 'sum_player' that takes an instance of a player and returns the sum of their 'speed', 'endurance' and 'accuracy' attributes.

    To do this define the method with two paramenters: 'self' and another one for the player (although we are not going to use self). Then make it return a sum (you can use the function sum()) of a list of values retrieved with getattr()\
    using the player as first parameter and the name of the attribute as a string as the second parameter.
    '''

    def sum_player(self, player):   # Deze 'self' code verwijst naar de de 'self' code die ik hierboven bij de 'class Commentator' heb aangemaakt. Omdat de 'self' code al is gedefinieerd / gekoppeld aan het argument 'name', moet ik nog een\
                                    # argument / het argument 'player' aanmaken om binnnen deze 'instance' de data / attributen van de spelers (die ook in de class Player staan) te kunnen gebruiken.

        attributes = ["speed", "endurance", "accuracy"]

        sum = 0 # Met deze code start je de optelsom van de 'sum_player' 'instance method' met het getal '0'. Door deze variabl eerst op nul te zetten, kan je straks iets hierbij optellen.

        for attribute in attributes: # Met de variabel 'attribute' ga je itereren / loopen over de lijst / variabel genaamd 'attributes'. 
            sum += getattr(player, attribute)   # Met deze code zeg je: tel met de '+=' operator het getal / de waarde van één van de attributen op bij de variabel 'sum'. De variabel / het object 'player' verwijst naar het argument 'player'\
                                                # in de benaming van deze 'instance'. De variabel / het argument 'player' is hier nodig om 2 redenen: 1= omdat de 'getattr()' code altijd 2 argumenten moet hebben. 2= Je hebt het nodig om de\
                                                # de waardes van de attributen van de spelers in de 'Player' class te kunnen gebruiken wanneer je deze aanroept bij de 'if __name__ == "__main__"' code helemaal onderaan deze code. En\
                                                # 'attribute' is hier de 'eigenschap' van het object 'player' en deze verwijst naar de 'waardes' van de uitkomst van de for loop die nu geplaatst zijn in de variabel 'attribute'. LET OP!!!\
                                                # De 'getattr()' code werkt NIET ‘direct’\ op een lijst. Het werkt WEL wanneer je de 'variabel naam' van een lijst gebruikt (dus door eerst een variabel / naam te geven aan een lijst).\
                                                # De 'getattr()' code werkt dus alleen 'direct' op 'variabelen' en 'strings'. Met andere woorden, op deze manier werkt de 'getattr()' code NIET: getattr(["speed", "endurance", "accuracy"])\
                                                # omdat je het direct voor een lijst plaatst.
            
            # print(F"Dit is de print statement bij de 'sum_player' op regel 140 van vraag 2 part 2 ('instance') = {sum}") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

        return round(sum, 2) # Met deze code zeg je: laat de optelsom / de waardes zien en rond de optelsom af met 2 decimalen.


    '''
    Question 2 - part 3-a = 'Compare_players':

    Write an instance method 'compare_players' that takes two instances of the class Player (in no particular order) and one of 'speed', 'endurance' and 'accuracy' as its arguments and returns the name of the player that scores the highest
    on one of the 3 attributes.

    For example: 

    - alice = Player('Alice', 0.8, 0.2, 0.6)
    - bob = Player('Bob', 0.9, 0.2, 0.6)
    - print(ray.compare_players(alice, bob, 'speed'))
    - Output = 'Bob'

    If the players score equally on this attribute, return the name of the player that has the highest strength according to the strength function you just implemented.

    LET OP!!! De onderstaande instance 'compare_players' heeft meerdere vergelijkingen. Dus omdat Python altijd de code van boven naar beneden leest, zal er dus altijd gekeken worden naar de eerste vergelijking. Als de eerste vergelijking\
    niet het geval blijkt te zijn, dan zal Python kijken naar de 2e vergelijking enz. En al deze vergelijkingen hangen af van welke getallen je invult bij het aanroepen van de 'class Player helemaal onderaan deze code'.
    '''


    def compare_players(self, player_1, player_2, performance): # Deze 'self' code verwijst dus naar de 'self' code van de 'Commentator' class én is gekoppeld aan het argument 'name' van de 'Commentator' class waardoor je dus weer de\
                                                                # spelers uit de 'Player' class als 'argument' kunt gebruiken wanneer je deze 'instance' aanroept helemaal onderaan deze code bij de 'if __name__ == "__main__"' code.

        performance_player_1 = getattr(player_1, performance)   # Met de variabel 'performance_player_1' zeg je: kijk met de 'getattr()' code naar: een speler, één van de attributen ("speed", "endurance" of "accuracy") én naar de waarde\
                                                                # / de uitkomst van het attribuut die je beide (dus de speler én het attribuut) als argumenten meegeeft / invult wanneer je deze 'functie' / 'instance' aanroept onderaan bij\
                                                                # de 'if __name__ == "__main__":' code) en geef deze / alles weer. En met onderstaande '3 print statements' kan je controleren welke variabel wat doet / weergeeft.
                
        # print(F"1e print statement 'player_1' bij 'comapere_players' = {player_1}")                
        # print(F"2e print statement 'performance' bij 'comapere_players' = {performance}")             
        # print(F"3e print statement 'performance_player_1' bij 'comapere_players' = {performance_player_1}")          

        performance_player_2 = getattr(player_2, performance)   # Met de variabel 'performance_player_2' zeg je hetzelfde als bij de variabl 'performance_player_1'.
        # print(performance_player_2)

        if performance_player_1 > performance_player_2:         # Met deze code zeg je: als het 'getal' / de 'uitkomst' van de variabel 'performance_player_1' groter is dan het 'getal' / de 'uitkomst' van de variabel 'performance_player_2',\
                                                                # voer dan onderstaande uit.
            # print(F"Dit is de print statement op regel 181: vraag 2 part 3-a = {performance_player_1}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

            # return player_1.name              # Deze return statement doet het ook.
            return getattr(player_1, "name")    # Met deze code zeg je: laat de 'naam' van 'de speler' / 'speler 1' zien als deze 'hoger scoort' dan 'speler 2' op 'één van de attributen'. LET OP!!! De scores kan je dus zelf invullen\
                                                # helemaal onderaan deze code bij de 'if __name__ == "__main__"' code bij het 'aanroepen' van de 'compare_players' instance.
        
        elif performance_player_2 > performance_player_1:       # Met deze code zeg je: als het 'getal' / de 'uitkomst' van de variabel 'performance_player_2' groter is dan het 'getal' / de 'uitkomst' van de variabel 'performance_player_1',\
                                                                # voer dan onderstaande uit.
            # print(F"Dit is de print statement op regel 189: vraag 2 part 3-a = {performance_player_2}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

            # return player_2.name              # Deze return statement doet het ook.
            return getattr(player_2, "name")    # Met deze code zeg je: laat de 'naam' van 'de speler' / 'speler 2' zien als deze 'hoger scoort' dan 'speler 1' op 'één van de attributen'. LET OP!!! De scores kan je dus zelf invullen\
                                                # helemaal onderaan deze code bij de 'if __name__ == "__main__"' code bij het 'aanroepen' van de 'compare_players' instance.


        '''
        Question 2 - part 3-b

        If the players score equally on 1 of the 3 attributes, return the name of the player that has the highest 'strength' according to the strength function / instance you just implemented.
        '''

        performance_player_1 = player_1.strength()[1]   # Met deze code zeg je: de variabel 'performance_player_1' is nu de waarde / float / het getal dat in de 'return' statement van de instance 'strength' in de class 'Player' vermeld staat.\
                                                        # Dit omdat de index die ik heb gebruikt [1] de 2e variabel van de variabel 'best_result' (= 'outcome_attribute') selecteert (en betreft alleen de waarde / float / het getal). LET OP!!!\
                                                        # Door een punt '.' te gebruiken kan je dus alsnog 'code' vanuit een andere 'class' selecteren.

        performance_player_2 = player_2.strength()[1]   # Hier doe ik hetzelfde als wat bij 'performance_player_1' staat.
        # print(performance_player_1)

        if performance_player_1 > performance_player_2: # Met deze code zeg je: als het 'getal' / de 'uitkomst' van de variabel 'performance_player_1' groter is dan het 'getal' / de 'uitkomst' van de variabel 'performance_player_2',\
                                                        # voer dan onderstaande uit.
            # print(F"Dit is de print statement op regel 211: vraag 2 part 3-b = {performance_player_2}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.
            
            return getattr(player_1, "name")            # Met deze 'return' statement kijk je met de 'getattr()' code 'eigenlijk' naar de waarde / float / het getal van de variabel 'player_1'. Maar omdat je de 'getattr()' code nu afdwingt\
                                                        # met het argument "name" (dit is dus een 'eigenschap' / 'kenmerk' van het 'object' player_1) dat verwijst naar het argument 'name' bij het aanmaken van deze class Commentator,\
                                                        # krijg je alleen de 'naam' van de speler te zien in de output en niet het 'getal' / de 'waarde' / 'float'. En de naam van de speler bij deze code kan je dus zelf invullen helemaal\
                                                        # onderaan deze code bij de 'if __name__ == "__main__"' code bij het 'aanroepen' van de 'compare_players' instance. De namen van de spelers zijn namelijk al gedefinieerd in de 'Player'\
                                                        # class maar deze kan je alsnog gebruiken door de code als volgt aan te roepen: print(winter.compare_players(rijkaard, seedorf, "accuracy"))

        elif performance_player_2 > performance_player_1: # Hier doe ik hetzelfde als wat bij de vorige 'if' statement staat.
            # print(F"Dit is de print statement op regel 220: vraag 2 part 3-b = {performance_player_2}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

            return getattr(player_2, "name")            # Hier doe ik hetzelfde als wat bij de vorige 'return' statement staat.


        '''
        Question 2 - part 3-c:

        If the 'highest strength' is also equal, report the name of the player that has the highest total score according to the 'sum_player' function / instance you just implemented.
        '''

        performance_player_1 = self.sum_player(player_1)    # Met deze code zeg je: de variabel 'performance_player_1' is nu de 'uitkomst' / het 'getal' bij de 'return statement' van de 'sum_player' instance. En de variabel 'player_1'\
                                                            # verwijst naar het 'argument' 'player_1' die ik heb aangemaakt bij het aanmaken / definiërenvan de 'compare_players' instance.
        
        performance_player_2 = self.sum_player(player_2)    # Met deze code zeg je: de variabel 'performance_player_2' is nu de 'uitkomst' / het 'getal' bij de 'return statement' van de 'sum_player' instance. En de variabel 'player_2'\
                                                            # verwijst naar het 'argument' 'player_2' die ik heb aangemaakt bij het aanmaken / definiëren van de 'compare_players' instance.
        
        if performance_player_1 > performance_player_2:     # Met deze code zeg je: als het 'getal' / de 'uitkomst' van de variabel 'performance_player_1' groter is dan het 'getal' / de 'uitkomst' van de variabel 'performance_player_2',\
                                                            # voer dan onderstaande uit.
            
            # print(F"Dit is de print statement op regel 240 bij vraag 2 part 3-c = {performance_player_1}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

            return getattr(player_1, "name")            # Met deze 'return' statement kijk je met de 'getattr()' code 'eigenlijk' naar de waarde / float / het getal van de variabel 'player_1'. Maar omdat je de 'getattr()' code nu afdwingt\
                                                        # met het argument "name" (dit is dus een 'eigenschap' / 'kenmerk' van het 'object' player_1) dat verwijst naar het argument 'name' bij het aanmaken van deze class Commentator,\
                                                        # krijg je alleen de 'naam' van de speler te zien in de output en niet het 'getal' / de 'waarde' / 'float'. En de naam van de speler bij deze code kan je dus zelf invullen helemaal\
                                                        # onderaan deze code bij de 'if __name__ == "__main__"' code bij het 'aanroepen' van de 'compare_players' instance. De namen van de spelers zijn namelijk al gedefinieerd in de 'Player'\
                                                        # class maar deze kan je alsnog gebruiken door de code als volgt aan te roepen: print(winter.compare_players(rijkaard, seedorf, "accuracy"))

        elif performance_player_2 > performance_player_1: # Hier doe ik hetzelfde als wat bij de vorige 'if' statement staat.    
            # print(F"Dit is de print statement op regel 249 bij vraag 2 part 3-c = {performance_player_2}\n") # Deze print statement werkt alleen als er aan deze if statementen is voldaan.

            return getattr(player_2, "name")            # Hier doe ik hetzelfde als wat bij de vorige 'return' statement staat.
        
            '''
            Question 2 - part 3-d:

            If the 'sum_player' is also equal, return the string: 'These two players might as well be twins!'.
            '''
        
        else:
            return "These two players might as well be twins!"


if __name__ == "__main__":

# attributes = ["speed", "endurance", "accuracy"] LET OP!!! Deze attributen lijst heb ik ook hier gezet zodat ik niet telkens naar boven hoef te scrollen om te kijken welke attributen er in de lijst zitten.

# Antwoord op vraag 2 part 3: a t/m d. LET OP!!! Je kan hier met de getallen spelen voor de 'compare_players' vraag (= vraag 2 - part 3-a t/m d) om verschillende uitkomsten te krijgen / te zien welke uitkomsten je krijgt.

# Antwoord op vraag 2 part 3-a = This code returns the name of the player that scores the highest on the same attribute.
    rijkaard = Player("Frank Rijkaard", 0.8, 0.7, 0.6)
    seedorf = Player("Clarence Seedorf", 0.9, 0.7, 0.6) # Antwoord = 'seedorf' omdat ze op de andere attributen gelijk scoren maar op speed scoort Seedorf hoger dan Rijkaard.

# Antwoord op vraag 2 part 3-b = If the players score equally on the same attribute, this code returns the name of the player that scores the highest 'strength' according to the 'strength' function / instance. Dus hiermee wordt het\
# volgende bedoeld: de speler die op 1 van de 3 attributen een hogere score heeft dan de andere 2 attributen én met deze attribuut ook een hogere score heeft dan alle 3 de attributen van de andere speler (NIET bij elkaar opgeteld maar\
# per attribuut), wordt met deze code weergegeven.
    # rijkaard = Player("Frank Rijkaard", 0.5, 0.4, 0.3)
    # seedorf = Player("Clarence Seedorf", 0.3, 0.4, 0.6) # Antwoord = 'seedorf' omdat het getal 6 het hoogste getal is van alle attributen van Seedorf én die van Rijkaard.

# Antwoord op vraag 2 part 3-c = If the players also score equally on the 'strength' function / instance, this code reports the name of the player that has the highest total score according to the 'sum_player' function / instance.
    # seedorf = Player("Clarence Seedorf", 0.1, 0.2, 0.3)
    # rijkaard = Player("Frank Rijkaard", 0.4, 0.5, 0.6) # Antwoord = 'rijkaard' omdat Rijkaard de hoogste score heeft wanneer je de score van alle 3 de attributen WEL bij elkaar opgeteld.

# Antwoord op vraag 2 part 3-d = If the players score is equal on all 3 attributes, this code returns the string: "These two players might as well be twins!
    # seedorf = Player("Clarence Seedorf", 0.1, 0.1, 0.1)
    # rijkaard = Player("Frank Rijkaard", 0.1, 0.1, 0.1)

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
    print(F"De naam van de 'Commentator' = {winter.name}")
    
    print('\n')

    print("Elaboration question 2 - part 2 = 'Sum Player':\n")
    print(winter.sum_player(seedorf))
    
    print('\n')

    print("Elaboration question 2 - part 3: a - d = 'Compare Players':\n")
    print(winter.compare_players(rijkaard, seedorf, "accuracy")) # attributes = ["speed", "endurance", "accuracy"] LET OP!!! Je kan "accuracy" op deze regel / bij deze print statement ook aanpassen in één van de andere attributen.

    print('\n')
