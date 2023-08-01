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
        'nationality' : nationality
    }


def add_stamp(passport, country) -> dict:

    if 'stamps' not in passport:
        passport['stamps'] = []     # Deze code zorgt ervoor dat de 'key' genaamd 'stamps' en de 'value' 'een lijst' (tezamen zijn dit de 'key-value pair') wordt toegevoegd aan de dictionary 'passport'.\
                                    # LET OP!!! Dit kan dus zonder gebruik te maken van een toevoegingscode, b.v. de '.append' code.

    if country not in passport['stamps']:       # Deze code gaat er samen met de '.append' code hieronder voor zorgen dat bestaande stamps / landen niet worden overschreven door nieuwe landen.
        if passport['nationality'] != country:  # Deze code controleert of het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit.
            passport['stamps'].append(country)  # Deze code zorgt ervoor dat als het land / de woonplaats van een persoon niet hetzelfde is als zijn nationaliteit, het land wordt toegevoegd aan de stamps dictionary.\
                                                # Deze code zorgt er ook voor dat bestaande stamps / landen niet worden overschreven door nieuwe landen.
    return passport


def add_biometric_data(
        passport,
        biometric_type,
        biometric_value,
        biometric_date
        ) -> dict:

    if 'biometric' not in passport:
        passport['biometric'] = {} # Met deze code maak je een geneste dict aan.

    biometric_data = {'value' : biometric_value, 'date' : biometric_date} # Met deze code maak je wederom een geneste dict aan om de 'key-value pairs' in te plaatsen.
    # biometric_data = {'type' : biometric_type, 'value' : biometric_value, 'date' : biometric_date}

    passport['biometric'][biometric_type] = biometric_data # Met deze code wijs je de 'geneste' 'biometric_data' dict toe aan de 'geneste' biometric dict.
        
    return passport

print('\n')

print('Below is the \'.append\' method to add someting to the pasport \'dictionary\'\n')

if __name__ == '__main__':
    countries = get_countries()
    
    passport = create_passport('Coolio', '1993-04-19', 'New York', '1,90', 'American')  # Met deze code maak je eerst een validatie aan voor de 'passport' dict zodat je de passport 'validatie' weer kunt gebruiken om\
    print(passport) # Met deze code roep je de 'passport' functie aan.                  # de volledige 'dict' op te roepen in de andere functies i.p.v. de 'key-value pairs van de passport dict handmatig te kopieren en\
                                                                                        # plakken in de andere functies (wat ik eerst deed vóór het gesprek met mentor Niels).
    stamp = add_stamp(passport, 'American')
    print(stamp) # Met deze code roep je de 'add_stamp' functie aan.

    stamp_2 = add_stamp(passport, 'Dutch') # 'Dit is even een dubbele visuele check om in de output te controleren of het land die in de 'stamp' staat inderdaad niet wordt geprint als deze gelijk is aan het land van de nationaliteit.
    print(stamp_2) # Met deze code roep je de 'add_stamp' functie aan.
    
    biometric = add_biometric_data(stamp, 'eyes', 'colour', '2023-07-31')
    print(biometric) # Met deze code roep je de 'add_biometric_data' functie aan.
    
    print('\n')
