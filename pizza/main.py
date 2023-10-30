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

def display_menu(): # Met deze instance wordt 'onderstaande menu weergegeven'.
    
    print("Pizza Ordering Menu:")
    print("1. Create a new order")
    print("2. Save orders to file")
    print("3. View existing orders")
    print("4. Exit")

pizza_order_list = [] 

while True: # Met deze code start je de while loop om ervoor te zorgen dat je altijd deze menu altijd te raadplegen is.
    
    display_menu() # Op deze manier roep je de 'display_menu' functie aan.
    choice = input("Enter your choice (1,2,3,4): ") # Met deze code geeft je de gebruiker de mogelijkheid één van de 4 opties te kiezen van het menu.

    if choice == "1": # 
        new_order = create_order()
        pizza_order_list.append(new_order)

    elif choice == "2":
        save_orders_to_file(pizza_order_list)
        print("Orders saved to file.")

    elif choice == "3":
        orders = load_orders_from_file()
        print("Existing Orders:")
        
        for categorize, order in enumerate(orders, start=1): # 
            print(F"{categorize}. {order.customer_name} ordered {order.pizza_type} with toppings {', '.join(order.toppings)}\n")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    
    print(display_menu())
    print(type(orders))
