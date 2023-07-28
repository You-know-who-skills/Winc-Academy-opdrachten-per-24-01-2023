# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(
        name, # (str)
        date_of_birth, # (str in ISO 8601 format, for example: 2002-12-31)
        place_of_birth, # (str)
        height, # (in meters, float)
        nationality # (str)
        ) -> dict:

    return {
        'name' : name,
        'date_of_birth' : date_of_birth,
        'place_of_birth' : place_of_birth,
        'height' : height,
        'nationality' : nationality,
    }
    

def add_stamp(passport: dict, country: str) -> dict:

    passport = {
        'name' : '',
        'date_of_birth' : '',
        'place_of_birth' : '',
        'height' : '',
        'nationality' : '',
    }
    
    if 'stamps' not in passport:
        passport.append['stamps'] = []  # Countries list of the countries that a person has been to.
        # passport['stamps'].append([]) # Countries list of the countries that a person has been to.


    return passport

print('Below is the \'.append\' method to add someting to the pasport \'dictionary\'\n')

Test = create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'Amercan')
Test_2 = add_stamp('LA', 'America')

if __name__ == '__main__':
    countries = get_countries()
    print(create_passport())
    print(add_stamp())