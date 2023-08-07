# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

print('\n')

def greet(name, greeting = 'Hello, <name>!') -> str:
    
    return greeting.replace('<name>', name)



if __name__ == "__main__":
    
    print(greet('Chuck D'))
    print('\n')