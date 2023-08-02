from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# While oefening

# Antwoord op vraag 1:

def unique_koala_facts (requested_facts: int) -> list:
    
    print('Elaboration question 1:\n')
    
    # len_facts = len(facts)
    # print(len_facts)
    
    unique_facts = [] # Deze variable betreft een lijst waarin alle unieke feiten komen die je qua aantal wilt zien met de functie 'unique_koala_facts', b.v. 2, 4 of 6 unieke feiten.
        
    count_begin, count_end = 0, 1000    # Met deze code geef je aan hoe vaak de 'while loop' moet gaan loopen door aan te geven bij welk punt / getal de loop moet beginen\
                                        # en bij welk punt / getal de loop moet eindigen.
    
    while len(unique_facts) < requested_facts: # Met deze code geef je aan dat zolang 'het aantal' unieke feiten in de variabel / lijst 'unique_facts' minder / kleiner is dan de variabel\
        # print(requested_facts)               # 'requested_facts', de loop door moet blijven gaan.

        fact = random_koala_fact() # Met deze variabel roep je de 'random_koala_fact' functie aan.
        
        if fact not in unique_facts:    # Met de code op deze 2 regels zeg je het volgende: 'Als de variabel 'fact' (waarin de functie 'random_koala_fact()' zit (= is het json bestand met alle\
            unique_facts.append(fact)   # willekeurige koala feiten)) niet in de 'unique_facts' lijst zit, voeg deze feit dan toe aan de 'unique_facts' lijst.
                                        # De code op deze 2 regels zorgt er tevens voor dat je geen dubbele feiten krijgt in de 'unique_facts' lijst. Dit doordat je aangeeft dat\
                                        # alleen als een feit uit het 'random_koala_fact() / jason bestand' nog niet in de 'unique_facts' lijst staat, dan pas het feit mag worden\
                                        # toegevoegd aan de 'unique_facts' lijst.

        if count_begin > count_end: # Met de code op deze 2 regels geef je aan dat als de het startpunt van aantal loops (= 'count_begin' = 0) meer is dan\
            break                   # het eindpunt van het aantal loops (= 'count_end' = 1000), pauzeer dan de loop met de 'break' statement.

        count_begin += 1 # Met deze code tel je 1 op bij de variable 'count begin'.
            
    return unique_facts




# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    
    # facts = (random_koala_fact) # 1e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    # unique_koala_facts(random_koala_fact()) # 2e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    print('\n')
    print('Below are the results of the amount of \'koala facts\' which you can choose by entering a number in the \'unique_koala_facts\' function:\n')
    print(unique_koala_facts(2))
        