# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

def create_passport(
        name, # = str
        date_of_birth, # = str in ISO 8601 format, for example: 2002-12-31
        place_of_birth, # = str
        height, # = in meters, float
        nationality # = str
        ) -> dict:

    return {
        'name' : name,
        'date of birth' : date_of_birth,
        'place of birth' : place_of_birth,
        'height' : height,
        'nationality' : nationality,
    }


def add_stamp(
        name, # = str
        date_of_birth, # = str in ISO 8601 format, for example: 2002-12-31
        place_of_birth, # = str
        height, # = in meters, float
        nationality, # = str
        country # = str
        ) -> dict:

    passport = {
        'name' : name,
        'date of birth' : date_of_birth,
        'place of birth' : place_of_birth,
        'height' : height,
        'nationality' : nationality,
    }
    
    if 'stamps' not in passport:
        passport["stamps"] = []

    if country not in passport['stamps']:
        passport['stamps'].append(country) # Countries list of the countries that a person has been to.
    
    if nationality == country:
        passport['stamps'].remove(country)

    # print(passport)
    return passport


print('\n')
print('Below is the \'.append\' method to add someting to the pasport \'dictionary\'\n')

if __name__ == '__main__':
    countries = get_countries()
    print(create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'American'))
    print(add_stamp('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'American'))
    print(add_stamp('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'Dutch'))
    print('\n')




# Op onderstaande manier kan de code ook worden gemaakt. LET OP!!! Onderstaande manier is nog niet helemaal af


#     def create_passport(name, date_of_birth, place_of_birth, height, nationality):
#     return {
#         "name": name,
#         "date_of_birth": date_of_birth,
#         "place_of_birth": place_of_birth,
#         "height": height,
#         "nationality": nationality,
#     }


# def add_stamp(passport, country):
    
#     print(f'{passport}')
#     passport = create_passport
#     print(f"tweede passport: {passport}")

#     if "stamps" not in passport:
#         passport["stamps"] = []

#     if country not in passport["stamps"]:
#         passport["stamps"].append(country)

#     return passport


# print('\n')
# print('Below is the \'.append\' method to add someting to the pasport \'dictionary\'\n')

# if __name__ == '__main__':
#     countries = get_countries()
#     print(create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'American'))
#     print(add_stamp('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'Africa'))
#     print('\n')

    # create = create_passport("Hank Bobbiton", "1980-12-31", "Brussels", 178.52, "Belgium")
    # print(create)

    # passport = add_stamp(create, 'Brussel')
    # print(passport) 
    
    # eerste = create_passport("Hank Bobbiton", "1980-12-31", "Brussels", 178.52, "Belgium")
    # print(f"eerste: {eerste}")

    # tweede = add_stamp(eerste, countries[0])
    # print(f"tweede: {tweede}")