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
    
    # Take cows to cowshed
    if location_of_the_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
         action = 'take cow to cowshed'

    # Milk cows      
    elif location_of_the_cows == 'cowshed' and cow_milking_status == True:
         action = 'milk cows'

    elif location_of_the_cows == 'pasture' and cow_milking_status == True:
         action = 'take cows to cowshed\n' + 'milk cows\n' + 'take cows back to pasture'

    # Fertilize pasture
    elif slurry_tank == True and location_of_the_cows == 'cowshed' and weather != 'sunny' and weather != 'windy':
         action = 'fertilize pasture'
    
    elif slurry_tank == True and location_of_the_cows == 'pasture' and weather != 'sunny' and weather != 'windy':
         action = 'take cows to cowshed\n' + 'fertilize pasture\n' + 'take cows back to pasture'

    # Mow grass 
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'pasture':
         action = 'mow grass'

    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'cowshed':
         action = 'take cows to cowshed\n' + 'mow grass\n' + 'take cows back to pasture'
    
    else:
         action = 'wait'     
    
    return action

print(farm_action('sunny','day', True, 'pasture', 'spring', False, True)) # Wincpy check --> gecheckt.
print('\n')

einde = 'De output van de \'farm_action\' functie eindigt hierboven.'
print(einde)
print('\n')

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
# print(farm_action('sunny','day', True, 'pasture', 'spring', False, True)) # Wincpy check --> gecheckt.
# print('\n')
