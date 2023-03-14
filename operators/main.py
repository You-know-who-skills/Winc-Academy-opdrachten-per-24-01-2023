# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# Vraag 1
spain_spoken_language = 'Castilian Spanish'
switzerland_spoken_language = 'German'

# Vraag 2
spain_prevalent_religion = 'Roman Catholic'
switzerland_prevalent_religion = 'Roman Catholic'

# Vraag 3
spain_capital = 'Madrid'
switzerland_capital = 'Bern'
spain_capital_len = len(spain_capital)
switzerland_capital_len = len(switzerland_capital)

# Vraag 4
spain_GDP_2021 = 1798
switzerland_GDP_2021 = 618228

# Vraag 5
spain_population_growth = 0.13  
switzerland_population_growth = 0.65

# Vraag 6
spain_population_count = 47163418

# Vraag 7
switzerland_population_count = 8508698

print(spain_spoken_language == switzerland_spoken_language) # Vraag 1
# print('\n')
print(spain_prevalent_religion == switzerland_prevalent_religion) # Vraag 2
# print('\n')
print(spain_capital_len != switzerland_capital_len)
# print('\n')
print(switzerland_GDP_2021 < spain_GDP_2021) # Vraag 4 DEZE FF AANGEPAST NAAR KLEINER DAN VOOR DE WINCPY CHECK
# print('\n')
print(spain_population_growth < 1 and switzerland_population_growth < 1) # Vraag 5
# print('\n')
print(spain_population_count >= 10000000) # Vraag 6
# print('\n')
print(switzerland_population_count <= 10000000) # Vraag 7
