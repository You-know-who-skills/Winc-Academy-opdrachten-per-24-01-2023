# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
#score1 = 'Ruud Gullit' # = Vraag 1
#score2 = 'Marco van Basten' # = Vraag 1

#goal_0 = 32 # = Vraag 2
#goal_1 = 54 # = Vraag 2


#scorers = score1 + ' ' + str(goal_0) + ', ' + score2 + ' ' + str(goal_1) # = Vraag 3

#report = (F'{score1} scored in the {goal_0}nd minute.\n{score2} scored in the {goal_1}th minute') # = Vraag 4


#Part 2
player = 'Frank Rijkaard' # = Vraag 1

first_name = (F'{player.find(" ")} {player[0:5]}') # = Vraag 2: slicen + find

last_name_len = (F'{player.find(" ")+1} {player[6:14]} {len(player[6:14])}') # = Vraag 3: find + slicen + len

name_short = 'F. Rijkaard! ' # = Vraag 4

chant = (F'{name_short[3:] * 8}' [:-1]) # = Vraag 5
print(chant)
print(chant[1])
print(chant[-1])
print(chant[-1] != ' ')



#good_chant = (!=) Vraag 5 en 6. Deze vragen zijn niet geheel duidelijk.


#print(score1 + ' ' + str(goal_0) + ', ' + score2 + ' ' + str(goal_1)) # Part 1, vraag 3
#print('\n')
#print(scorers)
#print('\n')
#print(F'{score1} scored in the {goal_0}nd minute')
#print('\n')
#print(F'{score2} scored in the {goal_1}th minute')

#print(report)
#print('\n')
#print(first_name)
#print('\n')
#print(last_name_len)
#print('\n')
#print(chant)
#print('\n')
#print(2 != 3)