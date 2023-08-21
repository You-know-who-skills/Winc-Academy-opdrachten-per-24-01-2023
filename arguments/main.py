# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

print('\n')

def greet(name, greeting = 'Wassup, <name>!') -> str:
    
    return greeting.replace('<name>', name)


def force(mass: float, body: str = 'earth') -> int:

    body = {
        'MERCURY': 0.330,
        'VENUS' : 4.87,
        'EARTH' : 5.97,
        'MOON' : 0.073,
        'MARS' : 0.642,
        'JUPITER' : 1898,
        'SATURN' : 568,
        'URANUS' : 86.8,
        'NEPTUNE' : 102,
        'PLUTO' : 0.0130
        }
    

if __name__ == "__main__":
    
    print(greet('Chuck D'))
    print('\n')
    print(force())