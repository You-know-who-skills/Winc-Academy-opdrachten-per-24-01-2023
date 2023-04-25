# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

films = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha', 'Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

make_films_lower = [films.lower() for films in films]

print(make_films_lower)

del films[:]

print(films)


# Vraag 1
def alphabetical_order(film_names: list) -> list:

    film_names.sort()

    print(film_names)
    
    return film_names


# print(alphabetical_order)


# Vraag 2
# def  won_golden_globe (won_golden_globes_for) -> bool:

#     won_golden_globes_for = ['jaws', 'star wars: episode iv -- a new hope', 'e.t. the extra-terrestrial', 'memoirs of a Geisha']
    
#     return film_names


# Vraag 3
# def remove_toto_albums(albums_to_be_removed) -> str:

#     albums_to_be_removed = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']
    
#     return film_names


