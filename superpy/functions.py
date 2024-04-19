
# Imports

import csv, datetime, pytz
import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd
from argparse import *
from datetime import timedelta

print('\n')

'''
De huidige datum returnen ZONDER menu en datums omzetten naar 'datetime objecten. DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
- Zaterdagnacht 06-04-2024 rond 00:55 uur ben ik met onderstaande functies bezig geweest. Dit omdat\
de input statements met datums in mijn functies geen vergelijking konden maken tussen een string en\
een datetime object (b.v. 'if input_date < current_date()'. Daarom heb ik de functie\
'convert_to_datetime_object()' toegevoegd zodat ik hiermee dit soort input statements wel kon\
omzetten naar een datetime object.

    - current_date() = aangepast;
    - convert_to_datetime_object() = toegevoegd;
    - convert_to_dutch_date() = niet aangepast.

Ik had deze code al eerder geschreven op zondagnacht 10-03-2024, maar dan met de 'datetime.date.today()' code
en dat veroorzaakte een foutmelding met mijn current date functie in andere functies. Dus heb ik deze code
op advies van een Winc mentor opnieuw geschreven met de 'datetime.datetime.today()' en toen kreeg ik geen
conflicten meer in m'n code.
'''

def current_date():

    return datetime.datetime.today()
    
# print(current_date())
# print("\n")


def convert_to_datetime_object(datetime_object):

    return datetime.datetime.strptime(datetime_object, "%d-%m-%Y")

# print(convert_to_dutch_date_test())
# print("\n")


def convert_to_dutch_date(date_format):

    return datetime.datetime.strptime(date_format, "%d-%m-%Y").strftime("%d-%m-%Y") # Met 'datetime module' maak je een 'datetime' object aan. Met 'strptime' (en 'strp' staat voor 'strippen' in de zin van dat je de tijd uit het object\
                                                                                    # stript / haalt) haal je dus de tijd uit de 'today' code.
# print(convert_to_dutch_date())
# print("\n")


'''
De huidige datum returnen MET menu. DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
Ik ben ook met deze functie begonnen op vrijdag 15-03-2024.
'''

def update_system_date():
    
    print("\n")
    
    print("Hello user, and welcome to the 'update system date' menu. With this option you can update the system date to the current date. Follow the steps below to update the system date.\n")

    print("Step 1 = Enter Y (for Yes) if you want to update the system date or enter N (for No) if you don't want to update the system date (not case sensitive).")
    print("Done!\n")
    
    while True:
        update_system = (input("Step 1 = Enter Y (for Yes) if you want to update the system date or enter N (for No) if you don't want to update the system date: ")).lower()
        print("\n")

        if update_system == "y":
            print("Great! The date of the system is updated to the current date. You can check the current date below.\n")

        elif update_system == "n":
            print("Noted! The date of the system will not be updated to the current date.\n")
        
        else:
            print(F"Hello user! '{update_system}' isn't the correct input for updating the system date. Please enter Y if you want to update the system date or N if you don't want to update te system date.\n") 
            
            continue
        break

    today_date = current_date()
    string_date = "15-03-2024" # This is de date this functions was written.

    if update_system == "y":
        string_date = datetime.datetime.strftime(today_date, "%d-%m-%Y")
        print(string_date)
        print("\n")

    with open("date_file.txt", 'w') as date_file:

        date_file.write(string_date)

# print(update_system_date())
# print("\n")


'''
Naar een specifieke datum gaan door deze ook zelf in te voeren. DEZE CODE DOET HET PER ZATERDAGNACHT 16-03-2024!!!
Ik ben ook met deze functie begonnen op zaterdagnacht 16-03-2024.
Ik wilde deze functie hebben naast de verplichte timedelta functie die ik van Winc moest schrijven omdat ik dit veel makkelijker vind,
zie mijn 'change_system_date()' functie waarin ik de timedelta code heb verwerkt.
'''

def go_to_specific_date():
    
    print("\n")
    
    print("Hello user, and welcome to the 'choose a specific system date' menu. With this option you can go to a specific date in the system. Follow the steps below to go to a specific date in the system.\n")

    print("Step 1 = Enter the date you want the system to go to.")
    print("Done!\n")
    
    while True:
        specific_date = (input("Enter the date you want the system to go to in the following format 'dd-mm-yyyy': "))
        print("\n")

        try:
            date_check = datetime.datetime.strptime(specific_date, "%d-%m-%Y")
            
        except ValueError:
            print(F"Hello user! '{specific_date}' isn't the correct format to fill in the specific date. Please enter the specific date in the following format: dd-mm-yyyy.\n")
            
            continue
        break


    with open("date_file.txt", 'w') as date_file:

        date_file.write(specific_date)
        print("Great! The date of the system has been changed to the specific date. You can check the specific date below.\n")

    return specific_date

# print(go_to_specific_date())
# print("\n")


'''
Systeem datum aanpassen. DEZE AANGEPASTE FUNCTIE DOET HET PER DONDERDAG 14-03-2024 ÉN IS OP VRIJDAG 15-03-2024 ALS 'PRIMA' BEVONDEN DOOR EEN WINC MENTOR.
Deze functie deed het al per zondagnacht 10-03-2024 ROND 02:57 UUR, maar ik heb de naam
(tijdrijzen functie / time travel) én de inhoud van deze functie aangepast op donderdag 14-03-2024
naar 'change_system_date' na een consult met een Winc mentor.
Met deze code kan je de systeem datum / de datum in het 'date_file.txt' bestand aanpassen naar welke
datum je maar wilt met een door jou opgegeven aantal 'dagen' of 'weken'.
'''

def change_system_date(): # Met deze functie moet je de datum van je systeem aanpassen door de datum in het 'date_file.txt' bestand aan te passen.

    print("\n")

    print("Hello user, and welcome to the 'change system date' menu.\n")
        
    print("Follow the steps below to change the system date by entering the number of days or weeks you want to change the system date with.\n")
    
    print("Step 1 = Enter 'days' if you want to change the system date in a period of days or enter 'weeks' if you want to change the system date in weeks (not case sensitive).")
    print("Step 2 = Enter 'past' if you want the system date to go to the past or enter 'future' if you want the system date to be in the future (not case sensitive).")
    print("Step 3 = Enter a 'number' for the couple of days or weeks that you want to change the system date with.")
    print("Done!.\n")

    date_periode_choice = ["days", "weeks"]
    date_travel_choice = ["past", "future"]

    while True:
        days_or_weeks = input("Step 1 = Enter 'days' if you want to change the system date in a period of days or enter 'weeks' if you want to change the system date in weeks (not case sensitive): ").lower()
        print("\n")

        if days_or_weeks in date_periode_choice:
            print(F"Great! Let's change the system date for a couple of '{days_or_weeks}'.\n")

        else:
            print(F"Hello user! '{days_or_weeks}' isn't the correct input to modify the system date. Please enter 'days' or 'weeks' for the correct system date modification.\n")

            continue
        break


    while True:
            past_or_future = input("Step 2 = Enter 'past' if you want the system date to go to the past or enter 'future' if you want the system date to be in the future (not case sensitive): ").lower()
            print("\n")

            if past_or_future in date_travel_choice:
                print(F"Great! Let's change the system date for a couple of '{days_or_weeks}' in the '{past_or_future}'.\n")

            else:
                print(F"Hello user! '{past_or_future}' isn't the correct input to modify the system date. Please enter 'future' or 'past' for the correct system date modification.\n")

                continue
            break


    while True:
        number = (input(f"Step 3 = Enter a 'number' for the couple of '{days_or_weeks}' that you want to change the system date with in the {past_or_future}: "))
        print("\n")

        try:
            int(number)
            
        except ValueError:
            print(F"Hello user! The number of '{days_or_weeks}' must only contain a 'number'. '{number}' doesn't only contain a number. Please enter a number to continue with the system date modification.\n")
            
            continue

        if int(number) > 105000 and days_or_weeks == "weeks".lower(): # Python geeft een foutmelding bij meer dan 105000 weken in het verleden.
            print(F"Hello user! The number you entered '{number}' is to far in the '{past_or_future}' Please enter a number below 105000.\n")

            continue

        elif int(number) > 738958 and days_or_weeks == "days": # Python geeft een foutmelding bij meer dan 738958 dagen in het verleden.
            print(F"Hello user! The number you entered '{number}' is to far in the '{past_or_future}' Please enter a number below 738958.\n")
            
            continue
        break


    timedelta_days = timedelta(days= int(number))
    timedelta_weeks = timedelta(weeks= int(number))
    
    today_date = current_date()

    # Modify system date by days.
    if days_or_weeks == "days" and past_or_future == "past":
        system_date = today_date - timedelta_days
        print("\n")
    
    elif days_or_weeks == "days" and past_or_future == "future":
        system_date = today_date + timedelta_days
        print("\n")
    

    # Modify system date by weeks.
    elif days_or_weeks == "weeks" and past_or_future == "past":
        system_date = today_date - timedelta_weeks
        print("\n")
    
    elif days_or_weeks == "weeks" and past_or_future == "future":
        system_date = today_date + timedelta_weeks
        print("\n")

    string_date = datetime.datetime.strftime(system_date, "%d-%m-%Y")

    with open("date_file.txt", 'w') as date_file:

        date_file.write(string_date)

    return F"If we go '{number}' '{days_or_weeks}' in the '{past_or_future}', the date = {string_date}" # LET OP!!! Ik wil ook nog de dag vóór de datum hebben (dus b.v. Monday of Tuesday etc.).

# print(change_system_date())
# print("\n")


'''
Speciale gelegenheden tekst bestand voor mijn 'special_occasion_countdown()' functie.
- Zondagnacht 17-03-2024 = Begonnen én afgrond rond 00:06 uur.
'''

with open('special_occasion.txt', 'w') as file:
    file.write(' ')


'''
Aftellen tot een bepaalde / speciale gelegenheidsdatum. DEZE CODE DOET HET!!! Per zaterdagnacht 30-03-2024 rond 01:12 uur.
- Vrijdag 29-01-2024 = Code aangepast samen met mentor Christiaan.
- Zaterdagnacht 30-03-2024 = Code aangepast én getest.
'''

def special_occasion_countdown():

    print("\n")

    print("Hello user, and welcome to the 'countdown to a special occasion' option.\n")
        
    print("Follow the steps below to create a countdown for a special occasion.\n")
    
    print("Step 1 = Step 1 = Enter the date of the special occasion in the following format: dd-mm-yyyy).")
    print("Step 2 = Type a sentence that you want to use for this special occasion date.")
    print("Done!.\n")


    while True:
        special_occasion_date = input("Step 1 = Enter the date of the special occasion in the following format: dd-mm-yyyy): ")
        
        try:
            convert_to_dutch_date(special_occasion_date)
            print("\n")
            print(F"Great! The special occasion date '{special_occasion_date}' has been filled in correctly.\n")
            
        except ValueError:
            print("\n")
            print(F"Hello user! '{special_occasion_date}' Isn't the correct format to fill in the special occasion date. Please enter the correct special occasion date in the following format: dd-mm-yyyy.\n")
            
            continue
        
        input_date = datetime.datetime.strptime(special_occasion_date, "%d-%m-%Y")  # Met deze code maak ik van mijn 'special_occasion_date' variabel een datetime object. Dit omdat het aan het begin van deze while loop nog niet opgeslagen\
        todays_date = datetime.datetime.today()                                     # is als een datetime object in / door Python. Dit kan je testen door de 'type' van mijn 'special_occasion_date' variabel hier te printen (zie de print\
                                                                                    # statement hieronder) en dan zie je dat het hier nog steeds een 'string' is. En door het met de variabel 'input_date' om te zetten naar een datetime\
                                                                                    # object, kan je het dus wel weer vergelijken met een andere datetime object en in dit geval is dat mijn 'today' variabel. Ik heb mijn 'current_date()'\
        if input_date < todays_date:                                                # functie geprobeerd te gebruiken, maar het lukt in deze functie dan toch niet om het te vergelijken met een datetime object omdat mijn 'current_date()'\
            print(type(input_date))                                               # functie een 'string' / 'strftime' is.
            print(F"Hello user! The date you just entered: '{special_occasion_date}', is a date in the past. And we're not able to time travel... yet. ;-). Please enter the correct special occasion date to continue the special occasion countdown: dd-mm-yyyy.\n")
            
            continue
        break


    special_occasion_sentence = input("Step 2 = Type a sentence that you want to add to the special occasion countdown (for instance: Until Christmas!!!): ")
    print("\n")
    
    with open('special_occasion.txt', 'w') as file:
    
        datetime_countdown = input_date - todays_date   # Dit zijn de variabelen die ik in de 'while loop' heb gebruikt en omdat ik van deze variabelen 'datetime objecten' heb gemaakt, kan ik hier ook met ze 'rekenen', als in de datums\
        print(datetime_countdown)                       # op- of aftrekken. En met deze print statement kan je zien hoe de uitkomst van mijn 'datetime_countdown' code er normaal gesproken uit ziet.

        string_countdown = str(datetime_countdown)      # Om beide variabelen te kunnen gebruiken als 'strings' heb ik ze hier 'gecast' naar een 'string'. En zo kan ik beide 'datetime objecten' ('input_date' en 'todays_date') als string\
                                                        # gebruiken.        
        length_string_countdown = string_countdown[0:string_countdown.find(",")]    # Met deze index geef ik aan waar mijn 'string_countdown' variabel begint (= 0) en waar mijn 'string_countdown' variabel eindigt (= bij de komma)\
                                                                                    # Dit omdat wanneer je 'datetime_countdown' variabel volledig (dus zonder te slicen / te indexen) uitprint (zie de print statement hierboven), zie je dat\
        file.write(F"{length_string_countdown.upper()} {special_occasion_sentence}")    # Python een komma plaatst tussen het aantal dagen en het tijdstip. Dus wanneer je wilt dat de komma en het tijdstip niet zichtbaar zijn wanneer je de\
                                                                                        # code uitprint, moet je 'slicen' door een index te gebruiken. En met deze code kwam ik erachter dat je dus ook kan slicen door een getal én een\
    return F"{length_string_countdown} {special_occasion_sentence}"                     # variabel in combinatie met de 'find()' code te gebruiken 'binnen een index'.

print(special_occasion_countdown())
print("\n")


'''
Inventory bestand maken. DEZE CODE DOET HET!!! Per donderdag 28-03-2024 rond 23:52 uur.
- Donderdag 28-03-2024 rond 23:52 uur = Code aangepast en getest.
'''

def create_inventory_file():
    
    with open("inventory.csv", 'w', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames=['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        # write = csv.DictWriter(inventory_file, delimiter= '\t', fieldnames=['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])    # LET OP!!! Als je een andere scheidingsteken dan de komma wil\
                                                                                                                                                                            # gebruiken, dan doe je dat # met de 'delimiter=''' code. De\
                                                                                                                                                                            # 'delimiter=''' code plaats je tussen de 'bestandsnaam' en de\
                                                                                                                                                                            # 'fieldnames' in.
        writer.writeheader()

# print(create_inventory_file())
# print("\n")


'''
Sales bestand maken. DEZE CODE DOET HET!!! Per vrijdagnacht rond 00:02 uur.
- Vrijdagnacht 29-03-2024 rond 00:02 uur = Code aangepast en getest.
'''

def create_sales_file():

    with open("sales.csv", 'w', newline='') as sales_file:
        writer = csv.DictWriter(sales_file, fieldnames=['id', 'name', 'sold_quantity', 'sold_amount', 'sold_date', 'expiration_date'])
        writer.writeheader()
        
# print(create_sales_file())
# print("\n")


'''
Losses bestand maken. DEZE CODE DOET HET!!! Per vrijdagnacht rond 00:11 uur.
- Vrijdagnacht 29-03-2024 rond 00:11 uur = Code aangepast en getest.
'''

def create_losses_file():

    with open("losses.csv", 'w', newline='') as losses_file:
        writer = csv.DictWriter(losses_file, fieldnames=['id', 'name', 'loss_quantity', 'loss_amount', 'loss_date', 'loss_cause', 'expiration_date'])
        writer.writeheader()
        
# print(create_losses_file())
# print("\n")


'''
Een door jou gekozen csv bestand converteren naar een Excel bestand. DEZE CODE DOET HET!!! Per maandag 19-02-2024.
- Dinsdagnacht 19-03-2024 rond 00:30 uur = Code aangepast.
- Vrijdagnacht 29-03-2024 rond 00:19 uur = Code aangepast en getest.
'''

def export_file_to_excel():

    print("Hello user, and welcome to the 'export file to Excel' option. With this option, you can export a choosen file to an Excel file. Have fun exporting!\n")

    print("Follow the steps below to to export a choosen file to an 'Excel' file.\n")
    
    print("Step 1 = Enter one of the following file names to export it to Excel: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Done!.\n")


    while True:
        file_name = input("Step 1 = Enter one of the following file names to export it to Excel: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        print("\n")

        if file_name == "inventory":
            file_name = "inventory.csv"
            print(F"Great! The '{file_name[:-4]}' file is found and it is exported to an Excel file.\n")

        elif file_name == "sales":
            file_name = "sales.csv"
            print(F"Great! The '{file_name[:-4]}' file is found and it is exported to an Excel file.\n")
            
        elif file_name == "losses":
            file_name = "losses.csv"
            print(F"Great! The '{file_name[:-4]}' file is found and it is exported to an Excel file.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")

            continue
        break


    if file_name == "inventory.csv":
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel("inventory.xlsx",
                        index_label= "Count",
                        freeze_panes= (1,1)
                        )
    
    if file_name == "sales.csv":
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel("sales.xlsx",
                        index_label= "Count",
                        freeze_panes= (1,1)
                        )
    
    if file_name == "losses.csv":
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel("losses.xlsx",
                        index_label= "Count",
                        freeze_panes= (1,1)
                        )

# print(export_file_to_excel())
# print("\n")


'''
DEZE CODE DOET HET PER MAANDAG 04-03-2024.
- Maandagnacht 01-04-2024 rond 00:51 uur = Functie getest na de start van mijn taak: kolom- en bestandsnamen aanpassen (door ze korter te maken). En hij doet het nog prima!!!

Met deze functie kan je specifieke data uit een kolom van een bestand pakken door onderstaande gegevens in te vullen.
Deze functie kan je dus ook gebruiken om op voorhand te checken of een 'product' of een 'product detail' (zoals b.v.
het product zelf of de houdbaarheidsdatum) wel of niet in een bestand voor komt. Dit doe je dus ook door onderstaande
gegevens in te vullen. Omdat ik DictReader gebruik, worden in deze functie alle 'keys' / kolomnamen en 'values' / kolom
inhoud geprint.

- 'file name' = naam van het bestand
- 'search type' = naam van het product
- 'column name' = naam van de kolom

De vorige versie van deze code deed het ook per dinsdag 13-02-2024, maar ik heb deze code opnieuw geschreven / aangepast
op vrijdag 01-03-2024 n.a.v. een consult met een Winc mentor op woensdag 28-02-2024, zodat ik deze functie ook voor
meerdere / andere functies kan gebruiken. Zie b.v. mijn 'modify_quantity' functie.
'''

def data_in_file_check(file_name: str, search_type: str, column_name: str):

    '''
    This function:
    - searches for data / product details of a chosen product in a chosen column in a chosen file and;
    - returns the found data / product details from the chosen column.
    '''

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        data_in_file = False

        column_name_results = []

        for row in rows:
            if row['name'] == search_type or row['id'] == search_type:
                
                data_in_file = True
                column_name_results.append(row[column_name])
                # LET OP!!! Je gebruikt in deze 'for loop' geen 'break' code omdat er dan maar 1 item wordt gereturnd met de 'return' statement. En als je de 'break' code weghaalt, wordt het laatste item / het item helemaal onderaan\
                # het bestand gereturnd. Dus wanneer je de gegevens die je zoekt met een 'for loop' wilt gebruiken (b.v. in een andere functie zoals ik met deze code heb gedaan in o.a. mijn 'modify_quantity' functie), dan kan je beter de\
                # gevonden gegevens eerst in een lijst plaatsen zoals ik hierboven heb gedaan met mijn variabel 'data_in_file = []'. Op deze manier kan je de gehele 'lijst' returnen én kan je de gegevens in de lijst weer gebruiken in\
                # andere functies.
        file.seek(0)

        if data_in_file == True:
            
            return column_name_results

# print(data_in_file_check("sales.csv", "pindakaas", "sold_amount"))
# print("\n")


'''
Checken (op voorhand) of een product 'wel' of 'niet' in een bestand voor komt (b.v. bij mijn input statements 'Enter the product 'name' or 'id'. DEZE CODE DOET HET PER WOENSDAG 28-02-2024.
- Vrijdag 19-04-2024 rond 16:14 uur = De variabel 'product_in_file_check' aangepast naar 'product_in_file' omdat het niet de bedoeling is dat je variabelen maakt die dezelfde naam hebben als de functie.
- Zaterdagnacht 13-04-2024 rond 00:42uur = functie aangepast door de print statement 'print("\n")' die 3 regels onder de 'with' statement stond te verwijderen. Dit omdat er een te grote\
  ruimte aan witregels ontstond in de for loop van mijn 'modify_qunatity()' functie.
- Maandagnacht 01-04-2024 rond 01:02 uur = Functie getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)' En hij doet het nog prima!!!
'''

def product_in_file_check(file_name: str, search_type: str):

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        product_in_file = False

        for row in rows:
            if row['name'] == search_type or row['id'] == search_type:
            
                product_in_file = True
                print(F"Product details for product '{search_type}' in the '{file_name[:-4]}' file:")
                print(row)
                print("\n")
                
        file.seek(0) # Even navragen of deze code nut heeft in deze functie én op deze plek.

        if product_in_file == True:
            return True
        
        elif product_in_file == False:
            return False

# print(product_in_file_check("sales.csv", "ei"))
# print("\n")


'''
Alle product details van een product in een gekozen bestand laten zien. DEZE CODE DOET HET PER VRIJDAG 19-04-2024 rond 17:38 uur.
'''

def show_product_details(file_name: str, search_type: str, expiration_date: str):

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        show_details = False

        product_details = []

        for row in rows:
            if (row['name'] == search_type or row['id'] == search_type) and row['expiration_date'] == expiration_date:
            
                show_details = True
                product_details.append(row)
                                
        file.seek(0) # Even navragen of deze code nut heeft in deze functie én op deze plek.

        if show_details == True:
            return product_details

# print(show_product_details('sales.csv', 'pindakaas', '01-03-2024'))
# print("\n")


'''
Algemene zoek-functie 'MET menu / input statements' voor het zoeken op 'product naam' en 'product id' in alle bestanden. DEZE CODE DOET HET PER MAANDAG 18-03-2024 ROND 19:45 UUR!!!
- Maandagavond 01-04-2024 rond 01:02 uur = Functie getest na de start van mijn taak: kolom- en bestandsnamen aanpassen (door ze korter te maken). En hij doet het nog prima!!!
- Vrijdagnacht 29-03-2024 rond 00:50 uur = Code aangepast en getest.
'''

def find_products():
    
    print("\n")
    
    print("Hello user and welcome to the 'find products' option. You can search for a product in one of the following files: 'inventory', 'sales' or 'losses'. Have fun searching!\n")

    print("Follow the steps below to search for a product.\n")
    
    print("Step 1 = Enter one of the following file names to search for a product: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Step 2 = Enter the product 'id' or 'name' (not case sensitive).")
    print("Done!.\n")

    while True:
        file_name = input("Step 1 = Enter one of the following file names to search for a product: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        print("\n")

        if file_name == "inventory":
            file_name = "inventory.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        elif file_name == "sales":
            file_name = "sales.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "losses":
            file_name = "losses.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")
            
            continue
        break
    

    while True:
        search_type = (input("Enter the product 'id' or 'name' (the product name is not case sensitive): ")).lower()
        
        if product_in_file_check(file_name, search_type) == True:
            print(F"Great! Product '{search_type}' is found in the '{file_name[:-4]}' file. You can check the product details above.\n")
        
        else:
            print(F"Hello user! Product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product 'name' or 'id' (the product name is not case sensitive).\n")
            
            continue
        break

# print(find_products())
# print("\n")


'''
Checken of een kolomnaam voor komt in een bestand. DEZE CODE DEED HET PER DONDERDAG 07-03-2024 rond 22:10 uur!!!
- Maandagavond 01-04-2024 rond 23:40 uur = Functie getest na de start van mijn taak: kolom- en bestandsnamen aanpassen (door ze korter te maken). En hij doet het nog prima!!!
- Vrijdag 08-03-2024 = Code aangepast na een tip van een Winc mentor door gebruik te maken van onderstaande code.
    - de 'reader' code i.p.v. de 'DictReader' code;
    - de 'next()' code i.p.v. een for loop, zie hieronder bij mijn notities een uitleg over het gebruik van de gewone 'reader' code en i.c.m. de 'next()' code.
'''

def column_name_check(file_name: str):

    with open(file_name, 'r') as file:
        reader = csv.reader(file)           # Wanneer je alleen de kolomnamen van een csv bestand wilt gebruiken voor een functie (zoals ik met deze functie heb gedaan voor mijn 'modify_product_details' functie, dan kan je beter alleen de\
                                            # 'reader' code gebruiken i.p.v. de 'DictReader' code. Het verschil is namelijk dat je dan geen 'keys' en 'values' hebt waardoor de 'reader' code direct itereerbaar is zoals b.v. in een gewone\
                                            # 'for loop'.
        check_column_name = next(reader)    # Met de 'next' code pak je altijd de 'gehele regel' / 'alle waardes die op de eerst iteratie' / 'regel' staan. Met andere woorden: alles wat in de eerst volgende iteratie staat. In deze code\
                                            # houdt dat dus in dat ik met de 'next' code in combinatie met de 'reader' code alle kolomnamen pak omdat die op de eerste regel van het bestand staan.
        print(F"These are the all the product detail names in the '{file_name[:-4]}' file:")
        print(check_column_name)
        print("\n")

    return check_column_name

# print(column_name_check("losses_file.csv"))


'''
Gehele 'inventory' bestand leeg maken. DEZE CODE DOET HET!!! Per dinsdag 02-04-2024 rond 15:48 uur.
- Dinsdag 02-04-2024 rond 15:48 uur = Ik heb de 3 losse 'clear_file()' functies samengevoegd in 1 functie. Ik heb de functie\
  getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- Dinsdag 19-03-2024 rond 15:49 uur = Ik heb deze functie aangepast en getest op 
'''

def clear_file():

    print("Hello user and welcome to the 'clear file' option. With this option you can clear a choosen file from all it's products. Have fun clearing!\n")

    print("Follow the steps below to clear a choosen file from all it's products.\n")
    
    print("Step 1 = Enter one of the following file names to clear all the products: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Step 2 = Decide if you 'do' or 'don't' want to clear the file of all it's products with Y or N.")
    print("Done!\n")
    
    while True:
        file_name = input("Step 1 = Enter one of the following file names to clear the file from all it's products: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            
        elif file_name == 'sales':
            file_name = 'sales.csv'
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            
        else:
            print("\n")
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")

            continue
        break


    print("\n")
    yes_or_no = input(F"Are you sure you want to clear the '{file_name[:-4]}' file from all it's products? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
        
    if yes_or_no == 'Y' or yes_or_no == 'y':
        print("\n")
        print(F"Great! The '{file_name[:-4]}' file has been cleared of all it's products.\n")
        print("\n")

        if file_name == 'inventory.csv':
            with open('inventory.csv', 'w', newline='') as inventory_file:
            
                writer = csv.DictWriter(inventory_file, fieldnames=['id', 'name', 'product quantity', 'product_purchase_amount', 'product_purchase_date', 'expiration_date'])
                writer.writeheader()

        elif file_name == 'sales.csv':
            with open('sales.csv', 'w', newline='') as sales_file:
            
                writer = csv.DictWriter(sales_file, fieldnames=['id', 'name', 'product_quantity', 'product_sales_amount', 'product_sales_date', 'expiration_date'])
                writer.writeheader()
        
        elif file_name == 'losses.csv':
            with open('losses.csv', 'w', newline='') as losses_file:
            
                writer = csv.DictWriter(losses_file, fieldnames=['id', 'name', 'loss_quantity', 'loss_amount', 'loss_date', 'loss_cause', 'expiration_date'])
                writer.writeheader()

    elif yes_or_no == 'N' or yes_or_no == 'n':
        print("\n")
        print(F"Oké. The '{file_name[:-4]}' file has not been cleared of all it's products.\n")
        print("\n")
        

# print(clear_file())
# print("\n")


'''
Alle producten van een zelf gekozen bestand / 1 van de 3 bestanden laten zien. DEZE CODE DOET HET!!! Per maandag 18-03-2024 rond 22:30 uur!!!
- Dinsdag 02-04-2024 rond 16:38 uur = Ik heb de functie aangepast en getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
'''

def view_all_products():

    print("\n")

    print("Hello user and welcome to the 'view all products' option. You can view all the products from one of the following files: 'inventory', 'sales' or 'losses'. Have fun viewing!\n")

    print("Follow the steps below to view all products from a choosen file.\n")
            
    print("Step 1 = Enter one of the following file names to view all the products: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Done!\n")


    while True:
        file_name = input("Step 1 = Enter one of the following file names to view all the products: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        print("\n")

        if file_name == "inventory":
            file_name = "inventory.csv"
            print(F"Great! The '{file_name[:-4]}' file is found. You can see all the products from the {file_name} below!\n")

        elif file_name == "sales":
            file_name = "sales.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "losses":
            file_name = "losses.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")

            continue
        break


    with open(file_name, 'r+') as inventory:
            reader = csv.reader(inventory) # Deze code plaatst elke regel van het csv bestand in een lijst.
            
            print(next(reader))

            for categorize, row in enumerate(reader, start=1):
                print(F"{categorize}. {row}\n") # LET OP!!! De punt na de variabel 'categorize' zorgt ervoor dat er na de nummering van de 'enumerate' code een punt komt te staan.
                
# print(view_all_products())
# print("\n")


'''
Product toevoegen of de producthoeveelheid aanpassen in inventory bestand indien product 'id',
'naam' en 'houdbaarheidsdatum' overeenkomen. DEZE CODE DOET HET PER WOENSDAG 24-01-2024!!!

- Dinsdagavond 02-04-2024 rond 20:22 uur = Functie getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- Donderdag 21-03-2024 rond 22:56 uur = Functie aangepast.
- Vrijdag 22-03-2024 rond 19:45 uur = Functie wederom getest.

LET OP!!! Ik heb per vrijdag 22-03-2024 besloten om de kolomnamen aanpassen, dus daarna moet ik\
deze én alle andere functies nog een keer testen :-(.
'''

def add_inventory_products():
    
    print("\n")
    
    print("Hello user, and welcome to the 'add inventory products' option. Follow the steps below to add products to your inventory file. Have fun adding!\n")

    print("Step 1 = Enter the product ID.")
    print("Step 2 = Enter the product name.")
    print("Step 3 = Enter the product purchase quantity.")
    print("Step 4 = Enter the product purchase amount and use a dot in stead of a comma to seperate any decimals.")
    print("Step 5 = Enter the product purchase date as follows: dd-mm-yyyy.")
    print("Step 6 = Enter the product expiration date as follows: dd-mm-yyyy.\n")


    today_date_string = datetime.datetime.today().strftime("%d-%m-%Y")

    today_date_datetime = datetime.datetime.strptime(today_date_string, "%d-%m-%Y")
    
    calculate_date = today_date_datetime + timedelta(1)
    
    tomorrow_date = datetime.datetime.strftime(calculate_date, "%d-%m-%Y")


    while True:
        id = (input("Step 1 = Enter the product ID: "))
        
        try:
            int(id)
            
        except ValueError:
            print("\n")
            print(F"Hello user! The product ID can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product id that only contains numbers.\n")
            
            continue 
        break        


    name = input(F"Step 2 = Enter the product name for product ID {id} (not case sensitive): ").lower()


    while True:
        quantity = input(F"Step 3 = Enter the purchase quantity for product '{name}': ")
        
        try:
            int(quantity)

        except ValueError:
            print("\n")
            print(F"Hello user! The purchase quantity for product '{name}' can only contain numbers. '{quantity}' Doesn't only contain numbers. Please enter the correct quantity for product '{name}'.\n")
            
            continue
        break      


    while True:
        purchase_amount = input(F"Step 4 = Enter the purchase amount for product '{name}': ")
        
        try:
            float(purchase_amount)

        except ValueError:
            print("\n")
            print(F"Hello user! '{purchase_amount}' Doesn't contain an amount or a dot to seperate the decimals. Please enter the correct purchase amount for product '{name}' and use a dot in stead of a comma to seperate any decimals.\n")

            continue
        break


    while True:
        purchase_date = input(F"Step 5 = Enter the purchase date for product '{name}' as follows: dd-mm-yyyy: ")
        
        try:
            input_date = convert_to_dutch_date(purchase_date)

        except ValueError:
            print("\n")
            print(F"Hello user! '{purchase_date}' Isn't the correct format for the purchase date. Please enter the correct purchase date for product '{name}' in the following format: dd-mm-yyyy.\n")
            
            continue
        
        if input_date > current_date():
            print("\n")
            print(F"Hello user! The date you just entered: '{purchase_date}', is a date in the future. And we're not able to time travel... yet. ;-). Please enter the correct date for product '{name}'.\n")

            continue
        break


    while True:
        expiration_date = input(F"Step 6 = Enter the expiration date for product '{name}' as follows: dd-mm-yyyy: ")
        
        try:
            input_date = convert_to_dutch_date(expiration_date)
        
        except ValueError:
            print("\n")
            print(F"Hello user! '{expiration_date}' Isn't the correct format for the expiration date. Please enter the correct expiration date for product '{name}' in the following format: dd-mm-yyyy.\n")
            
            continue

        if input_date == current_date():
            print("\n")
            print(F"Hello user! The expiration date of product '{name}' is today. So you can either: 1: enter the correct expiration date, 2: put it on sale, 3: think of a durable way not to waste it.\n")

            continue
        
        elif input_date == tomorrow_date:
            print("\n")
            print(F"Hello user! The expiration date of product '{name}' is tomorrow. So you can either: 1: enter the correct expiration date, 2: put product '{name}' on sale, or 3: think of a durable way not to waste product '{name}'.\n")

            continue

        elif input_date < current_date():
            print("\n")
            print(F"Hello user! Product '{name}' is rotton. So please throw it away a.s.a.p. or enter the correct expiration date for product '{name}'.\n")

            continue
        break


    product_details = {
        'id': id,
        'name' : name,
        'purchase_quantity' : quantity,
        'purchase_amount': purchase_amount,
        'purchase_date' : purchase_date,
        'expiration_date' : expiration_date,
        }

    with open('inventory.csv', 'r', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows:
            if row['id'] == id and row['name'] == name and row['purchase_amount'] and row['purchase_date'] and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) + int(quantity)
                
                already_exists = True
                break

            else:
                already_exists = False

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        
        if already_exists == True:
            writer.writerows(rows)  # Deze code doet het. Writerow verwacht een dictionary en kijkt naar de key (op de achtergrond). Writerows doet eigenlijk hetzelfde, maar die kijkt naar de\
                                    # iterabele.
            print("\n")                        
            print(F"Great! The quantity of product '{name}' has been updated, because the 'id', the 'name', the 'purchase amount', 'the purchase date' and the 'expiration date' are the same. You can check the product details below.\n")
            print(row)

        else:
            with open('inventory.csv', 'a+', newline='') as inventory_file:
                writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)

                print("\n")
                print(F"Great! Product '{name}' has been added to the 'inventory' file. You can check the product details below.\n")
                print(product_details)
                print("\n")

# print(add_inventory_products())
# print("\n")


'''
Sold products. DEZE CODE DOET HET!!! Ik heb deze functie aangepast en getest op zaterdagnacht 23-03-2024 rond 01:05 uur.
- Zaterdagnacht 06-04-2024 rond 01:53 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
'''

def add_sold_products():

    print("\n")
    
    print("Hello user, and welcome to the 'add sold products' option.\n")
    
    print("By adding a sold product, your inventory file will automatically be reduced with the same quantity of the product that you've sold.\n")
    
    print("Follow the steps below to add your sold products. Have fun adding!\n")
    
    print("Step 1 = Enter the product ID.")
    print("Step 2 = Enter the product name.")
    print("Step 3 = Enter the quantity of the sold product.")
    print("Step 4 = Enter the product sales amount and use a dot in stead of a comma to seperate any decimals.")
    print("Step 5 = Enter the product sales date as follows: dd-mm-yyyy.")
    print("Step 6 = Enter the product expiration date as follows: dd-mm-yyyy.\n")


    while True:
        id = (input("Step 1 = Enter the product ID: "))

        try:
            int(id)
            
        except ValueError:
            print("\n")
            print(F"Hello user! The product ID can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product ID that only contains numbers.\n")
            
            continue 

        if product_in_file_check("inventory.csv", id) == True:
            print(F"Great! Product ID '{id}' is found in the inventory file. You can see the product details above.\n")
        
        else:
            print("\n")
            print(F"Hello user! Product ID '{id}' was not found in the inventory file. Please enter the correct product ID.\n")

            continue
        break 


    while True:
        name = (input("Step 2 = Enter the product name: ")).lower()
        
        if data_in_file_check("inventory.csv", name, "name"):
            product_in_file_check("inventory.csv", name)
            print(F"Great! Product name '{name}' with product id '{id}' is found in the inventory file. You can see the product details above.\n")
        
        else:
            product_in_file_check("inventory.csv", id)
            print(F"Hello user! '{name}' is not a product 'name' in the inventory file. Please check the product details above for the correct product name (not case sensitive).\n")

            continue
        break


    while True:
        sold_quantity = (input(F"Step 3 = Enter the sold quantity of product '{name}': "))

        try:
            int(sold_quantity)

        except ValueError:
            print("\n")
            print(F"Hello user! The sold quantity can only contain numbers. '{sold_quantity}' Doesn't only contain numbers. Please enter the correct sold quantity for product '{name}'.\n")
            
            continue
        break  


    while True:
        sales_amount = (input(F"Step 4 = Enter the sales amount of product '{name}' and use a dot in stead of a comma to seperate any decimals: "))

        try:
            float(sales_amount)

        except ValueError:
            print("\n")
            print(F"Hello user! '{sales_amount}' Doesn't contain an amount or a dot to seperate the decimals. Please enter the correct sales amount for product '{name}' and use a dot in stead of a comma to seperate any decimals.\n")

            continue
        break


    while True:
        sales_date = (input(F"Step 5 = Enter the sales date of product '{name}' as follows: dd-mm-yyyy: "))

        try:
            convert_to_dutch_date(sales_date)
        
        except ValueError:
            print("\n")
            print(F"Hello user! '{sales_date}' Isn't the correct format for the sales date. Please enter the correct sales date for product '{name}' in the following format: dd-mm-yyyy.\n")
            
            continue
        
        input_date = convert_to_datetime_object(sales_date)  # Met deze code maak ik van mijn 'special_occasion_date' variabel een datetime object. Dit omdat het aan het begin van deze while loop nog niet opgeslagen\
        
        if input_date > current_date():
            print("\n")
            print(F"Hello user! The date you just entered: '{sales_date}', is a date in the future. And we're not able to time travel... yet. ;-). Please enter the correct sales date for product '{name}'.\n")

            continue
        break


    while True:
        expiration_date = (input("Step 6 = Enter the product expiration date as follows: dd-mm-yyyy: "))

        try:
            input_date = convert_to_datetime_object(expiration_date)
            
        except ValueError:
            print("\n")
            print(F"Hello user! '{expiration_date}' Isn't the correct format for the expiration date. Please enter the correct expiration date for product '{name}' in the following format: dd-mm-yyyy.\n")
            
            continue
        
        expiration_date_check = data_in_file_check("inventory.csv", name, "expiration_date")

        if expiration_date in expiration_date_check:
            print("\n")
            product_in_file_check("inventory.csv", name)
            print(F"Great! The entered expiration date '{expiration_date}' of product '{name}' matches one of the expiration dates in the inventory file. You can check the expiration date in the product details shown above.\n")

            if input_date == current_date():
                    print("\n")
                    print(F"Hello user! The expiration date of the sold product '{name}' was today.\n")

            if input_date < current_date():
                    print("\n")
                    print(F"Hello user! The expiration date of the sold product '{name}' has expired.\n")

        else:
            print("\n")
            product_in_file_check("inventory.csv", name)
            print(F"Hello user! The entered expiration date '{expiration_date}' doesn't match one or more of the expiration dates of product '{name}' in the inventory file. Please check the product details above for the correct\
 expiration date.\n")

            continue
        break


    product_details = {
        'id' : id,
        'name' : name,
        'sold_quantity' : sold_quantity,
        'sales_amount' : sales_amount,
        'sales_date' : sales_date,
        'expiration_date' : expiration_date
    }

    with open('sales.csv', 'r', newline='') as sales_file:
        reader = csv.DictReader(sales_file, fieldnames= ['id', 'name', 'sold_quantity', 'sales_amount', 'sales_date', 'expiration_date'])
        rows = list(reader)

        for row in rows:
            if row['id'] ==  id and row['name'] == name and row['sales_amount'] == sales_amount and row['sales_date'] == sales_date and row['expiration_date'] == expiration_date:
                row['sold_quantity'] = int(row['sold_quantity']) + int(sold_quantity)
                
                already_exists = True
                break

            else:
                already_exists = False

    with open("sales.csv", 'r+', newline='') as sales_file:
        writer = csv.DictWriter(sales_file, fieldnames= reader.fieldnames)
        
        if already_exists == True:
            writer.writerows(rows)
            print("\n")
            print(F"Great! The quantity of product '{name}' has been updated, because: the 'id', the 'name', the 'sales amount' the 'sales date' and the 'expiration date' are the same. You can check the details below.\n")
            print(row)
            
        else:    
            with open("sales.csv", 'a+', newline='') as sales_file:
                writer = csv.DictWriter(sales_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)
                print("\n")
                print(F"Great! Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the sales file. You can check the details below.\n")
                print(product_details)


    with open('inventory.csv', 'r+', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows[1:]: # De index code '[1:]' zorgt ervoor dat de for loop gaat loopen vanaf 'de eerste regel' waar data in staat en dus niet vanaf de 'header' / de 'kolomnamen'. 
            
            if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) - int(sold_quantity)  # Omdat ik op deze regel de dictonary ['purchase_quantity'] al heb gecast naar een 'integer' / 'int' binnen de for loop, hoef ik dat in\
                                                                                                # onderstaande 'if' statements niet meer te doen omdat Python dit onthoudt.
                
                if row['purchase_quantity'] >= 4 and row['purchase_quantity'] < 6:
                    print("\n")
                    print(F"STOCK UPDATE!!! The product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there are / is '{row['purchase_quantity']}' left in\
 stock.\n")

                elif row['purchase_quantity'] <= 0:
                        row['purchase_quantity'] = 0
                        print("\n")
                        print(F"STOCK UPDATE!!! Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there is '{row['purchase_quantity']}' / 'nothing'\
 left in stock. Maybe your customers love this product so much, that you should start thinking about a big sale for this product. ;-)\n")
        
        # print(type(row['purchase_quantity']))  # LET OP!!! Bij bovenstaande 'if' statement kreeg ik eerst 2 foutmeldingen: 1= TypeError: '<=' not supported between instances of 'str' and 'int'. 2= ValueError: invalid literal for int() with\
                                                # base 10: 'purchase_quantity'. Deze foutmeldingen werden o.a. veroorzaakt doordat ik de code '(row['purchase_quantity']))' had gecast in een integer terwijl dit al een integer was. Door het\
                                                # gebruik van dit soort print statements (dus door de 'type' ervoor te zetten) kan je als programmeur ook achterhalen wat de mogelijke oorzaak is van een foutmelding én hoe je dit vervolgens\
                                                # kunt oplossen. De output van deze print statement was namelijk '<class 'int'>', waardoor je dus weet dat het casten naar een integer niet nodig is omdat de key van de dictionary al een\
                                                # integer is. Zie voor meer uitleg over deze code mijn Excel doc.: Foutmeldingen inc. oplossingen.
                else:
                    print("\n")
                    print(F"STOCK UPDATE!!! Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' doesn't need to be reordered, because there are '{(row['purchase_quantity'])}' left in\
 stock.\n")           
                break

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        writer.writerows(rows)
        
# print(add_sold_products())
# print("\n")


'''
DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
- Maandagavond 02-04-2024 rond 23:17 uur = Functie getest én aangepast na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!

Losses / verlies producten toevoegen of de producthoeveelheid aanpassen in het losses bestand én het inventory\
bestand indien product 'id', 'naam', 'houbaarheidsdatum', 'verlies datum', 'oorzaak verlies', 'verlies bedrag'\
overeenkomen. LET OP!!! Ik heb deze functie aangepast én weer getest op maandagnacht 25-03-2024 rond 00:44 uur.
'''

def add_loss_products():

    print("\n")
    
    print("Hello user, and welcome to the 'add product losses' option.\n")

    print("By adding a product loss, your inventory file will automatically be reduced with the same quantity of the added product loss.\n")

    print("Follow the steps below to add a product loss.\n")
    
    print("Step 1 = Enter the product ID.")
    print("Step 2 = Enter the product name (not case sensitive).")
    print("Step 3 = Enter the loss quantity.")
    print("Step 4 = Enter the loss amount.")
    print("Step 5 = Enter one of the following causes of loss: broken, damaged, expired, missing, theft, other (not case sensitive).")
    print("Step 6 = Enter the product expiration date as follows: dd-mm-yyyy.\n")

    while True:
        id = (input("Step 1 = Enter the product ID: "))
        
        try:
            int(id)
            
        except ValueError:
            print("\n")
            print(F"Hello user! The product ID can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product id that only contains numbers.\n")
            
            continue

        if product_in_file_check("inventory.csv", id) == True:
            print(F"Great! Product ID '{id}' is found in the inventory file. You can see the product details above.\n")
        
        else:
            print(F"Hello user! Product ID '{id}' was not found in the inventory file. Please enter the correct product id.\n")

            continue
        break 
    

    while True:
        name = (input("Step 2 = Enter the product name: ")).lower()
        
        if data_in_file_check("inventory.csv", name, "name"):
            product_in_file_check("inventory.csv", name)
            print(F"Great! Product name '{name}' with product id '{id}' is found in the inventory file. You can see the product details above.\n")
        
        else:
            product_in_file_check("inventory.csv", id)
            print(F"Hello user! '{name.capitalize()}' is not a product 'name' in the inventory file. Please check the product details above for the correct product name (not case sensitive).\n")

            continue
        break


    while True:
        loss_quantity = (input(F"Step 3 = Enter the loss quantity of product '{name}': "))
        
        try:
            int(loss_quantity)

        except ValueError:
            print("\n")
            print(F"Hello user! The loss quantity can only contain numbers. '{loss_quantity}' Doesn't only contain numbers. Please enter the correct loss quantity for product '{name}'.\n")
            
            continue
        break  


    while True:
        loss_amount = (input(F"Step 4 = Enter the loss amount of product '{name}': "))
        
        try:
            float(loss_amount)

        except ValueError:
            print("\n")
            print(F"Hello user! The loss amount for product '{name}' can only contain an amount and a dot to seperate any decimals. '{loss_amount}' Doesn't only contain an amount or a dot. Please enter the correct loss amount for product\
 '{name}' and use a dot in stead of a comma to seperate any decimals.\n")

            continue
        break
    

    while True:
        loss_date = (input(F"Step 5 = Enter the loss date of product '{name}': "))
        
        try:
            convert_to_dutch_date(loss_date) # LET OP!!! Omdat ik hier 'nog' geen vergelijking ga maken, hoef ik de datum nog niet om te zetten naar een datetime object.

        except ValueError:
            print("\n")
            print(F"Hello user. '{loss_date}' Isn't the correct format to fill in the loss date. Please enter the correct loss date for product '{name}' in the following format: dd-mm-yyyy.\n")
            
            continue

        input_date = convert_to_datetime_object(loss_date) # LET OP!!! Hier ga ik wel een vergelijking maken en daarom zet ik de datum hier wel om naar een datetime object.

        if input_date > current_date():
            print("\n")
            print(F"Hello user. The date you just entered: '{loss_date}', is a date in the future. And we're not able to time travel... yet. ;-). Please enter the correct loss date for product '{name}'.\n")
        
            continue
        break


    while True:
        loss_cause = (input(F"Step 6 = Enter one of the following causes of loss for product '{name}': broken, damaged, expired, missing, theft or other (not case sensitive): ")).lower()
        
        loss_options = ['broken', 'damaged', 'expired', 'missing', 'theft', 'other']

        if loss_cause in loss_options:
            print("\n")
            print(F"Great! '{loss_cause.capitalize()}', is a correct cause of loss.\n")

        else:
            print("\n")
            print(F"Hello user. The cause of loss you just entered: '{loss_cause}', isn't a correct cause of loss for product '{name}'. Please enter one of the following causes of loss: broken, damaged, expired, missing, theft or other (not case sensitive).\n")

            continue
        break


    while True:
        expiration_date = (input(F"Step 7 = Enter the expiration date for product '{name}': "))
        
        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print("\n")
            print(F"Hello user! '{expiration_date}' Isn't the correct format to fill in the expiration date for product '{name}'. Please enter the correct expiration date for product '{name}' in the following format: dd-mm-yyyy.\n")
        
            continue
        
        expiration_date_check = data_in_file_check("inventory.csv", name, "expiration_date")   # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven\
                                                                                                            # ingevulde variabel: 'search_type' dat het door de gebruiker ingevulde product is.
        
        if expiration_date in expiration_date_check:    # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn 'input' statement 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'data_in_file_check' functie\
                                                        # dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te gebruiken\
                                                        # i.p.v. de '==' operator, want met de 'in' operator kijk je of er iets 'wel' of 'niet' in een lijst zit.
            print("\n")
            (product_in_file_check("inventory.csv", name))
            print(F"Great! The entered expiration date '{expiration_date}' of product '{name}' matches one of the expiration dates in the inventory file. You can check the expiration date in the product details shown above.\n")
            
        else:
            print("\n")
            (product_in_file_check("inventory.csv", name))
            print(F"Hello user! The entered expiration date '{expiration_date}' doesn't match one or more of the expiration dates of product '{name}' in the inventory file. Please check the product details above for the correct\
 expiration date.\n")

            continue
        break


    product_details = {
        'id' : id,
        'name' : name,
        'loss_quantity' : loss_quantity,
        'loss_amount' : loss_amount,
        'loss_date' : loss_date,
        'loss_cause' : loss_cause,
        'expiration_date' : expiration_date
    }

    with open("losses.csv", 'r+', newline='') as losses_file:
        reader = csv.DictReader(losses_file, fieldnames= ['id', 'name', 'loss_quantity', 'loss_amount', 'loss_date', 'loss_cause', 'expiration_date'])
        rows = list(reader)

        for row in rows:
            if row['id'] == id and row['name'] == name and row['loss_amount'] == loss_amount and row['loss_date'] == loss_date and row['loss_cause'] == loss_cause and row['expiration_date'] == expiration_date:
                row['loss_quantity'] = int(row['loss_quantity']) + int(loss_quantity)
                
                already_exists = True
                break

            else:
                already_exists = False
    
    with open('losses.csv', 'r+', newline='') as losses_file:
        writer = csv.DictWriter(losses_file, fieldnames= reader.fieldnames)
        
        if already_exists == True:
            writer.writerows(rows)  # Deze code doet het. Writerow verwacht een dictionary en kijkt naar de key (op de achtergrond). Writerows doet eigenlijk hetzelfde, maar die kijkt naar de\
                                    # iterabele.
        
            print(F"Great! The loss quantity of product '{name}' has been updated, because the 'id', the 'name', the 'loss amount', the 'loss date', the 'cause of loss' and the 'expiration date' are the same. You can check the details below.\n")
            print(row)
            print("\n")

        else:
            with open('losses.csv', 'a+', newline='') as losses_file:
                writer = csv.DictWriter(losses_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)

                print(F"Great! Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the losses file. You can check the details below.\n")
                print(product_details)
                print("\n")

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows[1:]: # De index code '[1:]' zorgt ervoor dat de 'for loop' gaat loopen vanaf 'de eerste regel' waar data in staat en dus niet vanaf de 'header' / de 'kolomnamen'. 
            
            if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) - int(loss_quantity)
                
                if row['purchase_quantity'] >= 4 and row['purchase_quantity'] < 6: # If the quantity of a product is 5 or less, it will trigger the print statement shown below.
                    print(F"STOCK UPDATE!!! The product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there are / is '{row['purchase_quantity']}' left in\
 stock.\n")

                elif row['purchase_quantity'] <= 0: # Met deze code / 'elif statement' geef je aan dat als een berekening onder de nul / 0 uit komt, de berekening nul / 0 moet blijven.
                        row['purchase_quantity'] = 0
                        print(F"STOCK UPDATE!!! Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there is '{row['purchase_quantity']}' / 'nothing'\
 left in stock. Maybe your customers love this product so much, that you should start thinking about a big sale for this product. ;-)\n")
        
        # print(type(row['purchase_quantity']))  # LET OP!!! Bij bovenstaande 'if' statement kreeg ik eerst 2 foutmeldingen: 1= TypeError: '<=' not supported between instances of 'str' and 'int'. 2= ValueError: invalid literal for int() with\
                                                # base 10: 'purchase_quantity'. Deze foutmeldingen werden o.a. veroorzaakt doordat ik de code '(row['purchase_quantity']))' had gecast in een integer terwijl dit al een integer was. Door het\
                                                # gebruik van dit soort print statements (dus door de 'type' ervoor te zetten) kan je als programmeur ook achterhalen wat de mogelijke oorzaak is van een foutmelding én hoe je dit vervolgens\
                                                # kunt oplossen. De output van deze print statement was namelijk '<class 'int'>', waardoor je dus weet dat het casten naar een integer niet nodig is omdat de key van de dictionary al een\
                                                # integer is. Zie voor meer uitleg over deze code mijn Excel doc.: Foutmeldingen inc. oplossingen.
                else:
                    print(F"STOCK UPDATE!!! Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' doesn't need to be reordered, because there are '{(row['purchase_quantity'])}' left in\
 stock.\n")           
                break

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        writer.writerows(rows)

# print(add_loss_products())
# print("\n")


'''
Modify quantity. Met deze code pas je alleen de hoeveelheid van een bepaald product aan in een door jou gekozen bestand,
zonder de voorraad van het inventory bestand aan te passen. DEZE CODE DOET HET PER WOENSDAG 28-2-2024.

- Zondagavond 14-04-2024 rond 21:46 uur = Functie getest én aangepast na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- LET OP!!! Deze functie heeft dus geen effect op de voorraad / de hoeveelheden van het inventory bestand. Het gaat dus om een losse / individuele aanpassing van\
de hoeveelheid van een product.
- Zaterdagnacht 23-03-2024 rond 02:48 uur = Functie aangepast en getest.
'''

def modify_quantity():

    print("\n")
    
    print("Hello user, and welcome to the 'modify quantity' option.\n")

    print("Follow the steps below to modify the quantity of a product in a chosen file.\n")

    print("Step 1 = Enter one of the following files in which you want to modify the quantity: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Step 2 = Enter the product 'name' or 'id' (the product name is not case sensitive).")
    print("Step 3 = Enter the relevant amount and use a dot to seperate any decimals.")
    print("Step 4 = Enter the relevant date as follows: dd-mm-yyyy.")
    print("Step 5 = Enter the product expiration date as follows: dd-mm-yyyy.")
    print("Step 6 = Enter 'increase' or 'decrease' to modify the quantity (not case sensitive).")
    print("Step 7 = Enter the number you want to modify ('increase' or 'decrease') the quantity with.")
    print("Done!\n")


    while True:
        file_name = input("Step 1 = Enter one of the following files in which you want to modify the quantity: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        print("\n")

        if file_name == "inventory":
            file_name = "inventory.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        elif file_name == "sales":
            file_name = "sales.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "losses":
            file_name = "losses.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")
            
            continue
        break


    while True:
        search_type = input("Step 2 = Enter the product 'name' or 'id' (the product name is not case sensitive): ").lower()
        print("\n")

        if product_in_file_check(file_name, search_type) == True:
            print(F"Great! Product '{search_type}' is found in the '{file_name[:-4]}' file. You can see the product details above.\n")
        
        else:
            print(F"Hello user! Product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product 'name' or 'ID' (the product name is not case sensitive).\n")

            continue
        break


    # Names for the relevant 'amount' in the relevant file for 'Step 3' in the while loop below.
    relevant_amount = ""
    
    if file_name == "inventory.csv":
        relevant_amount = "purchase amount"

    elif file_name == "sales.csv":
        relevant_amount = "sales amount"
    
    elif file_name == "losses.csv":
        relevant_amount = "loss amount"


    while True:
        input_amount = input(F"Step 3 = Enter the {relevant_amount} for product '{search_type}' and use a dot to seperate any decimals. You can double check the {relevant_amount} for product '{search_type}' in the previous step above: ")
        print("\n")

        try:
            float(input_amount)

        except ValueError:
            print(F"Hello user! The {relevant_amount} can only contain an amount and a dot to seperate any decimals. '{input_amount}' Doesn't only contain an amount and / or a dot to seperate the decimals. Please enter the correct\
 {relevant_amount} for product '{search_type}' and use a dot to seperate any decimals.\n")
            
            continue
        
        # 3 Variables to check the relevant data / product in the relevant file and column in step 3, with my 'data_in_file_check()' function.
        purchase_amount_check = data_in_file_check("inventory.csv", search_type, "purchase_amount")
        sales_amount_check = data_in_file_check("sales.csv", search_type, "sales_amount")
        loss_amount_check = data_in_file_check("losses.csv", search_type, "loss_amount")

        if file_name == "inventory.csv" and input_amount in purchase_amount_check:      # Ik heb deze code aangepast omdat ik de volgende foutmelding kreeg (en deze foutmelding kreeg ik ook bij stap 4): 'TypeError: argument of type\
            product_in_file_check(file_name, search_type)                               # 'NoneType' is not iterable'. Dit kwam omdat ik eerst met een 'if' statement moest aangeven dat de variabel 'file_name' gelijk moest zijn aan het\
                                                                                        # betreffende bestand én omdat ik in mijn oude code mijn input statement 'relevant_amount' niet in mijn if statement had verwerkt. En nu dus wel.
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the {relevant_amount}'s in the '{file_name[:-4]}' file. You can see the {relevant_amount} in the product details shown\
 above.\n")
        
        elif file_name == "sales.csv" and input_amount in sales_amount_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the {relevant_amount}'s in the '{file_name[:-4]}' file. You can see the {relevant_amount} in the product details shown\
 above.\n")
        
        elif file_name == "losses.csv" and input_amount in loss_amount_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the {relevant_amount}'s in the '{file_name[:-4]}' file. You can see the {relevant_amount} in the product details shown\
 above.\n")

        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered {relevant_amount} '{input_amount}' doesn't match one or more of the {relevant_amount}'s of product '{search_type}' in the '{file_name[:-4]}' file. Please check the product details above for the\
 correct {relevant_amount}.\n")

            continue
        break


    # Names for the relevant 'date' in the relevant file for 'Step 4' in the while loop below.
    relevant_date = ""

    if file_name == "inventory.csv":
        relevant_date = "purchase date"
    
    elif file_name == "sales.csv":
        relevant_date = "sales date"
    
    elif file_name == "losses.csv":
        relevant_date = "loss date"


    while True:
        input_date = input(F"Step 4 = Enter the {relevant_date} for product '{search_type}' as follows: dd-mm-yyyy. You can double check the {relevant_date} in the previous step above: ")
        print("\n")

        try:
            convert_to_dutch_date(input_date)
            
        except ValueError:
            print(F"Hello user! The entered {relevant_date} '{input_date}' isn't the correct format to fill in the {relevant_date} for product '{search_type}'. Please enter the correct {relevant_date} for product '{search_type}' in the\
 following format: dd-mm-yyyy.\n")
        
            continue
        
        # 3 Variables to check the relevant data / product in the relevant file and column in step 4, with my 'data_in_file_check()' function.
        purchase_date_check = data_in_file_check("inventory.csv", search_type, "purchase_date")
        sales_date_check = data_in_file_check("sales.csv", search_type, "sales_date")
        loss_date_check = data_in_file_check("losses.csv", search_type, "loss_date")
        
        if file_name == "inventory.csv" and input_date in purchase_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date} '{input_date}' matches one of the {relevant_date}'s of product '{search_type}' in the '{file_name[:-4]}' file. You can see the {relevant_date} in the product details shown above.\n")

        elif file_name == "sales.csv" and input_date in sales_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date} '{input_date}' matches one of the {relevant_date}'s of product '{search_type}' in the '{file_name[:-4]}' file. You can see the {relevant_date} in the product details shown above.\n")
        
        elif file_name == "losses.csv" and input_date in loss_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date} '{input_date}' matches one of the {relevant_date}'s of product '{search_type}' in the '{file_name[:-4]}' file. You can see the {relevant_date} in the product details shown above.\n")

        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered {relevant_date} '{input_date}' doesn't match one of the {relevant_date}'s of product '{search_type}' in the '{file_name[:-4]}' file. Please check the product details above for the correct\
 {relevant_date}.\n")

            continue
        break


    while True:
        expiration_date = input(F"Step 5 = Enter the 'expiration date' of product '{search_type}' as follows: dd-mm-yyyy: ")
        print("\n")

        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print(F"Hello user! '{expiration_date}' Isn't the correct format to fill in the expiration date for product '{search_type}'. Please enter the expiration date in the following format: dd-mm-yyyy.\n")
            
            continue
        
        expiration_date_check = data_in_file_check(file_name, search_type, "expiration_date")
        
        if expiration_date in expiration_date_check:    
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered expiration date '{expiration_date}' of product '{search_type}' with {relevant_amount} '{input_amount}' in the '{file_name[:-4]}' file, matches one of the expiration dates shown above in the product\
 details.\n")
        
        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered expiration date '{expiration_date}' doesn't match one of the expiration dates of product '{search_type}' with {relevant_amount} '{input_amount}' in the '{file_name[:-4]}' file. Please\
 check the product details above for the correct expiration date.\n")

            continue
        break


    while True:
        modify_type = input(F"Step 6 = Enter 'increase' if you want to increase the quantity or 'decrease' if you want to decrease the quantity for product '{search_type}' (not case sensitive): ").lower()
        print("\n")

        if modify_type == "increase" or modify_type == "decrease":
            
            print(F"Great! It's noted that you want to '{modify_type}' the quantity for product '{search_type}' with {relevant_amount} '{input_amount}', {relevant_date} '{input_date}' and expiration date '{expiration_date}' in the\
 '{file_name[:-4]}' file.\n")

        else:
            print(F"Hello user! '{modify_type}' Isn't the correct input to modify the quantity of product '{search_type}'. Please enter 'increase' or 'decrease' for the correct quantity modification (not case sensitive).\n")
            
            continue
        break


    while True:
        quantity = input(F"Step 7 = Enter the number by which you want to {modify_type} the quantity of product '{search_type}': ")
        
        try:
            int(quantity)

        except ValueError:
            print("\n")
            print(F"Hello user! The quantity can only contain numbers. '{quantity}' Doesn't only contain numbers. Please enter the correct quantity to {modify_type} product '{search_type}'.\n")
            
            continue
        break      


    with open(file_name, 'r+', newline= '') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        # Variables to loop over the relevant columns in the for below.
        quantity_in_file = 'purchase_quantity'  # Een variabel gebruik je wanneer je iets in je code ook wil kunnen veranderen. Dus met de variabel 'quantity_in_file' zorg ik er in eerste instantie voor dat deze variabel altijd als\
                                                # 'product_quantity' is gedefinieerd in onderstaande 'for loop'. Maar omdat ik alleen in mijn 'sales' en 'inventory' bestand de productdetail 'product_quantity' heb en in mijn 'losses'\
                                                # bestand deze productdetail 'loss_quantity' heet, ga ik met onderstaande 'if statement' de variabel aanpassen zodat ik met onderstaande 'for loop' ook kan itereren in mijn 'losses' bestand.\
                                                # Ik heb deze code geschreven omdat ik problemen kreeg toen onderstaande for loop alleen itereerde over de productdetail 'product_quantity'. Mijn 'losses' bestand had namelijk geen\
                                                # productdetail genaamd 'product_quantity' en dat veroorzaakte een probleem.
        if file_name == 'sales.csv':            # Met deze 2 codes geef ik dus aan dat als het bestandsnaam het 'losses' bestand betreft, de variabel 'quantity_in_file' aangepast moet worden in de productdetail 'loss_quantity'. En op deze\
            quantity_in_file = 'sold_quantity'  # manier komt onderstaande for loop niet in de problemen.

        elif file_name == 'losses.csv':
            quantity_in_file = 'loss_quantity'


        amount_in_file = 'purchase_amount'

        if file_name == 'sales.csv':
            amount_in_file = 'sales_amount'

        elif file_name == 'losses.csv':
            amount_in_file = 'loss_amount'


        date_in_file = 'purchase_date'

        if file_name == 'sales.csv':
            date_in_file = 'sales_date'

        elif file_name == 'losses.csv':
            date_in_file = 'loss_date'


        modification = False

        for row in rows:
            
            if (row['id'] == search_type or row['name'] == search_type) and row[amount_in_file] == input_amount and row[date_in_file] == input_date and row['expiration_date'] == expiration_date and modify_type == 'increase'.lower():
                row[quantity_in_file] = int(row[quantity_in_file]) + int(quantity)                                                                                                          # LET OP!!! Wanneer je na de 'or' operator nog meer\
                                                                                                                                                                                            # operarors gaat gebruiken (zoals de 'and' operator\
                                                                                                                                                                                            # operarors gaat gebruiken (zoals de 'and' operator\
                                                                                                                                                                                            # operarors gaat gebruiken (zoals de 'and' operator\
                                                                                                                                                                                            # operarors gaat gebruiken (zoals de 'and' operator\
                                                                                                                                                                                            # in deze 'if statement'), moet je de 'or' operators\
                                                                                                                                                                                            # tussen haakjes\# plaatsen, want anders werkt je\
                print("\n")                                                                                                                                                                 # code / de 'if statement' # niet.
                print(F"Great! Product '{search_type}' with {relevant_amount} '{input_amount}', {relevant_date} '{input_date}' and expiration date '{expiration_date}' in the '{file_name[:-4]}' file, has been 'increased' with a quantity of\
 '{quantity}'. See the result below.\n") 
                print(F"Result = {row}")
                
                modification = True
                break

            elif (row['id'] == search_type or row['name'] == search_type) and row[amount_in_file] == input_amount and row[date_in_file] == input_date and row['expiration_date'] == expiration_date and modify_type == 'decrease'.lower():
                row[quantity_in_file] = int(row[quantity_in_file]) - int(quantity)
                print("\n")
                print(F"Great! Product '{search_type}' with {relevant_amount} '{input_amount}', {relevant_date} '{input_date}' and expiration date '{expiration_date}' in the '{file_name[:-4]}' file, has been 'decreased' with a quantity of\
 '{quantity}'. See the result below.\n")
                print(F"Result = {row}")
                print("\n")
                
                modification = True
                break
        
            else:
                modification = False
        
        if modification == False:
            print("\n")
            print(F"Entered product details:")
            print(F"Product 'id' or 'name' = '{search_type}', product '{relevant_amount}' = '{input_amount}', product '{relevant_date}' = '{input_date}' and product 'expiration date' = '{expiration_date}'.")
            print("\n")
            product_in_file_check(file_name, search_type)
            print(F"Hello user! One or more of the entered product details wasn't filled in correctly. Please check the differences between the 'Entered product details' shown above and the 'Product details for product {search_type} in the\
 {file_name[:-4]} file' also shown above.\n")
            
        file.seek(0)

    with open(file_name, 'r+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        print("\n")

# print(modify_quantity())
# print("\n")

# HIER BEN IK MET MIJN FUNCTIES / CODES TESTEN!!!
'''
Wijzigen van de productdetails. Begonnen op maandag 26-02-2024. DEZE FUNCTIE DOET HET VOLLEDIG PER WOENSDAG 13-03-2024.

- Woensdag 27-03-2024 rond 23:10 uur = Witregels '("\n") aangepast en deze functie gekopieerd naar mijn Superpy document.

- Zondag 24-03-2024 rond 15:26 uur = Functie opnieuw gecheckt n.a.v. de houbaarheidsdatum check die ik heb\
aangepast bij vraag 3.
'''

def modify_product_details():

    print("\n")
    
    print("Hello user, and welcome to the 'modify product details' menu. Follow the steps below to modify the details of a product in a chosen file.\n")

    print("Step 1 = Enter the name of the file you want to modify the product detail in: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Step 2 = Enter the 'name' or the 'id' of the product for which you want to modify the product detail for (not case sensitive).")
    print("Step 3 = Enter the product expiration date as follows: dd-mm-yyyy.")
    print("Step 4 = Enter the detail of the product you want to change and seperate each part of the detail with an underscore, for instance 'product_name' or 'product_purchase_amount' etc. (not case sensitive).")
    print("Step 5 = Enter the modification you want to make for the product (not case sensitive).")
    print("Done!\n")


    while True:
        file_name = input("Step 1 = Enter the name of the file you want to modify the product detail in: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        
        if file_name == "inventory":
            file_name = "inventory_file.csv"
            print("\n")
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "sales":
            file_name = "sales_file.csv"
            print("\n")
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "losses":
            file_name = "losses_file.csv"
            print("\n")
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        else:
            print("\n")
            print(F"Hello user! There is no file named '{file_name}'. Please enter the correct file name (not case sensitive).\n")
            
            continue
        break


    while True:
        search_type = input("Step 2 = Enter the 'name' or the 'id' of the product for which you want to modify the product detail for (not case sensitive): ").lower()
        
        if product_in_file_check(file_name, search_type) == True:
            print(F"Great! Product '{search_type}' is found in the '{file_name[:-4]}' file. You can see the product details above.\n")
        
        else:
            print(F"Hello user! Product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product 'name' or 'id' (not case sensitive).\n")

            continue
        break


    while True:
        expiration_date = input(F"Step 3 = Enter the expiration date of product '{search_type}' as follows: dd-mm-yyyy: ")


        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print("\n")
            print(F"Hello user! '{expiration_date}' isn't the correct format to fill in the expiration date for product {search_type}. Please enter the expiration date in the following format: dd-mm-yyyy.\n")
            
            continue

        expiration_date_check = data_in_file_check(file_name, search_type, "product_expiration_date")   # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven\
                                                                                                        # ingevulde variabel: 'search_type' dat het door de gebruiker ingevulde product is.
        
        if expiration_date in expiration_date_check:    # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn 'input' statement 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'data_in_file_check' functie\
                                                        # dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te gebruiken\
                                                        # i.p.v. de '==' operator, want met de 'in' operator kijk je of er iets 'wel' of 'niet' in een lijst zit.
            (product_in_file_check(file_name, search_type))
            print(F"Great! The entered expiration date '{expiration_date}' of product '{search_type}' in the '{file_name[:-4]}' file matches one of the expiration dates shown above in the product details.\n")
        
        else:
            (product_in_file_check(file_name, search_type))
            print(F"Hello user! The entered expiration date '{expiration_date}' doesn't match one or more of the expiration dates of product '{search_type}' in the '{file_name[:-4]}' file. Please check the details for product '{search_type}' above for the correct expiration date.\n")

            continue
        break


    while True:
        column_name = (input(F"Step 4 = Enter the name of the detail for product '{search_type}' that you want to modify and seperate each part of the detail with an underscore, for instance 'product_name' or 'product_purchase_amount' etc. (not case sensitive): ")).lower()
        print("\n")

        if column_name in column_name_check(file_name):
            print(F"Great! The product detail '{column_name}' for product '{search_type}' is found in the '{file_name[:-4]}' file. You can check all the product detail names from the '{file_name[:-4]}' file above.\n")

        else:
            print(F"Hello user! The entered product detail '{column_name}' for product '{search_type}' was not found in the '{file_name[:-4]}' file. Please check all the product details from the '{file_name[:-4]}' file above and enter the correct product detail for product '{search_type}' (not case sensitive).\n")

            continue
        break


    while True:
        product_detail = (input(F"Step 5 = Enter the modification you want to make for the product detail '{column_name}' for product '{search_type}' in the '{file_name[:-4]}' file (not case sensitive): ")).lower()
        
        if column_name == "product_id" or column_name == "product_quantity" or column_name == "loss_quantity":
            
            try:
                int(product_detail)

            except ValueError:
                print("\n")
                print(F"Hello user! The modification for product detail '{column_name}' for product '{search_type}' in the '{file_name[:-4]}' file can only contain numbers. '{product_detail}' doesn't only contain numbers. Please enter the correct modification for product detail '{column_name}'.\n")
            
                continue


        elif column_name == "product_purchase_amount" or column_name == "product_sales_amount" or column_name == "loss_amount":
        
            try:
                product_detail = float(product_detail)

            except ValueError:
                print("\n")
                print(F"Hello user! The modification for product detail '{column_name}' for product '{search_type}' in the '{file_name[:-4]}' file can only contain an amount or a dot to seperate any decimals. '{product_detail}' doesn't only contain an amount or a dot. Please enter the correct modification for product detail '{column_name}' for product '{search_type}' and use a dot in stead of a comma to seperate any decimals.\n")
                
                continue


        elif column_name == "product_purchase_date" or column_name == "product_sales_date" or column_name == "product_expiration_date" or column_name == "loss_date":
            
            try:
                convert_to_dutch_date(product_detail)
                
            except ValueError:
                print("\n")
                print(F"Hello user! '{product_detail}' isn't the correct format to fill in the date for product '{search_type}' in file '{file_name}. Please enter the date in the following format: dd-mm-yyyy.\n")
        
                continue
        break


    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        for row in rows:
            if (row['product_name'] == search_type or row['product_id'] == search_type) and row["product_expiration_date"] == expiration_date:
                
                (product_in_file_check(file_name, search_type))
                
                yes_or_no = input(F"Are you sure you want to modify the product detail '{column_name}' for product '{search_type}' with expiration date '{expiration_date}' shown above in the '{file_name[:-4]}' file to '{product_detail}'? Press 'Y' or 'N' (not case sensitive): ")
                
                if yes_or_no == 'Y' or yes_or_no == 'y':
                    row[column_name] = product_detail
                    print("\n")
                    print(F"Great! The product detail '{column_name}' for product '{search_type}' with expiration date '{expiration_date}' in the '{file_name[:-4]}' file has been modified to '{product_detail}'. You can check the product details below.\n")
                    print(row)
                    print("\n")
                    break
                    
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    print("\n")
                    print(F"Oké. The product detail '{column_name}' for product '{search_type}' with expiration date '{expiration_date}' in the '{file_name[:-4]}' file has not been modified to '{product_detail}'. You can check the product details below.\n")
                    print(row)
                    print("\n")
                    break
        
        file.seek(0)

    with open(file_name, 'r+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
# print(modify_product_details())
# print("\n")


'''
Product verwijderen op bais van 'naam' of 'id' én in combinatie met de houdbaarheidsdatum. DEZE CODE DOET HET PER ZATERDAGNACHT 09-03-2024 ROND 02:39 UUR.
'''

def remove_product():

    print("\n")

    print("Hello user, and welcome to the 'remove product' menu.\n")
        
    print("Follow the steps below to remove a product from a chosen file.\n")
    
    print("Step 1 = Enter the 'name' of the file in which you want to remove a product.")
    print("Step 2 = Enter the 'name' or the 'id' of the product that you want to remove (not case sensitive).")
    print("Step 3 = Enter the product 'expiration_date'.")
    print("Step 4 = Double check if you have chosen the correct product to remove.")
    print("Step 5 = Enter 'Y' if you are sure you want to remove the product. Or enter 'N' if you don't want to remove the product (not case sensitive).")
    print("Done!.\n")
    
    while True:
        file_name = input("Step 1 = Enter the 'name' of the file in which you want to remove a product: 'inventory', 'sales' or 'losses': ").lower()
        print("\n")

        if file_name == "inventory".lower():
            file_name = "inventory_file.csv"
            print(F"The '{file_name[:-4]}' file is found.\n")
        
        elif file_name == "sales".lower():
            file_name = "sales_file.csv"
            print(F"The '{file_name[:-4]}' file is found.\n")
        
        elif file_name == "losses".lower():
            file_name = "losses_file.csv"
            print(F"The '{file_name[:-4]}' file is found.\n")

        else:
            print(F"Sorry, but there is no file named '{file_name}'. Please enter the correct file name (not case sensitive).\n")
            
            continue
        break
    
    
    while True:
        search_type = input("Step 2 = Enter the product 'name' or 'id' (not case sensitive): ").lower()
        print("\n")

        if product_in_file_check(file_name, search_type) == True:
            print(F"Product '{search_type}' is found in the '{file_name[:-4]}' file. You can see the product details above.\n")
        
        else:
            print(F"Sorry, but product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product 'name' or 'id' (not case sensitive).\n")

            continue
        break


    while True:
        expiration_date = input(F"Step 3 = Enter the expiration date for product '{search_type}' which you want to remove as follows: dd-mm-yyyy: ")
        print("\n")

        try:
            date_check = datetime.datetime.strptime(expiration_date, "%d-%m-%Y")
            
        except ValueError:
            print(F"Sorry, but '{expiration_date}' isn't the correct format to fill in the 'expiration date' for product '{search_type}'. Please enter the expiration date in the following format: dd-mm-yyyy.\n")
            
            continue

        expiration_date_check = search_file_data(file_name, search_type, "product_expiration_date") # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven ingevulde\
        # print(expiration_date_check)                                                          # 'search_type' product.

        if expiration_date in expiration_date_check:    # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn 'input' statement 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'search_file_data' functie\
                                                        # dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te gebruiken\
                                                        # i.p.v. de '==' operator, want met de 'in' operator kijk je of er iets 'wel' of 'niet' in een lijst zit.
        
            print(F"Great! The entered expiration date '{expiration_date}' of product '{search_type}' in the '{file_name[:-4]}' file matches one of the expiration dates shown above in the 'product details'.\n")
            
        else:
            print(F"Sorry, but the entered expiration date '{expiration_date}' doesn't match one or more of the expiration dates of product '{search_type}' in the '{file_name[:-4]}' file. Please check the details for product '{search_type}' above for the correct expiration date.\n")

            continue
        break


    with open(file_name, 'r', newline= '',) as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        for row in rows:

            if (row['product_name'] == search_type or row['product_id'] == search_type) and row["product_expiration_date"] == expiration_date:
            
                yes_or_no = input(F"Are you sure you want to remove product '{search_type}' from the '{file_name[:-4]}' file? Press 'Y' or 'N' (the letters are not case sensitive): ").lower()
                print("\n")

                if yes_or_no == 'Y' or yes_or_no == 'y':
                    rows.remove(row)
                    print("\n")
                    print(F"Product '{search_type}' with expiration date '{expiration_date}' is removed from the '{file_name[:-4]}' file.")
                    print("\n")
                    break
                    
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    print("\n")
                    print(F"Product '{search_type}' with expiration date '{expiration_date}' is not removed from the '{file_name[:-4]}' file.\n")
                    print("\n")
                    break
            
        file.seek(0)
        
    with open(file_name, 'w', newline= '') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# print(remove_product())
# print("\n")


'''
LET OP!!! Deze code moet ik nog aanpassen met input statements én door gebruik te maken van mijn 'data in file' functie bij regel 528 hierboven.
Specifieke data van een bestand pakken met de volgende zoektermen: 'bestandsnaam', 'product naam' of 'product id'. DEZE CODE DOET HET PER VRIJDAG 22-03-2024!!! 
'''

def collect_product_details():
    
    print("\n")
    
    print("Hello user, and welcome to the 'collect product details' menu.\n")

    print("Follow the steps below to collect the details of a product in a chosen file.\n")

    print("Step 1 = Enter one of the following file names to collect the product details from: 'inventory', 'sales' or 'losses' (not case sensitive).")
    print("Step 2 = Enter the product 'name' or 'id' of which you want to collect the product details from (not case sensitive).")
    print("Step 3 = Enter the name of the 'product detail' you want to collect and seperate each part of the detail with an underscore, for instance 'product_name' or 'product_purchase_amount' etc. (not case sensitive).")
    print("Done!\n")


    while True:
        file_name = input("Step 1 = Enter one of the following file names to collect the product details from: 'inventory', 'sales' or 'losses' (not case sensitive): ").lower()
        print("\n")

        if file_name == "inventory":
            file_name = "inventory_file.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        elif file_name == "sales":
            file_name = "sales_file.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")
            
        elif file_name == "losses":
            file_name = "losses_file.csv"
            print(F"Great! The '{file_name[:-4]}' file is found.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following three file names: 'inventory', 'sales' or 'losses' (not case sensitive).\n")
            
            continue
        break


    while True:
        search_type = input("Step 2 = Enter the product 'name' or 'id' of which you want to collect the product details from (not case sensitive): ").lower()
        print("\n")

        if product_in_file_check(file_name, search_type) == True:
            print(F"Great! Product '{search_type}' is found in the '{file_name[:-4]}' file. You can see the product details above.\n")
        
        else:
            print(F"Hello user! Product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product 'name' or 'id' (not case sensitive).\n")

            continue
        break


    while True: # LET OP!!! DEZE WHILE LOOP MOET IK DUS VERANDEREN WANNEER IK ALLE KOLOMNAMEN HEB AANGEPAST.
        column_name = (input("Step 3 = Enter the name of the 'product detail' you want to collect and seperate each part of the detail name with an underscore, for instance 'product_name' or 'product_purchase_amount' etc. (not case sensitive): ")).lower()
        print("\n")

        if column_name not in column_name_check(file_name):
            print(F"Hello user! The entered product detail name '{column_name}' for product '{search_type}' was not found in the '{file_name[:-4]}' file. Please enter the correct product detail name for product '{search_type}' (not case sensitive).")
            print(F"You can check all the product detail names of the '{file_name[:-4]}' file above.\n")

            continue

        else:
            print(F"Great! The entered product detail name '{column_name}' of product '{search_type}' is found in the '{file_name[:-4]}' file. You can check all product detail names of the '{file_name[:-4]}' file above.\n")
            print(F"And you can see all the collected details from '{column_name}' of product '{search_type}' from the '{file_name[:-4]}' file below.\n")
            
        break


    print(F"'{column_name}(s)' for product '{search_type}':")
    print(data_in_file_check(file_name, search_type, column_name))
    print("\n")
    
# print(collect_product_details())
# print("\n")


'''
Met de 'calculate_costs' functie kan je de totale kosten / inkoopprijs van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.
''' 

def calculate_costs(from_date: datetime.datetime , until_date: datetime.datetime):
    
    with open("inventory_file.csv", 'r') as inventory_file:
        reader = csv.DictReader(inventory_file)

        total_inventory = 0

        for row in reader:
        
            product_purchase_date = datetime.datetime.strptime(row["product_purchase_date"], "%d-%m-%Y")

            if from_date <= product_purchase_date and until_date >= product_purchase_date:
            # if begin_date <= product_purchase_date and end_date >= product_purchase_date:
                inventory = float(row["product_quantity"]) * float(row["product_purchase_amount"])
            
                total_inventory += inventory
        
        return round(total_inventory, 2)


'''
Met de 'calculate_revenue' functie kan je de totale omzet van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.
''' 

def calculate_revenue(from_date: datetime.datetime, until_date: datetime.datetime):

    with open("sales_file.csv", 'r') as sales_file:
        reader = csv.DictReader(sales_file)

        total_revenue = 0

        for row in reader:
        
            product_sales_date = datetime.datetime.strptime(row["product_sales_date"], "%d-%m-%Y")

            if from_date <= product_sales_date and until_date >= product_sales_date:
                revenue = float(row["product_quantity"]) * float(row["product_sales_amount"])
            
                total_revenue += revenue
        
        return round(total_revenue, 2)
        

'''
Met de 'calculate_profit' functie kan je de totale winst van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.
''' 

def calculate_profit(from_date, until_date):
    
    with open("sales_file.csv", 'r') as sales_file:
        reader = csv.DictReader(sales_file)

        total_profit = 0

        for row in reader:
    
            product_sales_date = datetime.datetime.strptime(row["product_sales_date"], "%d-%m-%Y")

            if from_date <= product_sales_date and until_date >= product_sales_date:
                profit = (calculate_revenue(from_date, until_date)) - (calculate_costs(from_date, until_date)) # De datum wordt hier toch op de Engelse manier weergegeven en ik wil het op de NL manier.
                        
                total_profit += profit
                
        return round(profit, 2)


'''
Met de 'time_frame_calculation' functie kan je de zelf kiezen wat je wilt uitrekenen in een door jou opgegeven periode: kosten, omzet of de winst. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.
''' 

def time_frame_calculation():

    print("Hello user, and welcome to the 'time frame calculation' menu. Follow the steps below to choose frow which time frame you want to see the calculation for the 'costs', the 'revenue' or the 'profit'.\n")
    print("Step 1 = Enter 'costs', 'revenue' or 'profit' to see the total calculation within a chosen time frame.")
    print("Step 2 = Enter the 'from' date as follows: dd-mm-yyyy.")
    print("Step 3 = Enter the 'until' date as follows dd-mm-yyyy.\n")


    while True:
        time_frame_type = input("Step 1 = Enter 'costs', 'revenue' or 'profit' to see the corresponding time frame: ").lower()
        print("\n")

        if time_frame_type == "costs" or time_frame_type == "revenue" or time_frame_type == "profit":
            print(F"Data for '{time_frame_type}' collected.\n")

        else:
            print(F"Hello user. '{time_frame_type}' Isn't the correct option for choosing a time frame. Please enter: 'costs' or 'revenue' or 'profit' to see the correct calculation within the chosen time frame.\n")
            continue
        break

    
    while True:
        from_date = input("Enter the 'from' date as follows: dd-mm-yyyy: ")
        print("\n")

        try:
            from_date = datetime.datetime.strptime(from_date, "%d-%m-%Y")
            
        except ValueError:
            print(F"Hello user. '{from_date}' Isn't the correct format to fill in the 'until' date. Please enter the correct 'from' date in the following format: dd-mm-yyyy.\n")

            continue
        break


    while True:
        until_date = input("Step 3 = Enter the 'until' date as follows dd-mm-yyyy: ")
        print("\n")

        try:
            until_date = datetime.datetime.strptime(until_date, "%d-%m-%Y")
            
        except ValueError:
            print(F"Hello user. '{until_date}' Isn't the correct format to fill in the 'until' date. Please enter the correct 'until' date in the following format: dd-mm-yyyy.\n")

            continue
        break    

    
    if time_frame_type == "costs":
        outcome = (calculate_costs(from_date, until_date))
        
    elif time_frame_type == "revenue":
        outcome = (calculate_revenue(from_date, until_date))
    
    elif time_frame_type == "profit":
        outcome = (calculate_profit(from_date, until_date))
        
    from_date = datetime.datetime.strftime(from_date, "%d-%m-%Y")
    until_date = datetime.datetime.strftime(until_date, "%d-%m-%Y")

    return F"The '{time_frame_type}' from '{from_date}' until '{until_date}' = EUR '{outcome}'."


if __name__ == "__main__":

    print("\n")
    
    # print(date_in_file())
    # print("\n")

    # print(current_date())
    # print("\n")

    # print(create_inventory_file())
    # print("\n")

    # print(create_sales_file())
    # print("\n")

    # print(sales_function())
    # print("\n")

    # print(create_losses_file())
    # print("\n")

    # print(add_losses_products())
    # print("\n")

    # print(add_sales_products())
    # print("\n")

    # print(sold_products())
    # print("\n")
    
    # print(select_file_for_data(" ", " "))
    # print("\n")
    
    # print(get_file_data())
    # print(get_file_data(" ", ""))
    # print("\n")
    
    # print(sum_existing_products('1210', 'brood', '24-01-2024', '24-01-2025'))
    # print("\n")

    # print(add_test_products())
    # print("\n")

    # print(add_products())
    # print("\n")
    
    # print(find_products())
    # print("\n")

    # print(find_product_id("12345"))
    # print(find_product_id("product_id"))
    # print("\n")

    # print(clear_inventory_file())
    # print("\n")

    # print(clear_sales_file())
    # print("\n")

    # print(show_all_products())
    # print("\n")

    # print(remove_product())
    # print("\n")
    
    # print(remove_product_name("melk"))
    # print("\n")

    # print(remove_product_id())
    # print("\n")

    # print(get_data_from_file("inventory_file.csv", "product_quantity"))
    # print("\n")
    