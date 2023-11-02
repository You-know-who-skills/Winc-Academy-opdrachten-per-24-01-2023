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

    def __init__(self, customer_name: str, pizza_type: str, toppings: list, order_time  = None, is_delivered = False,):

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
            
            file.write(f"{order.customer_name}, {order.pizza_type}, {'|'.join(order.toppings)}, {order.order_time}, {order.is_delivered}\n")
            
            # Met bovenstaande code geef je aan wat er in de variabel 'order_list' moet komen te staan om er vervolgens over te kunnen itereren, en ik heb dit gedaan met een 'F-string'.
            # Omdat je gebruik maakt van modules in deze code / dit bestand, kan je de punt '.' gebruiken om variabelen te koppelen met / verwijzen naar andere variabelen.
            # Met de '.write()' code geef je aan wat er in het bestand 'order.txt' moet komen te staan / moet worden geschreven.
            # Met de '|' teken + de '.join()' code geef je aan dat alle toppings bij elkaar geplaatst moeten worden én dat ze gescheiden moeten worden met de '|' teken. Met de '.join()' code kan je namelijk losstaande items in een lijst\
            # samenvoegen door 'vóór' de '.join()' code aan te geven 'met wat' je de items wilt samenvoegen.


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

    with open('./orders.txt', 'r') as file: # De 'with' statement / code kan je gebruiken om een blok met / regel van code uit te (laten) voeren. Met de 'open()' code kan je bestanden openen. Met de letter / code 'r' (dat voor 'read' staat)\
                                            # in deze code geef je aan dat je het geopende bestand in Python wil lezen. En met de 'as file' code geef je aan dat je het bestand 'orders.txt' met / als de variabel 'file' wilt lezen. Met ander\
                                            # woorden: het bestand 'orders.txt' = nu file geworden / is opnieuw gedefinieerd en is in Python 'file' geworden.

        for order in file:                          # Met de variabel 'order' ga je itereren over de gegevens die in het bestand 'orders.txt' staan. En het itereren over gegevens in een extern bestand (b.v. een 'txt' bestand zoals in deze\
            order_data = order.strip().split(', ')  # oefening) is dus ook mogelijk.
                                                    # Met de '.strip()' code verwijder je onnodige witte / blanco gedeeltes aan het begin én einde van een string. En met de '.split()' code maak je van een 'string' een 'lijst' waarbij je van\
            # print(order_data)                     # 'elk woord' / 'item' in de string een 'lijst item' maakt.
            
            if len(order_data) == 5:    # Met deze code zeg je: als de lengte in de lijst 'order_data' gelijk is aan 5 items, voer dan onderstaande code uit. En het aantal bepaal je in de 'PizzaOrder class', hierboven bij de\
                                        # 'if len(order_data) == 5' statement, hieronder bij het uitpakken / de volgorde bepaling bij de variabel 'order_data' én ook hieronder bij de variabel 'order'.
                
                customer_name, pizza_type, toppings, order_time, is_delivered = order_data  # Door de variabel 'order_data' 'achter' deze 5 variabelen / items te plaatsen, 'pak je deze variabelen uit' LET OP!!! Met 'uitpakken' wordt bedoeld\
                                                                                            # dat je op deze manier bepaald op welke plek / in welke volgorde de variablelen / items komen te staan in de lijst. Dus in deze code zal de\
                                                                                            # variabel 'customer_name' altijd als eerste komen te staan in de lijst.

                toppings = toppings.split('|')  # Met deze code geef je aan dat de variabel 'toppings' moet zoeken naar de '|' teken en vervolgens daarop moet gaan splitten. LET OP!!! Omdat ik bij de 'save_orders_to_file(order_list):'
                                                # functie heb aangegeven dat alle toppings bij elkaar geplaatst moeten worden én dat ze gescheiden moeten worden met de '|' teken door gebruik te maken van de '.join()' code.
                # print(F"De 'toppings' print statement = {toppings}.\n") # Print statement om te checken hoe de 'toppings' code eruit ziet.
                
                order_time = dt.strptime(order_time, "%Y-%m-%d %H:%M:%S.%f")    # Met deze code geef je de tijd mee in ISO 8601 formaat. De variabel 'order_time' staat nogmaals tussen haakjes omdat de 'strptime()' code waarschijnlijk\
                                                                                # 2 argumenten nodig heeft om te werken. LET OP!!! Ik schrijf 'waarschijnlijk' omdat ik hieronder de 'strptime()' ook heb gebruik met 1 argument en de code\
                                                                                # doet het nog steeds. Dus het is mij nog niet geheel duidelijk of de 'strptime()' code nou wel of niet met 2 argumenten gebruikt kan worden.
                # order_time = dt.strptime("%Y-%m-%d %H:%M:%S.%f")              # Deze code werkt dus ook zo ver ik kan zien in het 'orders.txt bestand'.

                is_delivered = is_delivered == 'True'   # Het is niet geheel duidelijk waarom deze code is hier is gezet, want volgens mentor Christiaan gebruik je deze code niet meer in deze oefening. Maar als de pizza is bezorgd, moet de\
                                                        # bezorger waarschijnlijk nog iets digitaals doen zodat deze code gaat werken.

                order = PizzaOrder(customer_name, pizza_type, toppings, order_time, is_delivered)   # Hier definieer je de variabel 'order' opnieuw met de PizzaOrder class omdat je 3 van de 5 variabelen anders hebt gedefinieerd hierboven.\
                                                                                                    # LET OP!!! Je definieert de variabel 'order' met de class 'PizzaOrder' hier ook opnieuw zodat je elke variabel individueel weer kunt\
                                                                                                    # aanroepen in het 'main.py' bestand op deze manier: 'order.customer_name' enz.
                
                orders.append(order) # Met deze code voeg je de (inhoud van de) variabel 'order' toe aan de lijst 'orders' aan het begin van deze instance hierboven.

            else: # Met deze code zeg je: wanneer niet aan bovenstaande code is voldaan, voer dan onderstaande code uit.
                # print(F"Invalid data format in the line: {order.strip()}") # Dit is de code uit de Winc uitwerking
                raise ValueError(F"Please check this order, because something is not right: {order.strip()}.\n") # Maar deze code is ook goed.
                
                # LET OP!!! De 2 error meldingen hierboven krijg je pas te zien als je / iemand zelf (per ongeluk) een aanpassing aanbrengt in het 'aantal itmes' in het 'orders.txt' bestand. Het 'orders.txt' bestand bestaat namelijk uit de\
                # 5 gedefinieerde items: 1 = customer_name, 2 = pizza_type, 3 = toppings, 4 = order_time, en 5 = is_delivered. En je kan dit zien doordat de items in het 'orders.txt' bestand worden gescheiden met een komma door de volgende\
                # code die ik hierboven heb aangemaakt: 'order_data = order.strip().split(', ')'. Als er dus een 6e item bij komt of 1 item wordt verwijderd, krijg je 1 van de hierboven vermeldde foutmeldingen.
                
        return orders


if __name__ == "__main__":

    order = PizzaOrder("Customer_name", "Pizza_type", "Toppings")
    # order = PizzaOrder("dit", "dat", "enzo")
    
    # create_order()
    
    orders = create_order()
    # order_2 = create_order()
    
    print(save_orders_to_file([orders]))

    print(load_orders_from_file())



