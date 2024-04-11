# Imports
import csv, datetime, pytz
from argparse import *
from functions import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
print('\n')

current_date = datetime.datetime.now().strftime("%d-%m-%Y")
print(current_date)

# current_datetime = datetime.datetime.now(tz= pytz.timezone('Europe/Amsterdam'))   # Deze code doet het ook, maar volgens mentor Christiaan hoef je alleen de date class te gebruiken bij de Superpy opdracht. Ik wil de Nederlandse volgorde
# print(current_datetime)                                                           # gebruiken bij deze code: dd-mm-yyyy, maar het is (nog) niet bekend of dit mogelijk is.


print('\n')



        # p_file.seek(0)

        # p_file.close()
    
    # with open('purchase_file.csv', 'r+') as p_file: # Deze code doet het per vrijdag 15-12-2023. Deze code leest alleen het bestand zoals ie is.
    #     reader = csv.reader(p_file)

    #     for p_file in reader:
    #         print(p_file)

    
    # with open('purchase_file.csv', 'r+') as p_file: # Deze code doet het ook per vrijdag 15-12-2023. Deze code: leest het bestand én plaatst de data in dictionaries.
    #     reader = csv.DictReader(p_file)

    #     for line in reader:
    #         print(line)
            
#     # with open('purchase_file.csv', 'r+') as p_file: # Deze code doet het ook per vrijdag 15-12-2023. Deze code: leest het bestand, plaatst de data in dictionaries én plaatst de dictionaries in een lijst.
#     #     reader = csv.DictReader(p_file)
#     #     rows = list(reader)
#     #     # rows = (reader)
#     #     print(rows)
#     #     print(len(reader.fieldnames[1]))
#     #     print("\n")
#     #     print("Lengte aantal rows van de 'p_file' variabel:")
#     #     # print(len(rows)) # Deze code laat het aantal regels zien.
        
#     #     # for column in rows:
#     #     #     product = column['product_name'], column['product_purchase_amount']

#     #     for categorize, column in enumerate(rows, start=1):
#     #         product = column['product_name'], column['product_purchase_amount']
            
#     #         print(F"{categorize} {product}")
        

#         # Onderstaande codes doen het, maar laten niet het aantal producten zien.
#         # total_products = []
        
#         # for product in rows:
#         #     total_products.append(product)

#         # # print(F"Totaal aantal producten = {total_products}\n") # Deze code print 
#         # print(F"Totaal aantal producten = {total_products[0]}\n")



# with open("sales_file.csv", 'w', newline='') as sales_file:
#     write = csv.DictWriter(sales_file, fieldnames=['product_id', 'sale_id', 'sale_price', 'sale_date'])
#     write.writeheader()
#     print(write)
#     print(sales_file)


# def addition_sales_file():

#     added_products = [
#         ['12345', '54321', '3.99', '14-12-2023'],
#         ['6789', '9876', '1.49', '13-12-2023']
#     ]

#     s_file = open('sales_file.csv', 'a', newline='')
#     writer = csv.writer(s_file)
#     writer.writerows(added_products)

#     s_file.seek(0)
#     s_file.close()

#     return F"Return statement van de 'sales_file': {s_file}"



parser = ArgumentParser(description = "Hello, and welcome to SuperPy: your supermarket inventory management system. Have fun managing!")

subparsers = parser.add_subparsers(dest= "command")

# Search for products in files. LET OP!!! IK MOET NOG EVEN NADENKEN WELKE ARGUMENTEN IK POSITIONAL EN OPTINAL GA MAKEN.
file_search = subparsers.add_parser("search", help= "Search for products in your files: 'inventory_file.csv', 'sales_file.csv' and 'losses_file.csv'.") # Met de 'add_parser' code geef je met een 'argument' aan wat de 'command' code moet zijn (+ de helptekst). En in dit geval is de command code 'inventory'.
file_search.add_argument("--search_item", type=str, help= "Use the 'product name' or the 'product id' to search for a product.") # Met deze code geef je aan welk argument je wilt gebruiken om met de functies hieronder bij de 'args.command == "inventory' te werken.
file_search.add_argument("--file_name", type=str, help= "Enter the name of the file in which you want to search for a product.") # Met deze code geef je aan welk argument je wilt gebruiken om met de functies hieronder bij de 'args.command == "inventory' te werken.
file_search.add_argument("--column_name", type=str, help= "Enter the name of the file in which you want to search for a product.") # Met deze code geef je aan welk argument je wilt gebruiken om met de functies hieronder bij de 'args.command == "inventory' te werken.
# file_search.add_argument("search_item", type=str, help= "Use the 'product name' or the 'product id' to search for a product.") # Met deze code geef je aan welk argument je wilt gebruiken om met de functies hieronder bij de 'args.command == "inventory' te werken.
# file_search.add_argument("file_name", type=str, help= "Enter the name of the file in which you want to search for a product.") # Met deze code geef je aan welk argument je wilt gebruiken om met de functies hieronder bij de 'args.command == "inventory' te werken.


# Parse arguments
args = parser.parse_args() # De '.parse_args' code bevat alle argumenten die ik in de hierboven vermelde subparser argumenten heb geplaatst. En in dit geval zijn het de argumenten: 

if args.command == "search": # Met deze code geef je aan wat de 'command' code moet zijn die ik hierboven bij en de 'subparsers = parser.add_subparsers(dest= "command")' heb gedefinieerd. En in dit geval is het 'search'.
    
    if args.search_item == "product":           # # Met deze code geef je aan dat als het 'argument' '.search_item' gelijk is aan het argument 'product', onderstaande functie uitgevoerd moet worden. En in je terminal doe je dit met de\
        print(select_file_for_data(args.file_name)) # code: search_item product (= 'positional arguments'). LET OP!!! Als je de bovenstaande argumenten optioneel (= 'optional arguments') maakt met de 2 min tekens ervoor (b.v.\
        # print(select_file_for_data(args.file_name, args.column_name)) # code: search_item product (= 'positional arguments'). LET OP!!! Als je de bovenstaande argumenten optioneel (= 'optional arguments') maakt met de 2 min tekens ervoor (b.v.\
                                                    # '--search_item' of '--get_data'), dan vraag je dit als volgt op in je terminal: search --search_item product --file_name HIER VUL JE DAN DE NAAM OF DE VARIABEL VAN HET BESTAND VAN HET\
                                                # BESTAND WAARIN JE WIL ZOEKEN. Ik heb voor deze argparse code een functie inc. uitleg geschreven over hoe je een product kunt zoeken.
    
    if args.search_item == "id":
        outcome = find_product_id(args.enter_search_item)
        # print(outcome)
    
    # if args.clear_inventory == "clear": # DEZE CODE DOET HET!!!
    #     outcome = clear_purchase_file()
    
    # if args.add_test_products == "atp": # DEZE CODE DOET HET OOK!!!
    #     outcome = add_test_products()

    # if args.add_product == "add":
    #     outcome = add_product()


# purchase_parser.add_argument("clear_purchase_file", type= str, help= "Select this option to clear all products from the new purchase file.")


#     if args.manage_purchase_file == "create":
#         outcome = create_purchase_file()

#     if args.manage_purchase_file == "add":
#         outcome = add_test_products()
    
#     if args.manage_purchase_file == "clear":
#         outcome = clear_purchase_file()
    
#     if args.manage_purchase_file == "all":
#         outcome = show_all_products()




'''
Onderstaande code voor de mogelijkheid om producten toe te voegen doe ik wel wanneer ik alle andere oprachten heb afgerond.
'''

# def add_purchased_products(): # Deze functie doet het.

#     added_products = [
#         ['12345', 'Pindakaas', '3.99', '14-12-2023', '14-12-2024'],
#         ['6789', 'kaas', '1.49', '13-12-2023', '13-12-2024'],
#         ['6789', 'brood', '1.49', '12-12-2023', '12-12-2024']
#     ]

#     p_file = open('purchase_file.csv', 'a', newline='')
#     writer = csv.DictWriter(p_file, fieldnames= write.fieldnames)
#     writer.writerows(added_products)
#     print(p_file)


#     p_file.seek(0)

#     p_file.close()
    
#     return p_file



# def add_products(product_id, product_name, product_purchase_amount, product_purchase_date, product_expiration_date)-> dict: # Deze functie doet het nog niet.
    
#     with open("purchase_file.csv", 'r+', newline='') as p_file:
#         reader = csv.DictReader(p_file)
#         rows = list(reader)
#         print(write)

#         for row in rows:
#             if row["product_id"] == product_id and ["product_name"] == product_name:
#                 print("Het werkt")
#                 break

#         p_file.seek(0)

#         writer = csv.DictWriter(p_file, fieldnames= reader.fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)
#         print(p_file)


#         p_file.close()
    
#         return p_file

    
    # with open("purchase_file.csv", 'a', newline='') as p_file:
        
    #     product_id = input("Enter the product id: ")
    #     product_name = input("Enter the product name: ")
    #     product_purchase_amount = input("Enter the product purchase amount: ")
    #     product_purchase_date = input("Enter the product purchase date: ")
    #     product_expiration_date = input("Enter the product expiration date: ")
        
    #     row = (product_id, product_name, product_purchase_amount, product_purchase_date, product_expiration_date)
        
    #     writer = csv.writer(p_file)
    #     writer.writerows(row)
    #     print(p_file)

    #     p_file.seek(0)

    #     p_file.close()
    
    #     return p_file

'''
Onderstaande code werkt ook daadwerkelijk om data / gegevens / producten toe te voegen aan het 'purchase_file.csv' bestand.
Ik moet dus ff uitzoeken of ik dit middels een functie of gewoon ga doen.
'''

# added_products = [
#     ['12345', 'Pindakaas', '14-12-2023', '14-12-2024', '3.99'],
#     ['6789', 'Kaas', '13-12-2023', '13-12-2024', '1.49']
# ]

# p_file = open('purchase_file.csv', 'a', newline='')
# writer = csv.writer(p_file)
# writer.writerows(added_products)

# p_file.seek(0)
# p_file.close()

# if __name__ == "__main__":
#     print(outcome)