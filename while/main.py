from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# While oefening

# Antwoord op vraag 1:

def unique_koala_facts (facts: int) -> list:
    
    print('Antwoord op vraag 1:')

    while facts < range(1000):
        print(facts)

    # print('\n')
    
    # print('\n')
    
    # print(facts, len([facts]))
    # print('\n')

    # unique_facts = []
    
    # koala = (len([facts]))
    # unique_facts.append(facts)
    # print(koala)
    # print('\n')


    
    # facts range(1000)
    # print(facts)
    
    # facts = unique_facts(key=len)

    # unique_facts.append(facts)
    # print(facts)
    # print(unique_facts)
        
    




    # while facts in unique_facts:
    #     if len(unique_facts) < range(1000):
    #         print(facts)
    
    # while unique = list(unique_facts.split)
    # print(unique)

    # while unique_facts < range(1000):
    #     # print(list(unique_facts.split))
    #     print(len(unique_facts))



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    facts = (random_koala_fact) # 1e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    # unique_koala_facts(random_koala_fact()) # 2e Manier om het 'random_koala_fact' bestand aan te roepen in je functie.
    
    print(unique_koala_facts(facts))
    