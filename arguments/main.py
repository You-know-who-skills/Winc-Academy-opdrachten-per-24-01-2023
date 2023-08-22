# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

print('\n')

def greet(name, greeting = 'Wassup, <name>!') -> str:
    
    return greeting.replace('<name>', name)


def force(mass: float, body: str = 'earth') -> int:

    bodies = {
        'mercury': 3.7,
        'venus' : 8.9,
        'earth' : 9.8,
        'moon' : 1.6,
        'mars' : 3.7,
        'jupiter' : 23.1,
        'saturn' : 9.0,
        'uranus' : 8.7,
        'neptune' : 11.0,
        'pluto' : 0.7,
        }
        
    return mass * round(bodies[body], 1) # Je kan de code / formule direct in de return statement plaatsen of eerst een variabel aanmaken waarin je de code / formule plaatst en daarna returned.

'''
Op bovenstaande manier gebruik je de 'round(,)' code om binnen een 'dict' de 'waarde' / 'value' van een 'key' te benaderen:
1 = Start met het openen van de round code --> round(
2 = Geef de naam van de dict op als --> bodies
3 = Gebruik de / een parameter om bij de waarde te komen --> [body]
4 = Geef aan op hoeveel decimalen de waarde / value moet eindigen --> , 1
5 = Sluit de round code --> )
'''


def pull(m1: float, m2: float, d: float) -> int:

    G = 6.674 * 10**11

    pull = G * ((m1 * m2) / d**2)
    
    return pull

'''
De 'pull' functie van hierboven snap ik nog niet, dus deze heb ik gewoon overgenomen van de uitwerking in de lesstof van de module, want ik was ff helemaal klaar\
met alle onduidelijke en foutieve vraagstellingen in de lesstof van de module.
'''


if __name__ == "__main__":
    
    print("Hieronder staat het antwoord op vraag 1:'\n")
    print(greet('Chuck D'))
    
    print('\n')

    print("Hieronder staat het antwoord op vraag 2:'\n")
    print(force(9, 'venus'))
    
    print('\n')

    print("Hieronder staat het antwoord op vraag 3:'\n")
    print(pull(6, 10, 11))


