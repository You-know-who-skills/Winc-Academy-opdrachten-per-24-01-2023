'''
Question 1 part 1 = Create a module named 'order_management.py'.
'''

'''
Question 1 part 2 = Import the 'datetime object' from the 'datetime module' and give it the alias 'dt'.
'''

from datetime import datetime as dt # In de oefening stond niet dat je het 'datetime object' moest importeren van de 'datetime module'. Dus na een gesprek met een Winc mentor op dinsdag 17-10-2023 tussen 11:00 en 11:45 uur ben ik hierachter\
                                    # gekomen.


'''
Question 1 part 3 = Define a class named 'PizzaOrder' in the 'order_management module' with the attributes shown below.

- customer_name = string

- pizza_type = string

- toppings = list of strings

- order_time = datetime object. 

- is_delivered = boolean

'Order_time' and 'is_delivered' must be default attributes, so set them as 'None' and 'False' respectively.

Define all the attributes as usual. The only different must be 'order_time'. Define it as 'order_time if order_time else dt.now()'.
'''

class PizzaOrder():

    def __init__(self, customer_name: str, pizza_type: str, toppings: list, order_time  = None, is_delivered = False):

        self.customer_name = customer_name
        self.pizza_type = pizza_type
        self.toppings = toppings
        self.order_time = order_time if order_time else dt.now()
        self.is_delivered = is_delivered


'''
Question 2 = Create a function in the 'order_management' module called 'create_order' which takes input from the user for the attributes of a 'PizzaOrder object' and returns a PizzaOrder object.

Within the function, create 3 variables with the same names that you used at the PizzaOrder class for:

- customer_name;
- pizza_type;
- and toppings.

At every variable, use te 'input()' function and write a nice 'prompt' to receive an answer. The real value of the variable will be the one given by the user at the console.

For the 'toppings' you need to do something extra: ask the user to separate the toppings with commas, and then add the '.split()' method at the end using the comma as a separator to create a list.

Return an 'instance' of PizzaOrder, with the 3 arguments / variables as attributes.
'''


def create_order(): # Dit stond niet in de oefening, maar deze functie moet buiten de class worden geplaatst. Dus na een gesprek met een Winc mentor op dinsdag 17-10-2023 tussen 11:00 en 11:45 uur ben ik hierachter gekomen.

    customer_name = input("Please enter your name: ")   # Met de 'input()' code zorg je ervoor dat de gebruiker iets in kan vullen. LET OP!!! De input code werkt ook zonder dat je de variabel print(customer_name) definieert.
    
    pizza_type = input("Please choose your pizza type: ")
    # print(pizza_type)

    toppings = input("Please choose your toppings and please separate each topping with a comma: ").split(",")  # Door de 'split()' code hier te gebruiken met de komma als separator, zorg je ervoor dat de items in deze input worden\
    # print(toppings)                                                                                           # gescheiden door de komma.

    return PizzaOrder(customer_name, pizza_type, toppings) # Met deze 'return' statement zorg je ervoor dat de gebruiker iets kan invullen bij de 3 variabelen die hierboven staan.


'''Question 3 = Save the order to a file.

The next function will save the order to a file. In this function we are going to use the 'with' statement.

You will need to access a 'txt' file and write in it with Python. We will use the 'open()' function and the '.write()' method.

Define a function called 'save_orders_to_file' in the 'order_management' module, which takes a list of 'PizzaOrder' objects (order_list, for example) and saves them to a file named "orders.txt" in the current directory. Each PizzaOrder\
object should be written to a new line in the file.

Create a 'orders.txt' file in your project folder. Use the with statement to open the file: 'with open('./orders.txt', 'w') as file:' With this we are opening the file by giving the path and writing mode as arguments.

Within the 'with' statement, add a 'for loop' to iterate among pizzas in the 'order_list' and make it write an 'f-string' that uses the attributes of the pizza object:

- '(file.write())'

It's vital to use the newline character '(/n)' at the end of the string, so every pizza is written in a new line of the '.txt file'.
'''

def save_orders_to_file(order_list):

    with open('./orders.txt', 'w') as file: # De 'with' statement / code kan je gebruiken om een blok met / regel van met code uit te (laten) voeren. Met de 'open()' code kan je bestanden openen. Met de letter 'w' (dat voor 'write' staat)\
                                            # in deze code geef je aan dat je in het geopende bestand wil gaan schrijven.

        for order in order_list: # Met de variabel 'order' ga ik itereren over alles wat in de variabel 'order_list' staat. En hieronder ga ik bepalen wat er in 'order_list' komt te staan.
            
            file.write(F"{order.customer_name}, {order.pizza_type}, {order.toppings}\n")    # Met deze code geef je aan wat er in de 'order_list' variabel moet komen te staan om erover te kunnen itereren. En dit heb ik gedaan middels een\
                                                                                            # 'F-string'.


'''
Question 4 = 

One more order to go!
Now we want the opposite. To retrieve orders from the .txt file.
Remember that we stored the orders in separate lines? Those are going to be our iterables.

Here we are going to make use of the datetime module. You can read the documentation, or follow the steps precisely if you don't feel like digging on it too much.

Define a function named load_orders_from_file in the order_management module, which loads PizzaOrder objects from the "orders.txt" file and returns them as a list.

Within the function, start by creating a variable orders as an empty list.

Use the while statement, this time to read the file:

And then add a for loops that iterates among the lines of the file and creates separate "words" for every string:

with open('./orders.txt', 'r') as file:
    for line in file:
      order_data = line.strip().split(', ')

Add ad if-else statement. If the order_data is made of 5 items, let's define them. Else, rise an error (write a sentence)

Redefine order_data as a list made of the 5 objects that we want inside. You can do this with the unpacking method if you use this syntax:

customer_name, pizza_type, toppings, order_time, is_delivered = order_data

Inside the if statement you still need to define toppings, order_time, is_delivered and the order itself, that needs to be appended to the list.
If you struggle with this, use the hint below.

Remember to finish it with the else part of the statement.

Make it return orders
'''

def load_orders_from_file():

    orders = []

    with open('./orders.txt', 'r') as file: # De 'with' statement / code kan je gebruiken om een blok met / regel van met code uit te (laten). Met de 'open()' code kan je bestanden openen. Met de letter 'r' (dat voor 'read' staat) in deze\
                                            # code geef je aan dat je het geopende bestand wil lezen.
    
        for order in file:
            order_data = order.strip().split(', ')

            if len(order_data) == 5:
                
                customer_name, pizza_type, toppings, order_time, is_delivered = order_data

                toppings = toppings.split('|')
                # order_time = dt.strptime(order_time, "%Y-%m-%d %H:%M:%S.%f")
                is_delivered = is_delivered == 'True'
                order = PizzaOrder(customer_name, pizza_type, toppings, order_time, is_delivered)
                orders.append(order)

            else:
                raise ValueError(F"Please make sure that every line is filled in correctly.\n")
            
            return orders


if __name__ == "__main__":

    order = PizzaOrder("dit", "dat", "enzo")
    
    order_1 = create_order()
    # order_2 = create_order()
    
    print(save_orders_to_file([order_1]))

    print(load_orders_from_file())



