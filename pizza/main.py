'''
Question 5 = This is the last step! 

You just have to implement some code at main.py and make everything works!

Create a script in main.py that imports the order_management module and uses the create_order, save_orders_to_file, and load_orders_from_file functions to allow users to create new orders, save orders to a file, and view existing orders from the file. The script should display a menu with options for each of these actions, and allow the user to navigate between them.

Start by importing the 3 functions that you created from the order_management module

Write a simple function that simply prints the menu, with four numbered options: the 3 you created and 'exit' as fourth

Create a pizza_order_list as an empty list

Create an infinite loop with while that displays the function that prints the menu and ask for input.

Now use if statements to execute the functions from the orders_management module.

You will need to implement some code under every if statement to make it work perfectly.

use the break keyword if the input is 4 to stop the loop

Add a final else statement that prints some kinf of error if the input is not between 1 to 4.
'''

from order_management import create_order, save_orders_to_file, load_orders_from_file # Op deze manier kan je ook meerdere functies van een module openen.

def display_menu(): # Met deze functie wordt 'onderstaande menu weergegeven'.
    
    print("\n")
    
    print("Pizza Ordering Menu:")
    print("1. Create a new order")
    print("2. Save orders to file")
    print("3. View existing orders")
    print("4. Exit \n")

pizza_order_list = [] 

while True: # Met deze code start je de while loop om ervoor te zorgen dat je altijd deze menu altijd te raadplegen is.
    
    display_menu() # Op deze manier roep je de 'display_menu' functie aan.
    choice = input("Enter your choice (1,2,3,4) below: \n") # Met deze code geeft je de gebruiker de mogelijkheid om één van de 4 opties te kiezen van het menu.
    
    if choice == "1":                       # Met deze code zeg je: als de variabel 'choice' gelijk is aan 'het getal '1' dat door een gebruiker is ingevoerd', doe dan onderstaande.
        new_order = create_order()          # Met de variabel 'new_order' roep je de 'create_order' functie aan van het 'order_management' bestand.
        pizza_order_list.append(new_order)  # Met deze code voeg je de variabel 'new_order' (= dus de 'create_order()' functie) toe aan de 'pizza_order_list'.

    elif choice == "2":                         # Met deze code zeg je: als de variabel 'choice' gelijk is aan 'het getal '2' dat door een gebruiker is ingevoerd', doe dan onderstaande.
        save_orders_to_file(pizza_order_list)   # Met deze code zeg je: voeg de variabel 'pizza_order_list' (= waar nu de 'create_order' functie in zit d.m.v. de variabel 'new_order') toe aan het 'order.txt' bestand.
        print("Orders saved to file.\n")          # Met deze code zeg je: laat deze 'string' zien nadat de variabel 'pizza_order_list' (= waar nu de 'create_order' functie in zit d.m.v. de variabel 'new_order') is toegevoegd aan het\
                                                # 'order.txt' bestand.

    elif choice == "3":                         # Met deze code zeg je: als de variabel 'choice' gelijk is aan 'het getal '3' dat door een gebruiker is ingevoerd', doe dan onderstaande.
        orders = load_orders_from_file()        # Met deze code zeg je: laat alle orders zien die in het 'order.txt' bestand zitten.
        print("Existing Orders:\n")               # Met deze code zeg je: laat deze 'string' zien wanneer alle orders uit het 'order.txt' bestand zitten worden getoond.
        
        for categorize, order in enumerate(orders, start=1):    # Met de variabel 'categorize' ga je itereren over de gegevens in het 'order.txt' bestand.
                                                                
                                                                # De variabel 'order' gebruik je hier om '2 redenen': 1= omdat de 'enumerate' code 2 argumenten nodig heeft om het te kunnen gebruiken, 2= omdat je een variabel nodig hebt die\
                                                                # je gaat gebruiken om de nodige variabelen uit de 'order_management.py' module te halen. LET OP!!! De variabel 'order' is aan geen enkele andere code in deze modules\
                                                                # gekoppeld, dus ook al zou je de variabel 'order' vervangen voor een andere variabel (b.v. 'test' i.p.v. 'order'), dan zou de code het nog steeds doen. Dit komt vanwege de\
                                                                # punt '.' die je bij het gebruik van 'modules' gebruikt om codes uit andere modules aan te roepen. LET OP!!!! DEZE AANTEKENING NOG FF DUBBEL CHECKEN BIJ EEN WINC MENTOR.
                                                                
                                                                # De 'enumerate' code zorgt ervoor 'dat gegevens in een bestand of lijst genummerd worden'. In deze code worden dus de orders / bestellingen in het 'orders.txt' bestand\
                                                                # genummerd. LET OP!!! De 'enumerate' code gebruik je vrijwel alleen in een 'for loop'. LET OP!!! De nummering bij gebruik van de 'enumerate' code 'begint standaard bij het\
                                                                # getal 0'. Dus als als je wilt dat de nummering begint bij het getal 1 i.p.v. 0, dan moet je altijd ', start=1' achter / rechts van de variabel plaatsen (dus in deze code is\
                                                                # dat: 'enumerate(orders, start=1)').

            print(F"{categorize}. {order.customer_name} ordered {order.pizza_type} with toppings {', '.join(order.toppings)}\n")    # Met deze code / 'F-string' maak je een leesbare zin voor de gebruikers door de woorden 'ordered' en 'with'\
                                                                                                                                    # toe te voegen aan de zin + de nodige variabelen aan te roepen op de manier hoe je dat doet met modules:\
                                                                                                                                    # 'order.NAAM VARIABEL'.

            # print(F"Print statement regel 57 = {categorize}") # LET OP!!! Deze check / test print statement zie je alleen wanneer je de 'while loop' eerst stopt met 'Ctrl + C'. En dit geldt ook voor wanneer je andere aanpassingen niet ziet.
            # print('\n')

    elif choice == "4": # Met deze code zeg je: als de variabel 'choice' gelijk is aan 'het getal '4' dat door een gebruiker is ingevoerd', doe dan onderstaande.
        
        break # Met de 'break' code stop je deze 'while loop' direct (een for loop kan je ook stoppen met de 'break' code, maar dat is in deze code niet relevant).

    else: # Met deze code zeg je: als aan alle bovenstaande voorwaardes niet is voldaan, doe dan / print dan onderstaande.
        print("Invalid option. Please choose a valid option between 1 and 4.") # Deze string / print statement krijg je te zien wanneer een gebruiker een getal invoert dat NIET tussen de 1 en de 4 zit.

if __name__ == "__main__":
    
    print("\n")

    print(display_menu())

    print("\n")
    
