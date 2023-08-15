from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# While oefening

# Antwoord op vraag 1:

print('\n')



def unique_koala_facts (requested_facts: int) -> list:
        
    unique_facts = [] # Deze variable betreft een lijst waarin alle unieke feiten komen die je qua aantal wilt zien met de functie 'unique_koala_facts', b.v. 2, 4 of 6 unieke feiten.
        
    count_begin, count_end = 0, 1000    # Met deze code geef je aan hoe vaak de 'while loop' moet gaan loopen door aan te geven bij welk punt / getal de loop moet beginen\
                                        # en bij welk punt / getal de loop moet eindigen.
    
    while len(unique_facts) < requested_facts: # Met deze code geef je aan dat zolang 'het aantal' unieke feiten in de variabel / lijst 'unique_facts' minder / kleiner is dan de variabel\
        # print(requested_facts)               # 'requested_facts', de loop door moet blijven gaan.

        fact = random_koala_fact() # Met deze variabel roep je de 'random_koala_fact' functie aan.
        
        if fact not in unique_facts:    # Met de code op deze 2 regels zeg je het volgende: 'Als de variabel 'fact' (waarin de functie 'random_koala_fact()' zit (= is het json bestand met alle\
            unique_facts.append(fact)   # willekeurige koala feiten)) niet in de 'unique_facts' lijst zit, voeg deze feit dan toe aan de 'unique_facts' lijst.
                                        # De code op deze 2 regels zorgt er tevens voor dat je geen dubbele feiten krijgt in de 'unique_facts' lijst. Dit doordat je aangeeft dat\
        # count_begin += 1              # alleen als een feit uit het 'random_koala_fact() / jason bestand' nog niet in de 'unique_facts' lijst staat, dan pas het feit mag worden\
                                        # toegevoegd aan de 'unique_facts' lijst.

        if count_begin > count_end: # Met de code op deze 2 regels geef je aan dat als het startpunt van het aantal loops (= 'count_begin' = 0) meer is dan\
            break                   # het eindpunt van het aantal loops (= 'count_end' = 1000), pauzeer dan de loop met de 'break' statement.

        count_begin += 1    # Met deze code tel je 1 op bij de variable 'count begin'. Deze code kan je ook tussen de 'if' statements hierboven plaatsen b.v. op regel 30,\
                            # maar dan buiten de if statements qua tab / indentation.
            
    return unique_facts


# Antwoord op vraag 2:

def num_joey_facts () -> int:

    fact = random_koala_fact() # Deze variabel pakt 1 willekeurige koala feit.
    
    count_first_joey, count_total_joey = 0, 0   # Met de variabel 'count_first_joey' geef je aan dat het aantal loops bij 0 moet beginnen.\
                                                # Met de variabel 'count_total_joey' geef je ook aan dat het aantal loops bij 0 moet beginnen.
    unique_facts = [] # Deze variable is de lijst waarin de unieke feiten van de koala's komen.
    
    while count_first_joey < 10:    # Met de variabel 'count_first_joey' start ik de while loop. En met de '< 10' code geef ik aan dat het\
                                    # eerste feit maximaal 10 gezien moet worden.
        
        another_joey_fact = random_koala_fact()  # Met deze variabel zorg je ervoor dat er naar een andere feit gezocht kan worden\
                                                # na / naast het zoeken naar een feit bij de variabel 'fact' hierboven.
        
        if fact == another_joey_fact:    # Met deze 'if' statement geef je aan dat als een feit bij de variabel 'fact' gelijk is aan een feit bij de variabel\
            count_first_joey += 1       # 'another_joey_fact', er bij de variabel 'count_first_joey' er 1 bij opgeteld moet worden\
                                        #  met de '+= 1' code. Op deze manier zoekt de variabel 'count_first_joey' altijd naar een volgende feit.
        if another_joey_fact not in unique_facts:    # Met deze 'if' statement check je of een nieuw gevonden feit van de variabel 'get another fact'\
            unique_facts.append(another_joey_fact)   # al in de lijst / variabel 'unique_facts' voor komt / is geplaatst. Zo niet,\
                                                    # dan wordt deze toegevoegd met de '.append' code.
            if 'joey' in another_joey_fact.lower():  # Met deze 'if' statement doe je 3 dingen: 1= als het item 'joey' wel voor komt in de variabel\
                count_total_joey +=1                # 'another_joey_fact' (2= maak alle letters in de variabel 'another_joey_fact' klein),\
                                                    # voeg deze feit dan toe aan de variabel 'count_total_joey'.
    # return count_total_joey # Deze return statement keurt wincpy welgoed.
    return (F' Dit is de uitkomst van de return statement: {count_total_joey}') # Deze return statement werkt ook én is ook goed, maar wincpy keurt het helaas niet goed.


def koala_weight() -> int:

    facts = random_koala_fact()

    count_first_weight, count_total_weight = 0, 0

    weight_facts = []
    
    while 'kg' not in facts:
                
        another_weight_fact = random_koala_fact()
        
        if facts == another_weight_fact:
            count_first_weight += 1
            
        if 'kg' in another_weight_fact:
            weight_facts.append(another_weight_fact.split()[-1])
            # weight_facts.append(another_weight_fact.split())
            weight_fact_split = str(weight_facts.split()[0])
            break 
    
    # return weight_facts
    return weight_fact_split
    




# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    
    # facts = (random_koala_fact) # 1e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    # unique_koala_facts(random_koala_fact()) # 2e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    
    print('Elaboration question 1:\n')
    print('Below are the results of the amount of \'koala facts\' which you can choose by entering a number in the \'unique_koala_facts\' function:\n')
    print(unique_koala_facts(2))

    print('\n')
    
    print('Elaboration question 2:\n')
    print('Below are the unique \'koala facts\' which contain the word / name \'joey\':\n')
    print(num_joey_facts())
    
    print('\n')
    
    print('Elaboration question 3:\n')
    print(koala_weight())
    print('\n')