# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# Vraag 1
def greet(name):
    groet = 'Hello'
    naam = name
    return F'{groet}, {naam}!' 

vol_groet = greet('Bob')

print(vol_groet)

print('\n')

# Vraag 2
def add(a, b, c):
    return a + b + c

sum = add(5, 3, 2)

print(sum)

print('\n')

# Vraag 3
def positive(number):
    return number > 0

positief_1 = positive(50)
positief_2 = positive(-50)
positief_3 = positive(0)

print(positief_1)
print(positief_2)
print(positief_3)

print('\n')

# Vraag 4
def negative(number):
    return number < 0

negatief_1 = negative(50)
negatief_2 = negative(-50)
negatief_3 = negative(0)

print(negatief_1)
print(negatief_2)
print(negatief_3)

