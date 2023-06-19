from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# While oefening

# Antwoord op vraag 1:

def unique_koala_facts (unique_facts: list) -> list:
    
    print('Antwoord op vraag 1:')
    
    
    
    facts = unique_facts.split()
    


    print(facts)

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
    print(random_koala_fact())
