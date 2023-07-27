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
        # 'stamps' : list(country), # Countries list of the countries that a person has been to.
        'stamps' : country = [], # Countries list of the countries that a person has been to.
    }
    
    if passport not in country:
        country.append(passport)

    return passport

Test = create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'Amercan')
Test_2 = add_stamp('LA', 'America')

if __name__ == '__main__':
    countries = get_countries()
    print(create_passport())
    print(add_stamp())