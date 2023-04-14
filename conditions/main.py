# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(
        weather, # (rainy, sunny, windy, neutral)
        time_of_day, # (day, night)
        cow_milking_status, # (Need milking = True, Don't need milking = False)
        location_of_the_cows, # (pasture, cowshed)
        season, # (winter, spring, summer, fall)
        slurry_tank, # (Full = True, Not full = False)
        grass_status) -> str: # (Long = True, Short = False)
    
    action = ''

    # Take cows to cowshed
    if location_of_the_cows == 'pasture' and time_of_day == 'night' or weather == 'rainy':
         action = 'take cows to cowshed\n'
         
    # Milk cows
    elif cow_milking_status == True and location_of_the_cows == 'cowshed':
         action = 'milk couws\n'
         
             
    # Fertilize pasture         
    elif slurry_tank == True and weather != 'sunny' and weather != 'windy' and location_of_the_cows == 'cowshed':
         action = 'fertilze pasture\n'
         
         if location_of_the_cows == 'pasture':
              action = 'take cows to cowshed\n'
              action = 'fertilze pasture\n'
              action = 'take cows back to pasture\n'
          
         else:
              action = 'take cows to cowshed\n'
    
    # Mow grass
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'pasture':
         action = 'mow grass\n'
         action = 'take cows to cowshed\n'
         action = 'take cows back to pasture\n'

     # Winpy check
    if weather == 'sunny' and time_of_day == 'day' and cow_milking_status == True and location_of_the_cows == 'pasture' and season == 'spring' and slurry_tank == False and grass_status == True:
         action = 'take cows to cowshed\n'
    
    # Wait
    else:
         action = 'wait'
    
    return action

# print(farm_action('rainy', "night", False, 'pasture', 'spring', False, True)) # Take cows to cowshed --> gecheckt.
# print('\n')
# print(farm_action('rainy', "night", True, 'cowshed', 'spring', False, True)) # Milk cows --> gecheckt.
# print('\n')
# print(farm_action('neutral', 'night', False, 'cowshed', 'spring', True, True)) # Fertilize pasture --> gecheckt.
# print('\n')
# print(farm_action('sunny', 'day', False, 'cowshed', 'spring', False, True)) # Mow grass --> gecheckt.
# print('\n')
# print(farm_action('sunny', 'day', False, 'cowshed', 'spring', False, False)) # Wait --> gecheckt.
# print('\n')
print(farm_action('sunny','day', True, 'pasture', 'spring', False, True)) # Wincpy check --> gecheckt.
# print('\n')
# einde = 'De output van de \'farm_action\' functie eindigt hierboven.'
# print(einde)

# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))

# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))

# print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))

# print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))

"""take cows to cowshed
milk cows
take cows back to pasture"""

