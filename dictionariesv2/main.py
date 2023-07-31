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
        passport['stamps'] = []     # Deze code zorgt ervoor dat de 'key' genaamd 'stamps' en de 'value' 'een lijst' (tezamen zijn dit de 'key-value pair') wordt toegevoegd aan de dictionary 'passport'.\
                                    # LET OP!!! Dit kan dus zonder gebruik te maken van een toevoegingscode.

    if country not in passport['stamps']:       # # Deze code gaat er samen met de '.append' code hieronder voor zorgen dat bestaande stamps / landen niet worden overschreven door nieuwe landen.
        if passport['nationality'] != country:  # Deze code controleert of het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit.
            passport['stamps'].append(country)  # Deze code zorgt ervoor dat als het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit, het land wordt toegevoegd aan de stamps dictionary.\
                                                # Deze code zorgt er ook voor dat bestaande stamps / landen niet worden overschreven door nieuwe landen.

    return passport


def add_biometric_data(name, # = str
        date_of_birth, # = str in ISO 8601 format, for example: 2002-12-31
        place_of_birth, # = str
        height, # = in meters, float
        nationality, # = str
        country, # = str
        biomatric_type,
        biomatric_value,
        biomatric_date
        ) -> dict:


    passport = {
            'name' : name,
            'date of birth' : date_of_birth,
            'place of birth' : place_of_birth,
            'height' : height,
            'nationality' : nationality,
            'stamps' : [],
    }


    if country not in passport['stamps']:       # # Deze code gaat er samen met de '.append' code hieronder voor zorgen dat bestaande stamps / landen niet worden overschreven door nieuwe landen.
        if passport['nationality'] != country:  # Deze code controleert of het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit.
            passport['stamps'].append(country)  # Deze code zorgt ervoor dat als het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit, het land wordt toegevoegd aan de stamps dictionary.\
                                                # Deze code zorgt er ook voor dat bestaande stamps / landen niet worden overschreven door nieuwe landen.

    if 'biometric' not in passport:
        passport['biometric'] = {}

        if 'biomatric type' not in 'biomatric':
            passport['biomatric type'] = biomatric_type
            
            if 'biomatric_value' not in 'biomatric':
                passport['biomatric_value'] = biomatric_value

                if ('biomatric_date') not in 'biomatric':
                    passport['biomatric_date'] = (biomatric_date)

    return passport


    # passport = {
    #     'name' : name,
    #     'date of birth' : date_of_birth,
    #     'place of birth' : place_of_birth,
    #     'height' : height,
    #     'nationality' : nationality,
    #     'stamps' : [],
    #     'biometric' : {
    #         'biomatric type' : biomatric_type,
    #         'biomatric value' : biomatric_value,
    #         'biomatric_date' : biomatric_date,

    #     },

    # }

    
    # if country not in passport['stamps']:       # # Deze code gaat er samen met de '.append' code hieronder voor zorgen dat bestaande stamps / landen niet worden overschreven door nieuwe landen.
    #     if passport['nationality'] != country:  # Deze code controleert of het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit.
    #         passport['stamps'].append(country)  # Deze code zorgt ervoor dat als het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit, het land wordt toegevoegd aan de stamps dictionary.\
    #                                             # Deze code zorgt er ook voor dat bestaande stamps / landen niet worden overschreven door nieuwe landen.

    # if 'stamps' not in passport:
    #     passport["stamps"] = []     # Deze code zorgt ervoor dat de 'key' genaamd 'stamps' en de 'value' 'een lijst' (tezamen zijn dit de 'key-value pair') wordt toegevoegd aan de dictionary 'passport'.\
    #                                 # LET OP!!! Dit kan dus zonder gebruik te maken van een toevoegingscode.

    # return passport

print('\n')
print('Below is the \'.append\' method to add someting to the pasport \'dictionary\'\n')

if __name__ == '__main__':
    countries = get_countries()
    print(create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'American'))       # Met deze code roep je de 'create_passport' functie aan.
    print(add_stamp('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'American')) # Met deze code roep je de 'add_stamp' functie aan.
    print(add_stamp('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'Dutch'))
    print(add_biometric_data('Coolio', '1993-04-19', 'New York', '1,90', 'American', 'Dutch', 'ogen', 'kleur', '2023-07-31'))
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