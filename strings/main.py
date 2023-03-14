# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer1 = 'Ruud Gullit' # = Vraag 1
scorer2 = 'Marco van Basten' # = Vraag 1

goal_0 = 32 # = Vraag 2
goal_1 = 54 # = Vraag 2


scorers = scorer1 + ' ' + str(goal_0) + ', ' + scorer2 + ' ' + str(goal_1) # = Vraag 3

report = (F'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute') # = Vraag 4

# Part 2
player = 'Frank Rijkaard' # = Vraag 1

first_name = player[0:player.find(" ")] # = Vraag 2: slicen + find

# first_name_2 = player[0:player.find(" ")] [-4:] # = Vraag 2: slicen + find LET OP!!! Deze string heb ik uitgecommentarieerd om te oefenen met de index waarbij je een min getal gebruikt vóór de dubbele punt.

last_name_len = len(player[player.find(" "):] [:-1]) # = Vraag 3: find + slicen + len

name_short = player[0:1] + '.' + ' ' +  player[player.find(" ")+1:] # = Vraag 4

chant = (F'{first_name}! ' * len(first_name)) [:-1] # = Vraag 5

# chant_2 = ((first_name + '!' + ' ') * len(first_name)) [:-1] # = Vraag 5 --> LET OP!!! Op deze manier is het ook mogelijk.

# chant_3 = (F'{first_name}! '* 5) [:-1] # = Vraag 5: Met deze OUDE code wordt het aantal chants niet aangepast aan het aantal karakters van de voornaam.

good_chant = (chant[-1] != ' ') # = Vraag 6


# Part 1
print(scorer1) # Part 1: vraag 1
print('\n')
print(scorer2) # Part 1: vraag 1
print('\n')
print(goal_0) # Part 1: vraag 2
print('\n')
print(goal_1) # Part 1: vraag 2
print('\n')
print(scorers) # Part 1: vraag 3
print('\n')
print(report) # Part 1: vraag 4
print('\n')

# #Part 2
print(player) # Part 2: vraag 1
print('\n')
print(first_name) # Part 2: vraag 2
print('\n')
# print(first_name_2) # Part 2: vraag 3
print('\n')
print(last_name_len)
print('\n')
print(name_short) # Part 2: vraag 4
print('\n')
print(chant) # Part 2: vraag 5
print('\n')
# print(chant_2)
# print(chant_3)
print(good_chant) # Part 2: vraag 6
