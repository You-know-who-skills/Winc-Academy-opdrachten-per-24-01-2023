# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Vraag 1
films = []

# Vraag 2
gg_films = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha']

# gg_films_lower = [gg_films.lower() for gg_films in gg_films]

# print(gg_films_lower)



# won = ''

# Vraag 3
tidy_list = ['Jaws', 'Star Wars: Episode iv -- A New Hope', 'E.T. The Extra-Terrestrial', 'Memoirs of a Geisha', 'Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

# tidy_list = wrong_list.capitalize() # for wrong_list in wrong_list

# test = wrong_list[.find('Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New')]



# print(capitalized)

# print(tidy_list)

# tidy_list = ''

# print(gg_films_lower)




# print(films_lower)

# del films[:]

# print(films)


# Vraag 1
def alphabetical_order(films: list) -> list:

    films.sort()

    return films

print(alphabetical_order(films))
print('\n')

# Vraag 2
def won_golden_globe(won: list) -> bool:

    gg_films_lower = [gg_films.lower() for gg_films in gg_films]

    if won in gg_films_lower:
       print(won, "is", True)
       return True
    
    else:
       print(won, "is", False)
    
    return False

won_golden_globe("jaws")
won_golden_globe("jeff")
print('\n')

print(won_golden_globe(gg_films))
print('\n')


# Vraag 3
def remove_toto_albums(tidy_list) -> list:
    
    if "Fahrenheit" in tidy_list:
        tidy_list.remove("Fahrenheit")
    
    if "The Seventh One" in tidy_list:
        tidy_list.remove("The Seventh One")

    if "Toto XX" in tidy_list:
        tidy_list.remove("Toto XX")

    if "Falling in Between" in tidy_list:
        tidy_list.remove("Falling in Between")

    if "Toto XIV" in tidy_list:
        tidy_list.remove("Toto XIV")

    if "Old Is New" in tidy_list:
        tidy_list.remove("Old Is New")

    
    
    return tidy_list

print('\n')
print(remove_toto_albums(tidy_list))





# #     albums_to_be_removed = 
    
# #     return film_names

# # del wrong_list['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

# # tidy_list = remove_toto_albums(wrong_list)

# # print(tidy_list)
