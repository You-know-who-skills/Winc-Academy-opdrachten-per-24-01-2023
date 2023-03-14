# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2 # Vraag 1
price_per_kilo = 'Leek is' + ' ' + str(leek_price) + ' ' + 'euro' + ' ' 'per kilo.' # Vraag 2

# Part 2
order = 'leek 4' # Vraag 1
order_find = order[order.find(" "):] [+1] # Vraag 2'
order_total = int(order_find) # Vraag 3
sum_total = leek_price * order_total # Vraag 4

# Part 3
broccoli_costs = 2.34 # Vraag 1
broccoli_order = 1.6 # Vraag 1
total_price_1 = broccoli_costs * broccoli_order # Vraag 2
total_price_2 = round(total_price_1, 2) # Vraag 2
total_order = str(broccoli_order) + 'kg' + ' ' + 'broccoli' + ' ' + 'costs' + ' ' + str(total_price_2) + 'e' # Vraag 3 


# Part 1
print(price_per_kilo) # Vraag 2
# print('\n')

# Part 2
# print(order_find) # Vraag 2
# print('\n')
print(sum_total) # Vraag 4
# print('\n')

# Part 3
# print(total_price_2) # Vraag 2
# print('\n')
print(total_order)