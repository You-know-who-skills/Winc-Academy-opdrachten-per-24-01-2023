
# Imports

import csv
from argparse import *
from datetime import timedelta
from datetime import datetime
from rich import print as rprint
from rich.console import Console
from rich.table import Table

import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)
import pandas as pd

print('\n')

# User functions - create or clear files.

'''
Één van de 3 bestanden opnieuw maken: 'Inventory', 'Sales' en 'Losses'. DEZE CODE DOET HET!!! Per maandag 03-06-2024 rond 22:45 uur.\
- Ik heb alle 3 de losse functies die de bestanden 'Inventory', 'Sales' en 'Losses' creëren samengevoegd tot 1 functie. Ik heb vrijwel\
  al mijn functies / codes op deze manier geschreven zodat de gebruiker de mogelijkheid heeft om te kiezen wat hij / zij wil doen, dus\
  waarom deze 3 functies niet. Naar mijn mening werkt dit namelijk makkelijker, sneller én efficienter. Zie de oude notities van de 3\
  losse functies hieronder.

Notitie van mijn losse 'inventory' functie:
- Inventory bestand maken. DEZE CODE DOET HET!!! Per donderdag 28-03-2024 rond 23:52 uur.
- Vrijdagnacht 10-05-2024 = Oude kolomnamen aangepast naar de nieuwe kolomnamen.
- Donderdag 28-03-2024 rond 23:52 uur = Code aangepast en getest.

Notitie van mijn losse 'sales' functie:
Sales bestand maken. DEZE CODE DOET HET!!! Per vrijdagnacht 29-03-2024 rond 00:02 uur.
- Vrijdagnacht 10-05-2024 = Oude kolomnamen aangepast naar de nieuwe kolomnamen.
- Vrijdagnacht 29-03-2024 rond 00:02 uur = Code aangepast en getest.

Notitie van mijn losse 'losses' functie:
Losses bestand maken. DEZE CODE DOET HET!!! Per vrijdagnacht 29-03-2024 rond 00:11 uur.
- Vrijdagnacht 29-03-2024 rond 00:11 uur = Code aangepast en getest.
'''

def create_new_file():

    rprint("- Hello user, and welcome to the [bright_cyan]'create file'[/bright_cyan] option. With this option you can create the following files: 'Inventory', 'Sales' or 'Losses' (not case sensitive).\n")

    print("- Follow the step(s) below to create one of the following files: 'Inventory', 'Sales' or 'Losses' (not case sensitive).\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'create a new file'")

    table.add_row("- Step 1 = Enter one of the following file names to create the file: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to create the file: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory' or file_name == 'sales' or file_name == 'losses':
            rprint(F"[green] Great!:thumbs_up: The '{file_name.capitalize()}' file has been created.[/green]")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names to create it: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

            continue
        break

    print('\n')

    if file_name == 'inventory':
        with open('inventory.csv', 'w', newline='') as inventory_file:
            writer = csv.DictWriter(inventory_file, fieldnames=['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
            # write = csv.DictWriter(inventory_file, delimiter= '\t', fieldnames=['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])    # LET OP!!! Als je een andere scheidingsteken dan de komma wil\
                                                                                                                                                                        # gebruiken, dan doe je dat # met de 'delimiter=''' code. De\
                                                                                                                                                                        # 'delimiter=''' code plaats je tussen de 'bestandsnaam' en de\
                                                                                                                                                                        # 'fieldnames' in.
            writer.writeheader()

    elif file_name == 'sales':
        with open('sales.csv', 'w', newline='') as sales_file:
            writer = csv.DictWriter(sales_file, fieldnames=['id', 'name', 'sold_quantity', 'sales_amount', 'sales_date', 'expiration_date'])
            writer.writeheader()

    elif file_name == 'losses':
        with open('losses.csv', 'w', newline='') as losses_file:
            writer = csv.DictWriter(losses_file, fieldnames=['id', 'name', 'loss_quantity', 'loss_amount', 'loss_date', 'loss_cause', 'expiration_date'])
            writer.writeheader()

# print(create_new_file())
# print('\n')


'''
Gehele 'inventory' bestand leeg maken. DEZE CODE DOET HET!!! Per dinsdag 02-04-2024 rond 15:48 uur.
- Dinsdag 02-04-2024 rond 15:48 uur = Ik heb de 3 losse 'clear_file()' functies samengevoegd in 1 functie. Ik heb de functie\
  getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- Dinsdag 19-03-2024 rond 15:49 uur = Ik heb deze functie aangepast en getest op 
'''

def clear_file():

    rprint("- Hello user, and welcome to the [bright_cyan]'clear file'[/bright_cyan] option. With this option you can clear a selected file from all it's products.\n")

    print("- Follow the step(s) below to clear a selected file from all it's products. Have fun clearing!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'clear a file'")
        
    table.add_row("- Step 1 = Enter one of the following file names to clear all the products: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Step 1 = Confirm if you 'do' or 'don't' want to clear the file of all it's products with 'Y' for Yes or 'N' for No (not case sensitive)")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to clear all the products: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            
        elif file_name == 'sales':
            file_name = 'sales.csv'
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            
        else:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

            continue
        break


    print('\n')
    yes_or_no = input(F"Are you sure you want to clear the '{file_name.capitalize()[:-4]}' file from all it's products? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
        
    if yes_or_no == 'Y' or yes_or_no == 'y':
        print('\n')
        rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file has been cleared of all it's products.[/green]\n")
        print('\n')

        if file_name == 'inventory.csv':
            with open('inventory.csv', 'w', newline='') as inventory_file:
            
                writer = csv.DictWriter(inventory_file, fieldnames=['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
                writer.writeheader()

        elif file_name == 'sales.csv':
            with open('sales.csv', 'w', newline='') as sales_file:
            
                writer = csv.DictWriter(sales_file, fieldnames=['id', 'name', 'sold_quantity', 'sales_amount', 'sales_date', 'expiration_date'])
                writer.writeheader()
        
        elif file_name == 'losses.csv':
            with open('losses.csv', 'w', newline='') as losses_file:
            
                writer = csv.DictWriter(losses_file, fieldnames=['id', 'name', 'loss_quantity', 'loss_amount', 'loss_date', 'loss_cause', 'expiration_date'])
                writer.writeheader()

    elif yes_or_no == 'N' or yes_or_no == 'n':
        print('\n')
        rprint(F"[wheat1]Okay. The [green]'{file_name.capitalize()[:-4]}'[/green] file will not be cleared of all it's products.[/wheat1]\n")
        print('\n')
        

# print(clear_file())
# print('\n')


# User function – export files to Excel.

'''
Een door jou gekozen csv bestand converteren naar een Excel bestand. DEZE CODE DOET HET!!! Per maandag 19-02-2024.
- Dinsdagnacht 19-03-2024 rond 00:30 uur = Code aangepast.
- Vrijdagnacht 29-03-2024 rond 00:19 uur = Code aangepast en getest.
'''

def export_file_to_excel():

    rprint("- Hello user, and welcome to the [bright_cyan]'export file to Excel'[/bright_cyan] option. With this option, you can export a selected file to an Excel file.\n")

    print("- Follow the step(s) below to export a selected file to an 'Excel' file. Have fun exporting!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")
    
    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'export a file to Excel'")
        
    table.add_row("- Step 1 = Enter one of the following file names to export it to Excel: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to export it to Excel: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/green]\n")

        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/green]\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

            continue
        break


    if file_name == 'inventory.csv':
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel('inventory.xlsx',
                        index_label= 'Count',
                        freeze_panes= (1,1)
                        )
    
    if file_name == 'sales.csv':
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel('sales.xlsx',
                        index_label= 'Count',
                        freeze_panes= (1,1)
                        )
    
    if file_name == 'losses.csv':
        csv_file = pd.read_csv(file_name)
        csv_file.index += 1
        csv_file.to_excel('losses.xlsx',
                        index_label= 'Count',
                        freeze_panes= (1,1)
                        )

# print(export_file_to_excel())
# print('\n')


# Help functions – convert and use dates.

'''
De huidige datum returnen ZONDER menu en datums omzetten naar 'datetime objecten. DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
- Zaterdagnacht 06-04-2024 rond 00:55 uur ben ik met onderstaande functies bezig geweest. Dit omdat\
  de input statements met datums in mijn functies geen vergelijking konden maken tussen een string en\
  een datetime object (b.v. 'if input_date < current_date()'. Daarom heb ik de functie\
  'convert_to_strptime()' toegevoegd zodat ik hiermee dit soort input statements wel kon\
  omzetten naar een datetime object.

    - current_date() = aangepast;
    - convert_to_strptime() = toegevoegd;
    - convert_to_dutch_date() = niet aangepast.

Ik had deze code al eerder geschreven op zondagnacht 10-03-2024, maar dan met de 'datetime.date.today()' code
en dat veroorzaakte een foutmelding met mijn current date functie in andere functies. Dus heb ik deze code
op advies van een Winc mentor opnieuw geschreven met de 'datetime.today()' en toen kreeg ik geen
conflicten meer in m'n code.
'''


def current_date():

    return datetime.today()
    
# print(current_date())
# print('\n')


def convert_to_strptime(datetime_object: datetime):

    return datetime.strptime(datetime_object, "%d-%m-%Y")

# print(convert_to_strptime())
# print('\n')


def convert_to_strftime(string: datetime):

    return datetime.strftime(string, "%d-%m-%Y")

# print(convert_to_strftime())
# print('\n')


def convert_to_dutch_date(date_format: datetime):

    return datetime.strptime(date_format, "%d-%m-%Y").strftime("%d-%m-%Y") # Met de 'datetime module' maak je een 'datetime' object aan. Met 'strptime' (en 'strp' kan je zien als 'strippen' in de zin van dat je de tijd uit het object\
                                                                                    # stript / haalt) haal je dus de tijd uit de 'today' code.
# print(convert_to_dutch_date())
# print('\n')


# User functions – use or modify dates in the system.


'''
De huidige datum returnen MET menu. DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
Ik ben ook met deze functie begonnen op vrijdag 15-03-2024.

- Dinsdag 07-05-2024 rond 23:57 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen\
  (door ze korter te maken)'. En hij doet het nog prima!!!
'''

def update_system_date():
    
    rprint("- Hello user, and welcome to the [bright_cyan]'update the system date'[/bright_cyan] option. With this option you can update the system date to the current date.\n")
    
    print("- Follow the step(s) below to update the system date. Have fun updating!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'update the system date'")
        
    table.add_row("- Step 1 = Enter 'Y' for Yes if you 'do' or 'N' for No if you 'don't' want to update the system date to the current date (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        update_system = (input("Step 1 = Enter 'Y' for Yes if you 'do' want to 'update the system date'. Or enter 'N' for No if you 'don't' want to update the system date (not case sensitive): ")).lower()
        print('\n')

        if update_system == "y":
            rprint("[green]Great!:thumbs_up: The date of the system has been updated to the current date. You can see the current date below.[/green]\n")

        elif update_system == "n":
            rprint("[wheat1]Okay! The date of the system will not be updated to the current date.[/wheat1]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! '{update_system}' isn't the correct input for updating the system date to the 'current date'. Please enter 'Y' if you 'do' want to update the system date to the 'current date'. Or enter 'N'\
 if you 'don't' want to update the system date to the 'current date' (not case sensitive).[/orange3]\n")
            
            continue
        break


    today_date_datetime = current_date()

    if update_system == "y":
        today_date_string = convert_to_strftime(today_date_datetime)

        print(today_date_string)
        print('\n')

        with open('date_file.txt', 'w') as date_file:

            date_file.write(today_date_string)

# print(update_system_date())
# print('\n')


'''
Systeem datum aanpassen. DEZE AANGEPASTE FUNCTIE DOET HET PER DONDERDAG 14-03-2024 ÉN IS OP VRIJDAG 15-03-2024 ALS 'PRIMA'\
BEVONDEN DOOR EEN WINC MENTOR.

- Woensdagnacht 08-05-2024 rond 00:51 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen\
  (door ze korter te maken)'. En hij doet het nog prima!!!

- Deze functie deed het al per zondagnacht 10-03-2024 ROND 02:57 UUR, maar ik heb de naam
  (tijdrijzen functie / time travel) én de inhoud van deze functie aangepast op donderdag 14-03-2024
  naar 'change_system_date' na een consult met een Winc mentor.
- Met deze code kan je de systeem datum / de datum in het 'date_file.txt' bestand aanpassen naar welke
  datum je maar wilt met een door jou opgegeven aantal 'dagen' of 'weken'.
'''

def change_system_date(): # Met deze functie moet je de datum van je systeem aanpassen door de datum in het 'date_file.txt' bestand aan te passen.

    rprint("- Hello user, and welcome to the [bright_cyan]'change the system date'[/bright_cyan] option.\n")
        
    print("- Follow the step(s) below to change the system date by entering the number of 'days' or 'weeks' that you want to change the system date with. Have fun changing!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'change the system date'")
        
    table.add_row("- Step 1 = Enter 'days' if you want to change the system date in a period of 'days'. Or enter 'weeks' if you want to change the system date in a period of 'weeks' (not case sensitive).")
    table.add_row("- Step 2 = Enter 'past' if you want the system date to go in the 'past' or enter 'future' if you want the system date to go in to the 'future' (not case sensitive).")
    table.add_row("- Step 3 = Enter a 'number' for the couple of 'days' or 'weeks' that you want to change the system date with.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        days_or_weeks = input("Step 1 = Enter 'days' if you want to change the system date in a period of days. Or enter 'weeks' if you want to change the system date in a period of weeks (not case sensitive): ").lower()
        print('\n')

        if days_or_weeks == 'days' or days_or_weeks == 'weeks':
            rprint(F"[green]Great!:thumbs_up: Let's change the system date for a couple of '{days_or_weeks}'.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! '{days_or_weeks}' isn't the correct input to modify the system date. Please enter 'days' or 'weeks' for the correct system date modification.[/orange3]\n")

            continue
        break


    while True:
            past_or_future = input("Step 2 = Enter 'past' if you want the system date to go in the 'past' or enter 'future' if you want the system date to go in to the 'future' (not case sensitive): ").lower()
            print('\n')

            if past_or_future == 'past' or past_or_future == 'future':
                rprint(F"[green]Great!:thumbs_up: Let's change the system date for a couple of '{days_or_weeks}' in the '{past_or_future}'.[/green]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! '{past_or_future}' isn't the correct input to modify the system date. Please enter 'past' or 'future' for the correct system date modification.[/orange3]\n ")

                continue
            break


    while True:
        number = (input(f"Step 3 = Enter a 'number' for the couple of '{days_or_weeks}' that you want to change the system date with in the '{past_or_future}': "))
        print('\n')

        try:
            int(number)
            
        except ValueError:
            rprint(F"[orange3]:scream: Hello user! The number of '{days_or_weeks}' can only contain a 'number'. '{number}' doesn't only contain a number. Please enter a 'number' to continue with the system date modification.[/orange3]\n")
            
            continue

        if int(number) > 738958 and days_or_weeks == 'days': # Python geeft een foutmelding bij meer dan 738958 dagen in het verleden.
            rprint(F"[orange3]:scream: Hello user! The number you've entered '{number}' is to far in the '{past_or_future}' Please enter a number below 738958.[/orange3]\n")

            continue

        elif int(number) > 105000 and days_or_weeks == 'weeks': # Python geeft een foutmelding bij meer dan 105000 weken in het verleden.
            rprint(F"[orange3]:scream: Hello user! The number you've entered '{number}' is to far in the '{past_or_future}' Please enter a number below 105000.[/orange3]\n")
            
            continue
        break


    timedelta_days = timedelta(days= int(number))
    timedelta_weeks = timedelta(weeks= int(number))
    
    today_date = current_date()

    # Modify system date by days.
    if days_or_weeks == 'days' and past_or_future == 'past':
        system_date = today_date - timedelta_days
        
    elif days_or_weeks == 'days' and past_or_future == 'future':
        system_date = today_date + timedelta_days
        
    # Modify system date by weeks.
    elif days_or_weeks == 'weeks' and past_or_future == 'past':
        system_date = today_date - timedelta_weeks
        
    elif days_or_weeks == 'weeks' and past_or_future == 'future':
        system_date = today_date + timedelta_weeks
        
    string_date = convert_to_strftime(system_date)


    with open('date_file.txt', 'w') as date_file:

        date_file.write(string_date)

    return rprint(F"[green]Great!:thumbs_up: If we go '{number}' '{days_or_weeks}' into the '{past_or_future}', the date = '{string_date}'[/green]\n") # LET OP!!! Ik wilde eigenlijk ook nog de dag vóór de datum hebben (dus b.v. Monday etc.).

# print(change_system_date())
# print('\n')


'''
Naar een specifieke datum gaan door deze ook zelf in te voeren. DEZE CODE DOET HET PER ZATERDAGNACHT 16-03-2024!!!

- Woensdagnacht 08-05-2024 rond 00:19 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen\
  (door ze korter te maken)'. En hij doet het nog prima!!!
- Ik ben ook met deze functie begonnen op zaterdagnacht 16-03-2024.
- Ik wilde deze functie hebben naast de verplichte timedelta functie die ik van Winc moest schrijven omdat ik dit veel makkelijker vind,
  zie mijn 'change_system_date()' functie waarin ik de timedelta code heb verwerkt.
'''

def select_specific_date():
    
    rprint("- Hello user, and welcome to the [bright_cyan]'select a specific system date'[/bright_cyan] option. With this option you can go to a specific date in the system. Have fun selecting!\n")
    
    print("- Follow the step(s) below to go to a specific date in the system. Have fun selecting!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'select a specific system date'")

    table.add_row("- Step 1 = Enter the 'date' you want the system to go to as follows 'dd-mm-yyyy'.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        specific_date = (input("Enter the 'date' you want the system to go to as follows 'dd-mm-yyyy': "))
        print('\n')

        try:
            convert_to_dutch_date(specific_date)
            
        except ValueError:
            rprint(F"[orange3]:scream: Hello user! '{specific_date}' isn't the correct way to fill in the 'specific date'. Please enter the 'specific date' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        break


    with open('date_file.txt', 'w') as date_file:

        date_file.write(specific_date)
        rprint("[green]Great!:thumbs_up: The date of the system has been changed to the specific date. You can see the specific date below.[/green]\n")

    return specific_date

# print(select_specific_date())
# print('\n')


'''
Aftellen tot een bepaalde / speciale gelegenheidsdatum. DEZE CODE DOET HET!!! Per zaterdagnacht 30-03-2024 rond 01:12 uur.
- Woensdagnacht 08-05-2024 rond 02:15 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- Vrijdag 29-01-2024 = Code aangepast samen met mentor Christiaan.
- Zaterdagnacht 30-03-2024 = Code aangepast én getest.
- Zondagnacht 17-03-2024 = Begonnen én afgrond rond 00:06 uur: speciale gelegenheden tekst bestand gemaakt voor mijn\
 'special_occasion_countdown()' functie.
'''

def special_occasion_date():

    rprint("- Hello user, and welcome to the [bright_cyan]'special occasion countdown'[/bright_cyan] option.\n")

    print("- Follow the step(s) below to create a countdown for a 'special occasion'. Have fun with the countdown!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")
    
    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'start a special occasion countdown'")

    table.add_row("- Step 1 = Enter the 'date' of the 'special occasion countdown' as follows: dd-mm-yyyy.")
    table.add_row("- Step 2 = Type a 'sentence' that you want to add to the 'special occasion countdown' (for instance: Until Christmas!!!).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        special_occasion_date = input("Step 1 = Enter the 'date' of the 'special occasion countdown' as follows: dd-mm-yyyy): ")
        print('\n')

        try:
            convert_to_dutch_date(special_occasion_date)
            
        except ValueError:
            rprint(F"[orange3]:scream: Hello user! '{special_occasion_date}' Isn't the correct way to fill in the 'date' for the 'special occasion countdown'. Please enter the correct 'date' for the 'special occasion countdown' as follows:\
 dd-mm-yyyy.[/orange3]\n")
            
            continue
        

        input_date = convert_to_strptime(special_occasion_date) # Met deze code maak ik van mijn 'special_occasion_date' variabel een datetime object. Dit omdat het aan het begin van deze while loop nog niet opgeslagen is als een 'datetime\
        todays_date = current_date()                            # object' in / door Python, maar nog steeds als een 'string'. Dit kan je testen door de 'type' van mijn 'special_occasion_date' variabel te printen en dan zie je dat het hier\
                                                                # nog steeds een 'string' is. En door het met mijn variabel 'input_date' om te zetten naar een 'datetime object', kan je het dus wel weer vergelijken met een andere 'datetime\
                                                                # 'datetime objecten'. En in dit geval is dat mijn 'todays_date' variabel.
        if input_date > todays_date:
            rprint(F"[green]Great!:thumbs_up: The 'date' for the 'special occasion countdown': '{special_occasion_date}', has been filled in correctly.[/green]\n")

        elif input_date < todays_date:                                    
            rprint(F"[orange3]:scream: Hello user! The 'date' you've just entered: '{special_occasion_date}', is a date in the past. And we're not able to time travel... yet.:wink: Please enter the correct 'date' for the 'special occasion\
 countdown' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        break


    special_occasion_sentence = input("Step 2 = Type a 'sentence' that you want to add to the 'special occasion countdown' (for instance: Until Christmas!!!): ")
    print('\n')
    

    with open('special_occasion.txt', 'w') as file:
    
        datetime_countdown = input_date - todays_date                                                           # Dit zijn de variabelen die ik in de 'while loop' heb gebruikt. En omdat ik van deze variabelen 'datetime objecten' heb gemaakt\
        print(F"Original countdown in days, hours, minutes, seconds and micro seconds= {datetime_countdown}")   # kan ik hier ook met ze 'rekenen', dus de datums op- of aftrekken. En met deze print statement kan je zien hoe de uitkomst van\
        print('\n')                                                                                             # mijn 'datetime_countdown' code er normaal gesproken uit ziet.

        full_string_countdown = str(datetime_countdown)     # Om mijn 'datetime_countdown' variabel (bestaande uit mijn 'input_date' en 'todays_date' variabelen) te kunnen gebruiken als 'strings', heb ik ze hier 'gecast' naar een 'string'.\
                                                            # En zo kan ik beide 'datetime objecten' ('input_date' en 'todays_date') ook als string gebruiken.
        short_string_countdown = full_string_countdown[0:full_string_countdown.find(",")]   # Met deze index geef ik aan waar mijn 'string_countdown' variabel begint (= bij '0') en waar mijn 'string_countdown' variabel eindigt (= bij de\
        file.write(F"{short_string_countdown.upper()} {special_occasion_sentence}")         # komma). Dit omdat wanneer je de 'datetime_countdown' variabel volledig (dus zonder te slicen / te indexen) print (zie de print statement hierboven\
                                                                                            # bij de 'F-string'), dan zie je dat Python een komma plaatst tussen het aantal dagen en het tijdstip. Dus wanneer je wilt dat de komma en het\
                                                                                            # tijdstip niet zichtbaar zijn wanneer je de code print, moet je 'slicen' door een index te gebruiken. En met deze code kwam ik erachter dat je dus\
                                                                                            # ook kan slicen door een getal én een variabel in combinatie met de 'find()' code kunt gebruiken 'binnen een index'.
    
    return rprint(F"[green]Great!:thumbs_up: You can see the 'date' for the 'special occasion countdown' below.\n\n{short_string_countdown.upper()} {special_occasion_sentence}[/green]\n")

    
# print(special_occasion_date())
# print('\n')


# Help functions – check and show products and product details.

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
        rprint(F"[bright_magenta]These are the all the 'product detail names' in the '{file_name.capitalize()[:-4]}' file:[/bright_magenta]")
        rprint(F"[bright_cyan]{check_column_name}[/bright_cyan]")
        print('\n')

    return check_column_name

# print(column_name_check("losses_file.csv"))
# print('\n')


'''
Checken (op voorhand) of een product 'wel' of 'niet' in een bestand voor komt (b.v. bij mijn input statements 'Enter the product 'name' or 'id'. DEZE CODE DOET HET PER WOENSDAG 28-02-2024.
- Dinsdagnacht 28-05-2024 rond 00:08 uur = Ik heb deze funtie aangepast door de print statement 'print(F"Product details for product '{search_type}' in the '{file_name.capitalize()[:-4]}'\
  file:")' buiten de loop te plaatsen. Hierdoor komen de product details netjes en overzichtelijker onder elkaar te staan en dit scheelt witregels.
- Vrijdag 19-04-2024 rond 16:14 uur = De variabel 'product_in_file_check' aangepast naar 'product_in_file' omdat het niet de bedoeling is dat je variabelen maakt die dezelfde naam hebben\
  als de functie.
- Zaterdagnacht 13-04-2024 rond 00:42uur = functie aangepast door de print statement 'print('\n')' die 3 regels onder de 'with' statement stond te verwijderen. Dit omdat er een te grote\
  ruimte aan witregels ontstond in de for loop van mijn 'modify_qunatity()' functie.
- Maandagnacht 01-04-2024 rond 01:02 uur = Functie getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)' En hij doet het nog prima!!!
'''

def product_in_file_check(file_name: str, search_type: str):

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        product_in_file = False

        rprint(F"[bright_magenta]Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file:[/bright_magenta]")

        for row in rows:
            if row['name'] == search_type or row['id'] == search_type:
            
                product_in_file = True
                rprint(F"[bright_cyan]{row}[/bright_cyan]")

        print('\n')
        
        if product_in_file == True:
            return True
        
        elif product_in_file == False:
            rprint("[bright_cyan]{No products found}[/bright_cyan]\n")

# print(product_in_file_check('sales.csv', "ei"))
# print('\n')


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

def product_detail_check(file_name: str, search_type: str, column_name: str):

    '''
    This function:
    - searches for data / product details of a selected product in a selected column in a selected file and;
    - returns the found data / product details from the selected column.
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
                # LET OP!!! Je gebruikt in deze 'for loop' geen 'break' code omdat er dan maar 1 item wordt gereturned met de 'return' statement. En als je de 'break' code weghaalt, wordt het laatste item / het item helemaal onderaan\
                # het bestand gereturned. Dus wanneer je de gegevens die je zoekt met een 'for loop' wilt gebruiken (b.v. in een andere functie zoals ik met deze code heb gedaan in o.a. mijn 'modify_quantity' functie), dan kan je beter de\
                # gevonden gegevens eerst in een lijst plaatsen zoals ik hierboven heb gedaan met mijn variabel 'data_in_file = []'. Op deze manier kan je de gehele 'lijst' returnen én kan je de gegevens in de lijst weer gebruiken in\
                # andere functies.
        
        if data_in_file == True:
            
            return column_name_results

# print(product_detail_check('sales.csv', "pindakaas", 'sales_amount'))
# print('\n')


'''
Alle product details van een product in een gekozen bestand laten zien. DEZE CODE DOET HET PER VRIJDAG 19-04-2024 rond 17:38 uur.
- Maandag 27-05-2024 = Ik heb deze functie aangepast zodat enkel en alleen de product details te zien zijn zoals ze in het csv\
  bestand ook te zien zijn inclusief de nummering.
'''

def show_product_details(file_name: str, search_type: str, expiration_date: str):

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        rprint(F"[bright_magenta]Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file:[/bright_magenta]")

        for categorize, row in enumerate(rows, start=2):
            
            if (row['name'] == search_type or row['id'] == search_type) and row['expiration_date'] == expiration_date:
                rprint(F"[bright_cyan]{categorize}. {row}[/bright_cyan]")

    print('\n')

# print(show_product_details('inventory.csv', 'koek', '24-01-2025'))
# print('\n')

# print(show_product_details('sales.csv', 'pindakaas', '01-03-2024'))
# print('\n')


# User functions – view and find products and product details and avoid wasting products.

'''
Alle producten van een zelf gekozen bestand / 1 van de 3 bestanden laten zien. DEZE CODE DOET HET!!! Per maandag 18-03-2024 rond 22:30 uur!!!
- Dinsdag 02-04-2024 rond 16:38 uur = Ik heb de functie aangepast en getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
'''

def view_all_products():

    rprint("- Hello user, and welcome to the [bright_cyan]'view all products'[/bright_cyan] option. You can view all the products from one of the following files: 'Inventory', 'Sales' or 'Losses'.\n")

    print("- Follow the step(s) below to view all products from a selected file. Have fun viewing!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'view all of the products from a selected file'")
        
    table.add_row("- Step 1 = Enter one of the following file names to view all the products: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to view all the products: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products from the '{file_name.capitalize()[:-4]}' file below![/green]\n")

        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products from the '{file_name.capitalize()[:-4]}' file below![/green]\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products from the '{file_name.capitalize()[:-4]}' file below![/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

            continue
        break


    with open(file_name, 'r+') as file:
            reader = csv.reader(file) # Deze code plaatst elke regel van het csv bestand in een lijst.
            
            print(F"   {next(reader)}") # Met de 'next' code zorg je er voor dat de eerste regel van een bestand (dus in dit geval is het een csv bestand) word overgeslagen wanneer je een nummering gebruikt. Hierdoor kan ik in deze functie bij de\
                                        # 'enumerate' code dus wel 'start=1' gebruiken i.p.v. 'start=2' zoals ik dit in mijn andere functies gebruik.

            for categorize, row in enumerate(reader, start=1):
                rprint(F"{categorize}. {row}\n") # LET OP!!! De punt na de variabel 'categorize' zorgt ervoor dat er na de nummering van de 'enumerate' code een punt komt te staan.
                
# print(view_all_products())
# print('\n')


'''
Met de 'view_products_within_period' functie kan je de 'inventory', 'sold' en losses producten binnen een bepaalde periode zien. BEGONNEN OP MAANDAG 13-05-2024.

- Donderdag 16-05-2024 rond 18:19 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'.\
  En hij doet het nog prima!!!
- Ik moet deze code nog goed testen per dinsdag 14-05-2024.
''' 

def view_products_within_period():

    rprint("- Hello user, and welcome to the [bright_cyan]'view products within a certain period'[/bright_cyan] option.\n")

    print("- Follow the step(s) below to see the 'purchased', 'sold', 'loss' or 'expiration' dates of products within a certain period. Have fun viewing!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'view products within a certain period'")
        
    table.add_row("- Step 1 = Enter one of the followoing file names to see the products within a certain period: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Step 2 = Enter 'other' if you want to view the 'purchased', 'sold' or 'loss' dates of the products. Or enter 'expiration' if you want to view the expiration dates of the products in a certain periode (not case sensitive).")
    table.add_row("- Step 3 = Enter the 'from date' as follows: dd-mm-yyyy.")
    table.add_row("- Step 4 = Enter the 'until date' as follows dd-mm-yyyy.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the followoing file names to see the products within a certain period: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

            continue
        break


    # Variables to select the correct relevant date in the while loop for 'step 2' below.
    if file_name == 'inventory.csv':
        date_in_file = 'purchase date'

    elif file_name == 'sales.csv':
        date_in_file = 'sales date'

    elif file_name == 'losses.csv':
        date_in_file = 'loss date'


    while True:
        date_type = input("Step 2 = Enter 'other' if you want to view the 'purchased', 'sold' or 'loss' dates of the products. Or enter 'expiration' if you want to view the expiration dates of the products within a certain periode (not case\
 sensitive): ").lower()
        print('\n')

        if date_type == 'expiration':
            date_in_file = 'expiration date'
        
        if date_type == "other":
            rprint(F"[green]Great!:thumbs_up: It's noted that you want to view the '{date_in_file}' of the products from the '{file_name.capitalize()[:-4]}' file within a certain period.[/green]\n")

        elif date_type == 'expiration':
            rprint(F"[green]Great!:thumbs_up: It's noted that you want to view the 'expiration date' of the products from the '{file_name.capitalize()[:-4]}' file within a certain period.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! '{date_type}' Isn't the correct input to view the '{date_in_file}' of the products from the '{file_name.capitalize()[:-4]}' file within a certain period. Please enter 'other' or 'expiration'\
 to view the '{date_in_file}' within a certain period (not case sensitive).[/orange3]\n")

            continue
        break


    while True:
        from_date = input("Step 3 = Enter the 'from date' as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(from_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{from_date}' Isn't the correct way to fill in the 'from date'. Please enter the correct 'from' date as follows: dd-mm-yyyy.[/orange3]\n")

            continue
        break


    while True:
        until_date = input("Step 4 = Enter the 'until date' as follows dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(until_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{until_date}' Isn't the correct way to fill in the 'until date'. Please enter the correct 'until' date as follows: dd-mm-yyyy.[/orange3]\n")
        
            continue
        break    


    with open(file_name, 'r') as relevant_file:
        reader = csv.DictReader(relevant_file)
        print('\n')

        # Variables to select the correct relevant date in the relevant file.
        if file_name == 'inventory.csv' and date_type == 'other':
            relevant_date = 'purchase_date'

        elif file_name == 'sales.csv' and date_type == 'other':
            relevant_date = 'sales_date'

        elif file_name == 'losses.csv' and date_type == 'other':
            relevant_date = 'loss_date'
        
        if date_type == 'expiration':
            relevant_date = 'expiration_date'


        if date_type == 'other':
            rprint(F"[green]Great!:thumbs_up: Below you can see the search results of all the products with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' in the\
 '{file_name.capitalize()[:-4]}' file.[/green]\n")
            
        elif date_type == 'expiration':
            rprint(F"[green]Great!:thumbs_up: Below you can see the search results of all the products with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' in the\
 '{file_name.capitalize()[:-4]}' file.[/green]\n")

        relevant_date_list = []

        for categorize, row in enumerate(reader, start=1):
        
            input_date = convert_to_strptime(row[relevant_date]) # Met de 'convert_to_strptime(row[relevant_date])' code zorg ik er voor dat alle relevante datums waarover je itereerd worden omgezet naar een datetime object.
            
            input_from_date = convert_to_strptime(from_date)
            
            input_until_date = convert_to_strptime(until_date)
            
            if date_type == 'other' and input_from_date <= input_date and input_until_date >= input_date:
                relevant_date_list.append(row)
                rprint(F"{categorize}. {row}")
            
            elif date_type == 'expiration' and input_from_date <= input_date and input_until_date >= input_date:
                relevant_date_list.append(row)
                rprint(F"{categorize}. {row}")
        print('\n')
        
        if len(relevant_date_list) == 0: # Met deze 'if' statement geef je aan dat als een lijst leeg is, onderstaande moet gebeuren.
            rprint(F"[orange3]:scream: There were no products found with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' in the '{file_name.capitalize()[:-4]}' file.[/orange3]\n")

# print(view_products_within_period())
# print('\n')


'''
Algemene zoek-functie 'MET menu / input statements' voor het zoeken op 'product naam' en 'product id' in alle bestanden. DEZE CODE DOET HET PER MAANDAG 18-03-2024 ROND 19:45 UUR!!!
- Maandagavond 01-04-2024 rond 01:02 uur = Functie getest na de start van mijn taak: kolom- en bestandsnamen aanpassen (door ze korter te maken). En hij doet het nog prima!!!
- Vrijdagnacht 29-03-2024 rond 00:50 uur = Code aangepast en getest.
'''

def find_products():
    
    rprint("- Hello user, and welcome to the [bright_cyan]'find products'[/bright_cyan] option. You can search for a product in one of the following files: 'Inventory', 'Sales' or 'Losses'.\n")
    
    print("- Follow the step(s) below to find the product you are looking for. Have fun finding!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'find products in a selected file'")

    table.add_row("- Step 1 = Enter one of the following file names to find the product you are looking for: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Step 2 = Enter the product 'ID' or 'name' (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to find the product you are looking for: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")
            
            continue
        break
    

    while True:
        search_type = (input("Enter the product 'ID' or 'name' (the product name is not case sensitive): ")).lower()
        print('\n')
        
        if product_in_file_check(file_name, search_type) == True:
            rprint(F"[green]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' of product '{search_type}' above.[/green]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct product 'name' or 'ID' (the product name is not case sensitive).[/orange3]\n")
            
            continue
        break

# print(find_products())
# print('\n')


'''
Checken welke producten over 3 dagen niet meer houdbaar zijn. Deze code doet het per vrijdag 10-05-2024 rond 21:33 uur.
- Zondag 02-06-2024 rond 23:24 uur: Functie aangepast én getest na de start van mijn taak: kolom- en bestandsnamen\
  aanpassen (door ze korter te maken). En hij doet het nog prima!!! Ik heb een 2e 'if' statement toegevoegd om er voor\
  te zorgen dat wanneer er 'geen' producten zijn die over 3 dagen niet meer houdbaar zijn, de gebruiker een melding te\
  zien krijgt dat er geen producten zijn gevonden.
'''

def	avoid_expired_products():

    rprint("- Hello user, and welcome to the [bright_cyan]'avoid expired products'[/bright_cyan] option.\n")
    
    rprint("- [bright_cyan]Please follow the step(s) below every day to avoid expired products. In this way you can help our planet :globe_showing_Europe-Africa: by not wasting products and you can help people who are less fortunate.\
:handshake: Have fun in helping to make our world :globe_showing_Europe-Africa: a better place!:muscle:[/bright_cyan]\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'avoid expired products'")
        
    table.add_row("- Step 1 = Enter 'Y' for Yes if you 'do' or 'N' for No if you 'don't' want to check for products that will expire in 3 days (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        yes_or_no = input("Step 1 = Enter 'Y' for Yes if you 'do' or 'N' for No if you 'don't' want to check for products that will expire in 3 days (not case sensitive): ").lower()
        print('\n')

        if yes_or_no == "y":
            rprint("[green]Great!:thumbs_up: You can see all the products that will expire in 3 days below. Please think of a way not to waste these products. Thanks in advance for helping to make our world :globe_showing_Europe-Africa: a\
 better and durable place.:muscle: :thumbs_up: [red]:red_heart:[/red][/green]\n")

        elif yes_or_no == "n":
            rprint("[wheat1]Okay! The products that will expire in 3 days will not be shown.[/wheat1]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' isn't the correct input for checking the products that will expire in 3 days. Please Enter 'Y' for Yes if you 'do' or 'N' for No if you 'don't' want to check for products that\
 will expire in 3 days (not case sensitive).[/orange3]\n")

            continue
        break


    with open('inventory.csv', 'r') as inventory_file:
        reader = csv.DictReader(inventory_file)
        rows = list(reader)

        avoid_waste_list = []
        
        for categorize, row in enumerate(rows, start=2):

            today_date = current_date()
            
            expire_date = convert_to_strptime(row['expiration_date'])
            
            day_after_tomorrow = today_date + timedelta(2)
            
            expire_days = today_date + timedelta(3)
            
            if yes_or_no == 'y' and expire_date > day_after_tomorrow and expire_date <= expire_days:
                avoid_waste_list.append(row)
                rprint(F" {categorize}. {row}\n")

        if len(avoid_waste_list) == 0 and yes_or_no == 'y':
            rprint(F"There are no products found that will expire in 3 days. [green]So good job on helping to make the world :globe_showing_Europe-Africa: a better and durable place.:thumbs_up: :muscle: [red]:red_heart:[/red][/green]\n")
                
# print(avoid_expired_products())
# print('\n')


# User functions – add or remove products.

'''
Product toevoegen of de producthoeveelheid aanpassen in inventory bestand indien product 'id',
'naam' en 'houdbaarheidsdatum' overeenkomen. DEZE CODE DOET HET PER WOENSDAG 24-01-2024!!!

- Woensdag 08-05-2024 en donderdagnacht 09-05-2024 rond 01:32 uur = Functie toch nog aangepast omdat ik een nieuwe functie heb\
  toegevoegd aan mijn datum functies: 'convert_to_strftime(string)'. Hierdoor ben ik weer al mijn functies gaan nalopen\
  waar ik de 'datetime' objecten gebruik zodat ik de functies netter kan maken.
- Dinsdagavond 02-04-2024 rond 20:22 uur = Functie getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen\
  (door ze korter te maken)'. En hij doet het nog prima!!!
- Donderdag 21-03-2024 rond 22:56 uur = Functie aangepast.
- Vrijdag 22-03-2024 rond 19:45 uur = Functie wederom getest.

LET OP!!! Ik heb per vrijdag 22-03-2024 besloten om de kolomnamen aan te passen, dus daarna moet ik deze én alle andere\
functies nog een keer testen :-(.
'''

def add_inventory_products():
    
    rprint("- Hello user, and welcome to the [bright_cyan]'add inventory products'[/bright_cyan] option.\n")
    
    print("- Follow the step(s) below to add products to the Inventory file. Have fun adding!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'add products to the Inventory file'")
        
    table.add_row("- Step 1 = Enter the product 'ID'.")
    table.add_row("- Step 2 = Enter the product 'name'.")
    table.add_row("- Step 3 = Enter the product 'purchase quantity'.")
    table.add_row("- Step 4 = Enter the product 'purchase amount' and use a dot in stead of a comma to seperate any decimals.")
    table.add_row("- Step 5 = Enter the product 'purchase date' as follows: dd-mm-yyyy.")
    table.add_row("- Step 6 = Enter the product 'expiration date' as follows: dd-mm-yyyy.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    maximum_digits = '15'

    while True:
        id = (input("Step 1 = Enter the product 'ID': "))
        
        try:
            int(id)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The product 'ID' can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product 'ID' that only contains numbers.[/orange3]\n")
            
            continue

        if len(id) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'ID' can't contain more than '{maximum_digits}' digits. The entered ID: '{id}', contains more than '{maximum_digits}' digits. Please enter an 'ID' that contains no more than\
 '{maximum_digits}' digits.[/orange3]\n")

            continue
        
        print('\n')
        id_check = product_in_file_check('inventory.csv', id)
        
        if id_check == True:
            rprint(F"[wheat1]:thinking_face: Please note that product ID '{id}' already exists in the 'Inventory' file. You can see the 'product details' of the existing product ID '{id}' above.[/wheat1]\n")
        break   # Deze 'break' statement staat nu 1 'tab' / 'indent' naar links waardoor je de gehele 'while loop' stopt, want het staat dan ook buiten de 'if' statement. En dat is in deze functie geen probleem omdat je verder niks doet met\
                # de variabel 'id_check'. Je kan deze 'break' statement ook 1 tab / indent naar rechts plaatsen en dan stopt de 'while loop' alleen wanneer bovenstaande conditie (dus de variabel 'id_check') 'True' is. Dat is hier dus niet\
                # nodig omdat je dus verder niks doet met de variabel 'id_check'.


    while True:
        name = input(F"Step 2 = Enter the 'name' for product ID '{id}' (not case sensitive): ").lower()

        print('\n')
        name_check = product_in_file_check('inventory.csv', name)
        
        if name_check == True:
            rprint(F"[wheat1]:thinking_face: Please note that product name '{name}' already exists in the 'Inventory' file. You can see the 'product details' of the existing product name '{name}' above.'[/wheat1]\n")
        break


    while True:
        purchase_quantity = input(F"Step 3 = Enter the 'purchase quantity' for product '{name}': ")
        
        try:
            int(purchase_quantity)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'purchase quantity' for product '{name}' can only contain numbers. '{purchase_quantity}' Doesn't only contain numbers. Please enter the correct 'purchase quantity' for product\
 '{name}'.[/orange3]\n")            
            
            continue

        if len(purchase_quantity) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'purchase quantity' can't contain more than '{maximum_digits}' digits. The entered 'purchase quantity': '{purchase_quantity}', contains more than '{maximum_digits}' digits. Please enter\
 a 'purchase quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n")

            continue
        break      


    while True:
        purchase_amount = input(F"Step 4 = Enter the 'purchase amount' for product '{name}' and use a dot in stead of a comma to seperate any decimals: ")
        
        try:
            float(purchase_amount)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{purchase_amount}' Doesn't contain an 'amount' or a 'dot' to seperate the decimals. Please enter the correct 'purchase amount' for product '{name}' and use a dot (in stead of a comma) to\
 seperate any decimals.[/orange3]\n")

            continue

        input_amount = float(purchase_amount)
        decimal_quantity = round(input_amount, 2)

        if input_amount != decimal_quantity:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'purchase amount' again and only add '2 decimals' when necessary.[/orange3]\n")

            continue

        elif len(purchase_amount) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'purchase amount' can't contain more than '{maximum_digits}' digits. The entered 'purchase amount': '{purchase_amount}', contains more than '{maximum_digits}' digits. Please enter a\
 'purchase amount' that contains no more than '{maximum_digits}' digits.[/orange3]\n")
            
            continue
        break


    while True:
        purchase_date = input(F"Step 5 = Enter the 'purchase date' for product '{name}' as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(purchase_date)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{purchase_date}' Isn't the correct way to fill in the 'purchase date'. Please enter the correct 'purchase date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        
        input_date = convert_to_strptime(purchase_date)

        if input_date > current_date():
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The date you just entered: '{purchase_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'purchase date' for product '{name}'.\n\
[/orange3]")

            continue
        break

    # The 3 variables below are to create the 'tomorrow_date' variable which is a notification code for when the expiration date of a product is tomorrow. This will help the user to avoid wasting products. See the 1st 'elif statement' in\
    # 'step 6' below.
    today_date = current_date()
    
    calculate_tomorrow = today_date + timedelta(1)          # Met de 'calculate_tomorrow' variabel tel ik 1 dag op bij de huidige datum. LET OP!!! Beide variabelen zijn datetime objecten en dat is nodgi om te kunnen rekeken met de datums.
    
    tomorrow_date = convert_to_strftime(calculate_tomorrow) # Met de 'tomorrow_date' variabel zet ik 'calculate_tomorrow' variabel om naar een string zodat ik deze bij de input statement van stap 6 hieronder (dat ook een string is) kan\
                                                            # gebruiken om de nodige vergelijking te kunnen maken.
    while True:
        expiration_date = input(F"Step 6 = Enter the 'expiration date' for product '{name}' as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(expiration_date)
        
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date'. Please enter the correct 'expiration date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        
        expiration = convert_to_dutch_date(expiration_date)     # Met de 'expiration' variabel zet ik de 'expiration_date' variabel (dat dus ook de input statement van stap 6 is) om naar de Nederlandse datum format.

        if expiration < current_date().strftime("%d-%m-%Y"):    # Met de '.strftime("%d-%m-%Y")' code zet ik mijn 'current_date()' functie (dat geen string is) om naar een string. Dit is nodig om de vergelijking met de 'input_date' variabel\
            print('\n')                                         # (dat ook een string is) te kunnen maken. En met de '.strftime("%d-%m-%Y")' code erachter wordt de datum format de Nederlandse datum format.
            rprint(F"[orange3]:scream: Hello user! Product '{name}' is rotton.:scream: So please throw it away a.s.a.p. or enter the correct expiration date for product '{name}'.[/orange3]\n")
            
            continue # Als bovenstaande 'if' statement / conditie 'True' is blijf je door de 'continue' statement in de loop hangen. En wanneer die 'False' is, ga je door naar de volgende stap.
        
        elif expiration == current_date().strftime("%d-%m-%Y"):
            print('\n')
            rprint(F"[wheat1]:astonished_face: Hello user! The 'expiration date' of product '{name}' is today.:astonished_face: So you can either: 1: enter the correct expiration date, 2: put it on sale or 3: think of a durable way to do\
something with product '{name}'.[/wheat1]")        

        elif expiration == tomorrow_date:
            print('\n')
            rprint(F"[wheat1]:thinking_face: Hello user! The 'expiration date' of product '{name}' is tomorrow.:thinking_face: So you can either: 1: enter the correct expiration date, 2: put it on sale or 3: think of a durable way to do\
something with product '{name}'.[/wheat1]")

        break


    product_details = {
        'id': id,
        'name' : name,
        'purchase_quantity' : purchase_quantity,
        'purchase_amount': purchase_amount,
        'purchase_date' : purchase_date,
        'expiration_date' : expiration_date,
        }

    with open('inventory.csv', 'r', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows:
            if row['id'] == id and row['name'] == name and row['purchase_amount'] and row['purchase_date'] and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) + int(purchase_quantity)
                
                already_exists = True
                break

            else:
                already_exists = False

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        
        if already_exists == True:
            writer.writerows(rows)                  # 'Writerow' verwacht een dictionary en kijkt naar de key (op de achtergrond). 'Writerows' doet eigenlijk hetzelfde, maar die kijkt naar de iterabele.
            print('\n')                        
            rprint(F"[green]Great!:thumbs_up: The quantity of product '{name}' has been updated, because the 'ID', the 'name', the 'purchase amount', 'the purchase date' and the 'expiration date' are the same. You can check the 'product\
 details' below.[/green]\n")
            rprint(F"[bright_cyan]{row}[/bright_cyan]")
            print('\n')

        else:
            with open('inventory.csv', 'a+', newline='') as inventory_file:
                writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)    # 'Writerow' verwacht een dictionary en kijkt naar de key (op de achtergrond). 'Writerows' doet eigenlijk hetzelfde, maar die kijkt naar de iterabele.

                print('\n')
                rprint(F"[green]Great!:thumbs_up: Product '{name}' has been added to the 'Inventory' file. You can check the 'product details' below.[/green]\n")
                rprint(F"[bright_cyan]{product_details}[/bright_cyan]")
                print('\n')

# print(add_inventory_products())
# print('\n')


'''
Sold products. DEZE CODE DOET HET!!! Ik heb deze functie aangepast en getest op zaterdagnacht 23-03-2024 rond 01:05 uur.
- Zaterdagnacht 06-04-2024 rond 01:53 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
'''

def add_sold_products():

    rprint("- Hello user, and welcome to the [bright_cyan]'add sold products'[/bright_cyan] option.\n")
    
    print("- By adding a sold product to the 'Sales' file, your 'Inventory' file will automatically be reduced with the same quantity of the products that you've sold.\n")
    
    print("- Follow the step(s) below to add your sold products. Have fun adding!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'add sold products to the Sales file'")
        
    table.add_row("- Step 1 = Enter the product 'ID'.")
    table.add_row("- Step 2 = Enter the product 'name'.")
    table.add_row("- Step 3 = Enter the product 'sold quantity'.")
    table.add_row("- Step 4 = Enter the product 'sales amount' and use a dot in stead of a comma to seperate any decimals.")
    table.add_row("- Step 5 = Enter the product 'sales date' as follows: dd-mm-yyyy.")
    table.add_row("- Step 6 = Enter the product 'expiration date' as follows: dd-mm-yyyy.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    maximum_digits = '15'

    while True:
        id = (input("Step 1 = Enter the product 'ID': "))
        
        try:
            int(id)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The product 'ID' can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product 'ID' that only contains numbers.[/orange3]\n")
            
            continue 
        
        print('\n')
        if product_in_file_check('inventory.csv', id) == True:
            rprint(F"[green]Great!:thumbs_up: Product ID '{id}' matches the product 'ID' of this product in the 'Inventory' file. You can see the 'product details' of product ID '{id}' from the 'Inventory' file above.[/green]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! The entered product ID: '{id}', was not found in the 'Inventory' file. You can only add a 'sold product' to the 'Sales' file if this product is also found in the 'Inventory' file. Please\
 enter the correct product 'ID'.[/orange3]\n")

            continue
        break 


    print('\n')
    product_in_file_check('inventory.csv', id)

    while True:
        name = (input("Step 2 = Enter the product 'name' as shown above in the 'product details' (not case sensitive): ")).lower()
        print('\n')

        if name in product_detail_check('inventory.csv', id, 'name'):
            product_in_file_check('inventory.csv', name)
            rprint(F"[green]Great!:thumbs_up: Product name '{name}' matches with the product ID '{id}' of this product in the 'Inventory' file. You can see the 'product details' of product '{name}' from the 'Inventory' file above.[/green]\n")

        else:
            product_in_file_check('inventory.csv', id)
            rprint(F"[orange3]:scream: Hello user! The entered product 'name': '{name}', doesn't match with the product ID '{id}' of this product in the 'Inventory' file. You can only add a 'sold product' to the 'sales' file if the product\
 'name' matches the name of this product in the 'Inventory' file. Please check the 'product details' above for the correct product 'name' for product ID '{id}'.[/orange3]\n")

            continue
        break


    while True:
        sold_quantity = (input(F"Step 3 = Enter the 'sold quantity' of product '{name}': "))

        try:
            int(sold_quantity)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'sold quantity' can only contain numbers. '{sold_quantity}' Doesn't only contain numbers. Please enter the correct 'sold quantity' for product '{name}'.[/orange3]\n")
            
            continue

        if len(sold_quantity) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'sold quantity' can't contain more than '{maximum_digits}' digits. The entered 'sold quantity': '{sold_quantity}', contains more than '{maximum_digits}' digits. Please enter a 'sold\
 quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n")
        
            continue
        break  


    while True:
        sales_amount = (input(F"Step 4 = Enter the 'sales amount' of product '{name}' and use a dot in stead of a comma to seperate any decimals: "))

        try:
            float(sales_amount)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{sales_amount}' Doesn't contain an 'amount' or a 'dot' to seperate the decimals. Please enter the correct 'sales amount' for product '{name}' and use a 'dot' (in stead of a comma) to\
 seperate any decimals.[/orange3]\n")

            continue
        
        input_amount = float(sales_amount)
        decimal_quantity = round(input_amount, 2)

        if input_amount != decimal_quantity:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'sales amount' again and only add '2 decimals' when necessary.[/orange3]\n")

            continue

        elif len(sales_amount) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'sales amount' can't contain more than '{maximum_digits}' digits. The entered 'sales amount': '{sales_amount}', contains more than '{maximum_digits}' digits. Please enter a 'sales\
 amount' that contains no more than '{maximum_digits}' digits.[/orange3]\n")        

            continue
        break


    while True:
        sales_date = (input(F"Step 5 = Enter the 'sales date' of product '{name}' as follows: dd-mm-yyyy: "))

        try:
            convert_to_dutch_date(sales_date)
        
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{sales_date}' Isn't the correct way to fill in the 'sales date'. Please enter the correct 'sales date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        
        input_date = convert_to_strptime(sales_date)    # Met de variabel 'input_date' maak ik van mijn variabel 'sales_date' een datetime object. Dit omdat het aan het begin van deze while loop (dus bij de 'try' code) niet opgeslagen wordt als\
                                                        # als een datetime object.
        if input_date > current_date():
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'sales date' you just entered: '{sales_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'sales date' for product '{name}'.\n\
 [/orange3]")

            continue
        break


    print('\n')
    product_in_file_check('inventory.csv', name)

    while True:
        expiration_date = (input(F"Step 6 = Enter the 'expiration date' of product '{name}' as shown above in the 'product details' as follows: dd-mm-yyyy: "))

        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date'. Please enter the correct 'expiration date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue
        
        expiration = convert_to_dutch_date(expiration_date)
        
        expiration_date_check = product_detail_check('inventory.csv', name, 'expiration_date')

        if expiration_date in expiration_date_check:
            print('\n')
            product_in_file_check('inventory.csv', name)
            rprint(F"[green]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{name}' in the 'Inventory file'. You can see all the 'expiration dates' of product '{name}'\
 in the 'product details' shown above.[/green]\n")

            if expiration == current_date().strftime("%d-%m-%Y"):   # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement. LET OP!!! Door de '.strftime("%d-%m-%Y")' method / code achter mijn 'current_date()' functie te plaatsen zorg ik ervoor dat het 'tijdstip' van mijn\
                                                                    # 'current_date()' functie niet zichtbaar is én dat de Nederlandse datum volgorde wordt gehanteerd.
                rprint(F"[wheat1]:astonished_face: Please note that the entered expiration date '{expiration_date}' of the sold product with product ID '{id}' and product name '{name}' is today.:astonished_face:[/wheat1]")

            if expiration < current_date().strftime("%d-%m-%Y"):    # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement. LET OP!!! Door de '.strftime("%d-%m-%Y")' method / code achter mijn 'current_date()' functie te plaatsen zorg ik ervoor dat het 'tijdstip' van mijn\
                                                                    # 'current_date()' functie niet zichtbaar is én dat de Nederlandse datum volgorde wordt gehanteerd.
                rprint(F"[wheat1]:scream: Please note that the entered expiration date '{expiration_date}' of the sold product with product ID '{id}' and product name '{name}' has expired.:scream:[/wheat1]")

        else:
            print('\n')
            product_in_file_check('inventory.csv', name)
            rprint(F"[orange3]:scream: Hello user! The entered expiration date: '{expiration_date}', doesn't match one of the 'expiration dates' of product '{name}' in the 'Inventory file'. Please check the 'product details' above for the\
 correct 'expiration date'.[/orange3]\n")

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

    with open('sales.csv', 'r+', newline='') as sales_file:
        writer = csv.DictWriter(sales_file, fieldnames= reader.fieldnames)
        
        if already_exists == True:
            writer.writerows(rows)
            print('\n')
            rprint(F"[green]Great!:thumbs_up: The 'sold quantity' of product '{name}' has been 'updated', because: the 'ID', the 'name', the 'sales amount' the 'sales date' and the 'expiration date' are the same. You can check the updated\
 details below.[/green]\n")            
            rprint(F"[bright_cyan]{row}[/bright_cyan]")
            print('\n')
            
        else:    
            with open('sales.csv', 'a+', newline='') as sales_file:
                writer = csv.DictWriter(sales_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)
                print('\n')
                rprint(F"[green]Great!:thumbs_up: Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the 'sales' file. You can check the details below.[/green]\n")
                rprint(F"[bright_cyan]{product_details}[/bright_cyan]")
                print('\n')


    with open('inventory.csv', 'r+', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows[1:]: # De index code '[1:]' zorgt ervoor dat de for loop gaat loopen vanaf 'de eerste regel' waar data in staat en dus niet vanaf de 'header' / de 'kolomnamen'. 
            
            if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) - int(sold_quantity)   # Omdat ik op deze regel de dictonary ['purchase_quantity'] al heb gecast naar een 'integer' / 'int' binnen de for loop, hoef ik dat in\
                                                                                                # onderstaande 'indented' / 'getabte' 'if' statements niet meer te doen omdat Python dit onthoudt. LET OP!!! Ik heb de 'break' statement aan\
                                                                                                # het einde van deze for loop uitgecommentarieerd omdat Python anders alleen het eerste product die gevonden wordt in het csv bestand aanpast.\
                if row['purchase_quantity'] >0 and row['purchase_quantity'] < 3:                # Dit omdat er met deze 'if' statement alleen maar wordt gekeken of het 'id', de 'naam' en de 'houdbaarheidsdatum' hetzelfde zijn. Dus als er\
                                                                                                # meerdere producten zijn met hetzelfde 'id', 'naam' en 'houdbaarheidsdatum', dan zouden die niet worden aangepast met deze 'if' statement.
                    rprint(F"[orange3]STOCK UPDATE!!!:astonished_face: The product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there are / is\
 '{row['purchase_quantity']}' left in stock.:astonished_face:[/orange3]\n")

                elif row['purchase_quantity'] <= 0:
                        row['purchase_quantity'] = 0
                        rprint(F"[orange3]STOCK UPDATE!!!:scream: Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there is '{row['purchase_quantity']}'\
 / 'nothing' left in stock.:scream:[/orange3]\n")
        
        # print(type(row['purchase_quantity'])) # LET OP!!! Bij bovenstaande 'if' statement kreeg ik eerst 2 foutmeldingen: 1= TypeError: '<=' not supported between instances of 'str' and 'int'. 2= ValueError: invalid literal for int() with\
                                                # base 10: 'purchase_quantity'. Deze foutmeldingen werden o.a. veroorzaakt doordat ik de code '(row['purchase_quantity']))' had gecast in een integer terwijl dit al een integer was. Door het\
                                                # gebruik van dit soort print statements (dus door de 'type' ervoor te zetten) kan je als programmeur ook achterhalen wat de mogelijke oorzaak is van een foutmelding én hoe je dit vervolgens\
                                                # kunt oplossen. De output van deze print statement was namelijk '<class 'int'>', waardoor je dus weet dat het casten naar een integer niet nodig is omdat de key van de dictionary al een\
                                                # integer is. Zie voor meer uitleg over deze code mijn Excel doc.: Foutmeldingen inc. oplossingen.
                else:
                    rprint(F"[green]STOCK UPDATE!!!:thumbs_up: Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' doesn't need to be reordered, because there are '{(row['purchase_quantity'])}'\
 left in stock.:grinning_face_with_big_eyes:[/green]\n")
                # break

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        writer.writerows(rows)
        
# print(add_sold_products())
# print('\n')


'''
DEZE CODE DOET HET PER VRIJDAG 15-03-2024!!!
- Maandagavond 02-04-2024 rond 23:17 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!

Losses / verlies producten toevoegen of de producthoeveelheid aanpassen in het losses bestand én het inventory\
bestand indien product 'id', 'naam', 'houbaarheidsdatum', 'verlies datum', 'oorzaak verlies', 'verlies bedrag'\
overeenkomen. LET OP!!! Ik heb deze functie aangepast én weer getest op maandagnacht 25-03-2024 rond 00:44 uur.
'''

def add_loss_products():

    rprint("- Hello user, and welcome to the [bright_cyan]'add product losses'[/bright_cyan] option.\n")

    print("- By adding a product loss to the Losses file, the Inventory file will automatically be reduced with the same quantity of the added product loss.\n")

    print("- Follow the step(s) below to add a product loss. Have fun adding!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'add products to the Losses file'")
        
    table.add_row("- Step 1 = Enter the product 'ID'.")
    table.add_row("- Step 2 = Enter the product 'name' (not case sensitive).")
    table.add_row("- Step 3 = Enter the product 'loss quantity'.")
    table.add_row("- Step 4 = Enter the product 'loss amount' and use a dot in stead of a comma to seperate any decimals.")
    table.add_row("- Step 5 = Enter the product 'loss date' as follows: dd-mm-yyyy.")
    table.add_row("- Step 6 = Enter one of the following 'causes of loss': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).")
    table.add_row("- Step 7 = Enter the product 'expiration date' as follows: dd-mm-yyyy.")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    maximum_digits = '15'

    while True:
        id = (input("Step 1 = Enter the product 'ID': "))
        print('\n')

        try:
            int(id)
            
        except ValueError:
            rprint(F"[orange3]:scream: Hello user! The product 'ID' can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product 'ID' that only contains numbers.[/orange3]\n")
            
            continue

        if product_in_file_check('inventory.csv', id) == True:
            rprint(F"[green]Great!:thumbs_up: Product ID '{id}' matches the product 'ID' of this product in the 'Inventory' file. You can see the 'product details' of product ID '{id}' from the 'Inventory' file above.[/green]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! The entered product ID: '{id}', was not found in the 'Inventory' file. You can only add a 'loss product' to the 'Losses' file if this product is also found in the 'Inventory' file. Please\
 enter the correct product 'ID'.[/orange3]\n")

            continue
        break 


    print('\n')
    product_in_file_check('inventory.csv', id)

    while True:
        name = (input("Step 2 = Enter the product 'name' as shown above in the 'product details' (not case sensitive): ")).lower()
        print('\n')

        if name in product_detail_check('inventory.csv', id, 'name'):
            product_in_file_check('inventory.csv', name)
            rprint(F"[green]Great!:thumbs_up: Product name '{name}' matches with the product ID '{id}' of this product in the 'Inventory' file. You can see the 'product details' of product '{name}' from the 'Inventory' file above.[/green]\n")

        else:
            product_in_file_check('inventory.csv', id)
            rprint(F"[orange3]:scream: Hello user! The entered product name: '{name}', doesn't match with the product ID '{id}' of this product in the 'Inventory' file. You can only add a 'loss product' to the 'Losses' file if the product\
 'name' matches the name of this product in the 'Inventory' file. Please check the 'product details' above for the correct product 'name' for product ID '{id}'.[/orange3]\n")

            continue
        break


    while True:
        loss_quantity = (input(F"Step 3 = Enter the 'loss quantity' of product '{name}': "))
        
        try:
            int(loss_quantity)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'loss quantity' can only contain numbers. '{loss_quantity}' Doesn't only contain numbers. Please enter the correct 'loss quantity' for product '{name}'.[/orange3]\n")
            
            continue

        if len(loss_quantity) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'loss quantity' can't contain more than '{maximum_digits}' digits. The entered 'loss quantity': '{loss_quantity}', contains more than '{maximum_digits}' digits. Please enter a 'loss\
 quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n")
            
            continue
        break  


    while True:
        loss_amount = (input(F"Step 4 = Enter the 'loss amount' of product '{name}' and use a dot (in stead of a comma) to seperate any decimals: "))
        
        try:
            float(loss_amount)

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{loss_amount}' Doesn't contain an 'amount' and / or a 'dot' to seperate the decimals. Please enter the correct 'loss amount' for product '{name}' and use a 'dot' (in stead of a comma) to\
 seperate any decimals.[/orange3]\n")
            continue

        input_amount = float(loss_amount)
        decimal_quantity = round(input_amount, 2)
        
        if input_amount != decimal_quantity:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'loss amount' again and only add '2 decimals' when necessary.[/orange3]\n")
            
            continue

        elif len(loss_amount) > 15:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The 'loss amount' can't contain more than '{maximum_digits}' digits. The entered 'loss amount': '{loss_amount}', contains more than '{maximum_digits}' digits. Please enter a 'loss amount'\
 that contains no more than '{maximum_digits}' digits.[/orange3]\n")        

            continue
        break


    while True:
        loss_date = (input(F"Step 5 = Enter the 'loss date' of product '{name}' as follows: dd-mm-yyyy: "))
        
        try:
            convert_to_dutch_date(loss_date) # LET OP!!! Omdat ik hier 'nog' geen vergelijking ga maken, hoef ik de datum nog niet om te zetten naar 'strptime'.

        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user. '{loss_date}' Isn't the correct way to fill in the 'loss date'. Please enter the correct 'loss date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue

        input_date = convert_to_strptime(loss_date) # LET OP!!! Hier ga ik wel een vergelijking maken en daarom zet ik de datum hier wel om naar 'strptime'.

        if input_date > current_date():
            print('\n')
            rprint(F"[orange3]:scream: Hello user. The date you just entered: '{loss_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'loss date' for product '{name}'.[/orange3]\n")
        
            continue
        break


    while True:
        loss_cause = (input(F"Step 6 = Enter one of the following 'causes of loss' options for product '{name}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive): ")).lower()
        
        loss_cause_options = ['broken', 'damaged', 'expired', 'missing', 'theft', 'other']

        if loss_cause in loss_cause_options:
            print('\n')
            rprint(F"[green]Great!:thumbs_up: '{loss_cause.capitalize()}' is a correct 'cause of loss'.[/green]\n")

        else:
            print('\n')
            rprint(F"[orange3]:scream: Hello user. The 'cause of loss' you just entered: '{loss_cause}', isn't a correct 'cause of loss' option in the 'Losses' file. Please enter one of the following 'causes of loss' for product '{name}':\
 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).[/orange3]\n")

            continue
        break


    print('\n')
    product_in_file_check('inventory.csv', name)
    
    while True:
        expiration_date = (input(F"Step 7 = Enter the 'expiration date' of product '{name}' as shown above in the 'product details' as follows: dd-mm-yyyy: "))
        
        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date' for product '{name}'. Please enter the correct 'expiration date' for product '{name}' as follows:\
 dd-mm-yyyy.[/orange3]\n")
        
            continue
        
        expiration = convert_to_dutch_date(expiration_date)

        expiration_date_check = product_detail_check('inventory.csv', name, 'expiration_date')  # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven\
                                                                                                # ingevulde variabel: 'search_type' dat het door de gebruiker ingevulde product is.
        
        if expiration_date in expiration_date_check:    # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn variabel 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'product_detail_check' functie\
                                                        # dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te gebruiken\
                                                        # i.p.v. de '==' operator, want met de 'in' operator kijk je of iets 'wel' of 'niet' in een lijst zit.
            print('\n')
            product_in_file_check('inventory.csv', name)
            rprint(F"[green]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{name}' in the 'Inventory' file. You can see all the 'expiration dates' of product '{name}'\
 in the 'product details' shown above.[/green]\n")
            
            if expiration == current_date().strftime("%d-%m-%Y"):   # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement. LET OP!!! Door de '.strftime("%d-%m-%Y")' method / code achter mijn 'current_date()' functie te plaatsen zorg ik ervoor dat het 'tijdstip' van mijn\
                                                                    # 'current_date()' functie niet zichtbaar is én dat de Nederlandse datum volgorde wordt gehanteerd.
                rprint(F"[wheat1]:astonished_face: Please note that the entered expiration date '{expiration_date}' of the loss product with product ID '{id}' and product name '{name}' is today.:astonished_face:[/wheat1]")

            if expiration < current_date().strftime("%d-%m-%Y"):    # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement. LET OP!!! Door de '.strftime("%d-%m-%Y")' method / code achter mijn 'current_date()' functie te plaatsen zorg ik ervoor dat het 'tijdstip' van mijn\
                                                                    # 'current_date()' functie niet zichtbaar is én dat de Nederlandse datum volgorde wordt gehanteerd.
                rprint(F"[wheat1]:scream: Please note that the entered expiration date '{expiration_date}' of the loss product with product ID '{id}' and product name '{name}' has expired.:scream:[/wheat1]")
            
        else:
            print('\n')
            product_in_file_check('inventory.csv', name)
            rprint(F"[orange3]:scream: Hello user! The entered expiration date: '{expiration_date}', doesn't match with one of the 'expiration dates' of product '{name}' in the 'Inventory' file. Please check the 'product details' above for\
 the correct 'expiration date'.[/orange3]\n")

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

    with open('losses.csv', 'r+', newline='') as losses_file:
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
            print('\n')
            rprint(F"[green]Great!:thumbs_up: The 'loss quantity' of product '{name}' has been 'updated', because the 'ID', the 'name', the 'loss amount', the 'loss date', the 'cause of loss' and the 'expiration date' are the same. You can\
 check the updated details below.[/green]\n")
            rprint(F"[bright_cyan]{row}[/bright_cyan]")
            print('\n')

        else:
            with open('losses.csv', 'a+', newline='') as losses_file:
                writer = csv.DictWriter(losses_file, fieldnames= reader.fieldnames)
                writer.writerow(product_details)
                print('\n')
                rprint(F"[green]Great!:thumbs_up: Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the 'Losses' file. You can check the details below.[/green]\n")
                rprint(F"[bright_cyan]{product_details}[/bright_cyan]")
                print('\n')

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
        rows = list(reader)
        
        for row in rows[1:]: # De index code '[1:]' zorgt ervoor dat de 'for loop' gaat loopen vanaf 'de eerste regel' waar data in staat en dus niet vanaf de 'header' / de 'kolomnamen'. 
            
            if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                row['purchase_quantity'] = int(row['purchase_quantity']) - int(loss_quantity)
                
                if row['purchase_quantity'] >0 and row['purchase_quantity'] < 3: # If the quantity of a product is 5 or less, it will trigger the print statement shown below.
                    rprint(F"[orange3]STOCK UPDATE!!!:astonished_face: The product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there are / is\
 '{row['purchase_quantity']}' left in stock.:astonished_face:[orange3]\n")

                elif row['purchase_quantity'] <= 0: # Met deze code / 'elif statement' geef je aan dat als een berekening onder de nul / 0 uit komt, de berekening nul / 0 moet blijven.
                        row['purchase_quantity'] = 0
                        rprint(F"[orange3]STOCK UPDATE!!!:scream: Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' needs to be reordered, because there is '{row['purchase_quantity']}'\
 / 'nothing' left in stock.:scream:[/orange3]\n")
        
        # print(type(row['purchase_quantity'])) # LET OP!!! Bij bovenstaande 'if' statement kreeg ik eerst 2 foutmeldingen: 1= TypeError: '<=' not supported between instances of 'str' and 'int'. 2= ValueError: invalid literal for int() with\
                                                # base 10: 'purchase_quantity'. Deze foutmeldingen werden o.a. veroorzaakt doordat ik de code '(row['purchase_quantity']))' had gecast in een integer terwijl dit al een integer was. Door het\
                                                # gebruik van dit soort print statements (dus door de 'type' ervoor te zetten) kan je als programmeur ook achterhalen wat de mogelijke oorzaak is van een foutmelding én hoe je dit vervolgens\
                                                # kunt oplossen. De output van deze print statement was namelijk '<class 'int'>', waardoor je dus weet dat het casten naar een integer niet nodig is omdat de key van de dictionary al een\
                                                # integer is. Zie voor meer uitleg over deze code mijn Excel doc.: Foutmeldingen inc. oplossingen.
                else:
                    rprint(F"[green]STOCK UPDATE!!!:thumbs_up: Product '{row['name']}' with product id '{row['id']}' and expiration date '{row['expiration_date']}' doesn't need to be reordered, because there are '{(row['purchase_quantity'])}'\
 left in stock.:grinning_face_with_big_eyes:[/green]\n")
                # break

    with open('inventory.csv', 'r+', newline='') as inventory_file:
        writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
        writer.writerows(rows)

# print(add_loss_products())
# print('\n')


# User functions – modify product details.


'''
Wijzigen van de productdetails. Begonnen op maandag 26-02-2024. DEZE FUNCTIE DOET HET VOLLEDIG PER WOENSDAG 13-03-2024.
- Dinsdag 28-05-2024 rond 16:03 uur = Mijn aangepaste functie 'show_product_details() toegevoegd aan deze functie én deze functie weer getest\
  nadat ik ook mijn 'product_in_file_check()' functie heb aangepast. Daarnaast ook nog wat tekstuele aanpassingen gedaan in deze functie.
- Dinsdag 30-04-2024 rond 16:17 uur = Nog wat tekstuele aanpassingen gedaan in deze functie zodat de zinnen bij de stappen meer uniform zijn.
- Maandag 29-04-2024 rond 21:59 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen\
  (door ze korter te maken)'. En hij doet het nog prima!!!
- Woensdag 27-03-2024 rond 23:10 uur = Witregels '("\n") aangepast en deze functie gekopieerd naar mijn Superpy document.
- Zondag 24-03-2024 rond 15:26 uur = Functie opnieuw gecheckt n.a.v. de houbaarheidsdatum check die ik heb aangepast bij vraag 3.
'''

def modify_product_details():

    rprint("- Hello user, and welcome to the [bright_cyan]'modify product details'[/bright_cyan] option.\n")

    print("- Follow the step(s) below to modify the details of a product in a selected file. Have fun modifying!\n")
    
    rprint("-[bright_magenta] Note 1! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    rprint("-[bright_magenta] Note 2! Step 5a will only appear when you select the 'Losses' file.[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'modify the product details in a selected file'")
        
    table.add_row("- Step 1 = Enter one of the following file names to modify a product detail: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    table.add_row("- Step 2 = Enter the current 'ID' or 'name' of the product that you want to modify (the product name is not case sensitive)")
    table.add_row("- Step 3 = Enter the current product 'quantity'.")
    table.add_row("- Step 4 = Enter the current product 'relevant amount' (for instance 'purchase amount' or 'sales amount' etc.) and use a dot to seperate any decimals.")
    table.add_row("- Step 5 = Enter the current product 'relevant date' (for instance 'purchase date' or 'sales date' etc.) as follows: dd-mm-yyyy.")
    table.add_row("- Step 5a = Enter one of the following 'causes of loss': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).")
    table.add_row("- Step 6 = Enter the current product 'expiration date' as follows: dd-mm-yyyy.")
    table.add_row("- Step 7 = Enter the current product 'detail name' that you want to modify, for instance 'expiration date' etc. (not case sensitive and you don't have to use an underscore in the 'product detail name).")
    table.add_row("- Step 8 = Enter the 'modification' you want to make for the product (not case sensitive).")
    table.add_row("- Step 9 = Confirm if you 'do' or 'don't' want to modify the product detail by entering 'Y' for Yes or 'N' for No (not case sensitive).")
    table.add_row("- Done!")

    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names to modify a product detail: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
            
        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")
            
            continue
        break


    while True:
        search_type = input("Step 2 = Enter the current 'ID' or 'name' of the product that you want to modify (the product name is not case sensitive): ").lower()
        print('\n')

        if product_in_file_check(file_name, search_type) == True:
            rprint(F"[green]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' of product '{search_type}' above.[/green]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct current 'ID' or 'name' of the product (not case sensitive).[/orange3]\n")

            continue
        break


    # Names for the relevant 'quantity' in the relevant file for 'step 3' in the while loop below.
    relevant_quantity = ''
    
    if file_name == 'inventory.csv':
        relevant_quantity = 'purchase quantity'

    elif file_name == 'sales.csv':
        relevant_quantity = 'sold quantity'
    
    elif file_name == 'losses.csv':
        relevant_quantity = 'loss quantity'

    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        quantity = (input(F"Step 3 = Enter the current '{relevant_quantity}' of product '{search_type}' (as shown above in the 'product details') that you want to modify: "))
        print('\n')

        # 3 Variables to check for the relevant quantity of the product in the relevant file with my 'product_detail_check()' function.
        purchase_quantity_check = product_detail_check('inventory.csv', search_type, 'purchase_quantity')
        sold_quantity_check = product_detail_check('sales.csv', search_type, 'sold_quantity')
        loss_quantity_check = product_detail_check('losses.csv', search_type, 'loss_quantity')
        
        if file_name == 'inventory.csv' and quantity in purchase_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_quantity}': '{quantity}', matches one of the current '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can\
 see all the '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")

        elif file_name == 'sales.csv' and quantity in sold_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_quantity}': '{quantity}', matches one of the current '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can\
 see all the '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and quantity in loss_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_quantity}': '{quantity}', matches one of the current '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can\
 see all the '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered current '{relevant_quantity}': '{quantity}', doesn't match with one of the current '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}'\
 file. Please check the 'product details' of product '{search_type}' shown above for the correct current '{relevant_quantity}'.[/orange3]\n")

            continue
        break


    # Names for the relevant 'amount' in the relevant file for 'step 4' in the while loop below.
    relevant_amount = ''
    
    if file_name == 'inventory.csv':
        relevant_amount = 'purchase amount'

    elif file_name == 'sales.csv':
        relevant_amount = 'sales amount'
    
    elif file_name == 'losses.csv':
        relevant_amount = 'loss amount'

    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        input_amount = input(F"Step 4 = Enter the 'exact' current '{relevant_amount}' of product '{search_type}' including any decimals as shown above in the 'product details' and use a dot (instead of a comma) to seperate any decimals: ")
        print('\n')

        # 3 Variables to check for the relevant amount of the product in the relevant file with my 'product_detail_check()' function.
        purchase_amount_check = product_detail_check('inventory.csv', search_type, 'purchase_amount')
        sales_amount_check = product_detail_check('sales.csv', search_type, 'sales_amount')
        loss_amount_check = product_detail_check('losses.csv', search_type, 'loss_amount')

        if file_name == 'inventory.csv' and input_amount in purchase_amount_check:      # Ik heb deze code aangepast omdat ik de volgende foutmelding kreeg (en deze foutmelding kreeg ik ook bij stap 4): 'TypeError: argument of type\
            product_in_file_check(file_name, search_type)                               # 'NoneType' is not iterable'. Dit kwam omdat ik eerst met een 'if' statement moest aangeven dat de variabel 'file_name' gelijk moest zijn aan het\
                                                                                        # betreffende bestand én omdat ik in mijn oude code mijn input statement 'relevant_amount' niet in mijn if statement had verwerkt. En nu dus wel.
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_amount}': '{input_amount}', matches one of the current '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see\
 all the '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'sales.csv' and input_amount in sales_amount_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_amount}': '{input_amount}', matches one of the current '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see\
 all the '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and input_amount in loss_amount_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_amount}': '{input_amount}', matches one of the current '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see\
 all the '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered current '{relevant_amount}': '{input_amount}', doesn't match with one of the current '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file.\
 Please check the 'product details' of product '{search_type}' shown above for the 'exact' correct current '{relevant_amount}'.[/orange3]\n")

            continue
        break


    # Names for the relevant 'date' in the relevant file for 'step 5' in the while loop below.
    relevant_date = ''

    if file_name == 'inventory.csv':
        relevant_date = 'purchase date'
    
    elif file_name == 'sales.csv':
        relevant_date = 'sales date'
    
    elif file_name == 'losses.csv':
        relevant_date = 'loss date'

    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        input_date = input(F"Step 5 = Enter the current '{relevant_date}' of product '{search_type}' as shown above as follows: dd-mm-yyyy: ")
        print('\n')

        # 3 Variables to check for the relevant date of the product in the relevant file with my 'product_detail_check()' function.
        purchase_date_check = product_detail_check('inventory.csv', search_type, 'purchase_date')
        sales_date_check = product_detail_check('sales.csv', search_type, 'sales_date')
        loss_date_check = product_detail_check('losses.csv', search_type, 'loss_date')
        
        if file_name == 'inventory.csv' and input_date in purchase_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_date}': '{input_date}', matches one of the current '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")

        elif file_name == 'sales.csv' and input_date in sales_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_date}': '{input_date}', matches one of the current '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and input_date in loss_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current '{relevant_date}': '{input_date}', matches one of the current '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered current '{relevant_date}': '{input_date}', doesn't match with one of the current '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file.\
 Please check the 'product details' of product '{search_type}' shown above for the correct current '{relevant_date}'.[/orange3]\n")

            continue
        break


    if file_name == 'losses.csv':

        print('\n')
        product_in_file_check('losses.csv', search_type)

        while True:
            loss_cause = (input(F"Step 5a = Enter the relevant 'cause of loss' of product '{search_type}' (as shown above in the 'product details') that you want to modify (not case sensitive): ")).lower()
            print('\n')
            
            if loss_cause in product_detail_check('losses.csv', search_type, 'loss_cause'):
                (product_in_file_check('losses.csv', search_type))
                rprint(F"[green]Great!:thumbs_up: The entered 'cause of loss': '{loss_cause}', matches one of the 'causes of loss' of product '{search_type}' in the 'Losses' file. You can see all the 'causes of loss' of product\
 '{search_type}' in the 'product details' shown above.[/green]\n")
            
            else:
                (product_in_file_check('losses.csv', search_type))
                rprint(F"[orange3]:scream: Hello user! The entered 'cause of loss': '{loss_cause}', doesn't match with one of the 'causes of loss' options in the 'Losses' file. Please enter the correct 'cause of loss' for product\
 '{search_type}' that you want to modify as shown above in the 'product details' (not case sensitive).[/orange3]\n")
                
                continue
            break


    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        expiration_date = input(F"Step 6 = Enter the current 'expiration date' of product '{search_type}' as shown above in the 'product details' as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print('\n')
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered current 'expiration date': '{expiration_date}', isn't the correct way to fill in the 'expiration date' for product '{search_type}' from the '{file_name.capitalize()[:-4]}'\
 file. Please enter the current 'expiration date' as shown above as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue

        expiration = convert_to_dutch_date(expiration_date)

        expiration_date_check = product_detail_check(file_name, search_type, 'expiration_date') # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven ingevulde\
                                                                                                # variabel: 'search_type' dat het door de gebruiker ingevulde product is.
        if expiration_date in expiration_date_check:
                                                        # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn 'input' statement 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'product_detail_check'\
                                                        # functie dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te\
            print('\n')                                 # gebruiken i.p.v. de '==' operator, want met de 'in' operator kijk je of er iets 'wel' of 'niet' in een lijst zit.
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered current 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 'expiration dates' of product '{search_type}' in the 'product details' shown above.[/green]\n")
            
            if expiration == current_date().strftime("%d-%m-%Y"):   # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement.
                rprint(F"[wheat1]:astonished_face: Please note that the entered 'expiration date' of product '{search_type}': '{expiration_date}', is today.:astonished_face:[/wheat1]\n")

            if expiration < current_date().strftime("%d-%m-%Y"):    # LET OP!!! Deze getabte / geïndente functie i.c.m. onderstaande print statement werkt alleen als de 'if' statement van hierboven 'True' is. Zo niet, dan werkt onderstaande\
                                                                    # 'else' statement.
                rprint(F"[wheat1]:scream: Please note that the entered 'expiration date' of product '{search_type}': '{expiration_date}', has expired.:scream:[/wheat1]\n")

        else:
            print('\n')
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered current 'expiration date': '{expiration_date}', doesn't match with one of the current 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file.\
 Please check the 'product details' above for the correct current 'expiration date'.[/orange3]\n")

            continue
        break


    print('\n')
    column_name_check(file_name)
    print('\n')

    while True:
        column_name = (input(F"Step 7 = Enter the 'product detail name' of product '{search_type}' (as shown above) that you want to modify, for instance 'expiration date' etc. (not case sensitive and you don't have to put an underscore in\
 the 'product detail name'): ")).lower()
        print('\n')
        
        # Below are all the unique column names from the 3 CSV files. I've put these column names in a 'column_name' variable for 2 reasons:
        # 1 = The user doesn't have to type the underscore. 2 = So that I can use them in my 'column_name_check()' function where the underscore is needed.
        if column_name == 'purchase quantity':
            column_name = 'purchase_quantity'

        elif column_name == 'purchase amount':
            column_name = 'purchase_amount'

        elif column_name == 'purchase date':
            column_name = 'purchase_date'

        elif column_name == 'sold quantity':
            column_name = 'sold_quantity'

        elif column_name == 'sales amount':
            column_name = 'sales_amount'

        elif column_name == 'sales date':
            column_name = 'sales_date'

        elif column_name == 'loss quantity':
            column_name = 'loss_quantity'

        elif column_name == 'loss amount':
            column_name = 'loss_amount'
        
        elif column_name == 'loss date':
            column_name = 'loss_date'
        
        elif column_name == 'loss cause':
            column_name = 'loss_cause'
        
        elif column_name == 'expiration date':
            column_name = 'expiration_date'


        if column_name in column_name_check(file_name):
            print('\n')
            rprint(F"[green]Great!:thumbs_up: The entered product detail name '{column_name}' for product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see all the 'product detail names' from the\
 '{file_name.capitalize()[:-4]}' file above.[/green]\n")

        else:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! The entered current 'product detail name': '{column_name}', doesn't match with one of the current 'product detail names' of product '{search_type}' in the '{file_name.capitalize()[:-4]}'\
 file. Please check the 'product detail names' above for the correct current 'product detail name'.[/orange3]\n")
            

            continue
        break


    print('\n')
    show_product_details(file_name, search_type, expiration_date)

    maximum_digits = '15'

    while True:
        product_detail = (input(F"Step 8 = Enter the 'modification' you would like to make for the '{column_name}' of product '{search_type}' in the the '{file_name.capitalize()[:-4]}' file (not case sensitive). You can see all the current\
 'product details' of product '{search_type}' above: ")).lower()
        
        if column_name == "id" or column_name == 'purchase_quantity' or column_name == 'sold_quantity' or column_name == 'loss_quantity':
            
            try:
                int(product_detail)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'modification' for product detail name '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file can only contain numbers. '{product_detail}' doesn't\
 only contain numbers. Please enter the correct modification for 'product detail name': '{column_name}'.[/orange3]\n")
            
                continue

            if len(product_detail) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The '{column_name}' can't contain more than '{maximum_digits}' digits. The entered '{column_name}': '{product_detail}', contains more than '{maximum_digits}' digits. Please enter the\
 modification for the '{column_name}' with a limit of '{maximum_digits}' digits.[/orange3]\n")
                
                continue

        elif column_name == 'purchase_amount' or column_name == 'sales_amount' or column_name == 'loss_amount':
        
            try:
                float(product_detail)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'modification' for product detail '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file can only contain an amount or a dot to seperate any\
 decimals. '{product_detail}' doesn't only contain an amount or a dot to seperate the decimals. Please enter the correct modification for product detail '{column_name}' of product '{search_type}' and use a dot in stead of a comma to\
 seperate any decimals.[/orange3]\n")
                
                continue
            
            product_detail_amount = float(product_detail)
            decimal_quantity = round(product_detail_amount, 2)
            
            if product_detail_amount != decimal_quantity:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the '{column_name}' again and only add '2 decimals' when necessary.[/orange3]\n")

                continue

            elif len(product_detail) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The '{column_name}' can't contain more than '{maximum_digits}' digits. The entered '{column_name}': '{product_detail}', contains more than '{maximum_digits}' digits. Please enter the\
 '{column_name}' with a limit of '{maximum_digits}' digits.[/orange3]\n")
                
                continue

        elif column_name == 'purchase_date' or column_name == 'sales_date' or column_name == 'expiration_date' or column_name == 'loss_date':
            
            try:
                convert_to_dutch_date(product_detail)
                
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{product_detail}' isn't the correct way to fill in the '{relevant_date}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter the '{relevant_date}'\
 as follows: dd-mm-yyyy.[/orange3]\n")
                
                continue

            avoid_future_date = convert_to_strptime(product_detail)

            if column_name == 'purchase_date' and avoid_future_date > current_date() or column_name == 'sales_date' and avoid_future_date > current_date() or column_name == 'loss_date' and avoid_future_date > current_date():
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The date you just entered: '{product_detail}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct '{relevant_date}' of product\
 '{search_type}' as follows: dd-mm-yyyy.[/orange3]\n")
                
                continue

        elif column_name == 'loss_cause':

            loss_cause_options = ['broken', 'damaged', 'expired', 'missing', 'theft', 'other']

            if product_detail in loss_cause_options:
                print('\n')
                rprint(F"[green]Great!:thumbs_up: '{product_detail.capitalize()}' is a correct cause of loss option in the '{file_name.capitalize()[:-4]}' file.[/green]\n")

            else:
                print('\n')
                rprint(F"[orange3]:scream: Hello user. The 'cause of loss' you just entered: '{product_detail}', isn't a correct 'cause of loss' option in the '{file_name.capitalize()[:-4]}' file. Please enter one of the following causes\
 of loss options for product '{search_type}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).[/orange3]\n")

                continue
        break


    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        # Variables for the relevant files which are needed to loop over the relevant columns in the for loop below.
        if file_name == 'inventory.csv':
            quantity_in_file = 'purchase_quantity'  # Een variabel gebruik je wanneer je iets in je code ook wil kunnen veranderen. Dus met de variabel 'quantity_in_file' zorg ik er in eerste instantie voor dat deze variabel altijd als\
                                                    # 'product_quantity' is gedefinieerd in onderstaande 'for loop'. Maar omdat ik alleen in mijn 'sales' en 'inventory' bestand de productdetail 'product_quantity' heb en in mijn 'losses'\
                                                    # bestand deze productdetail 'loss_quantity' heet, ga ik met onderstaande 'if statement' de variabel aanpassen zodat ik met onderstaande 'for loop' ook kan itereren in mijn 'losses'\
                                                    # bestand. Ik heb deze code geschreven omdat ik problemen kreeg toen onderstaande for loop alleen itereerde over de productdetail 'product_quantity'. Mijn 'losses' bestand had namelijk\
                                                    # geen productdetail genaamd 'product_quantity' en dat veroorzaakte een probleem.
        elif file_name == 'sales.csv':              # Met deze 2 codes geef ik dus aan dat als het bestandsnaam het 'losses' bestand betreft, de variabel 'quantity_in_file' aangepast moet worden in de productdetail 'loss_quantity'. En op\
            quantity_in_file = 'sold_quantity'      # deze manier komt onderstaande for loop niet in de problemen.

        elif file_name == 'losses.csv':
            quantity_in_file = 'loss_quantity'


        if file_name == 'inventory.csv':
            amount_in_file = 'purchase_amount'

        elif file_name == 'sales.csv':
            amount_in_file = 'sales_amount'

        elif file_name == 'losses.csv':
            amount_in_file = 'loss_amount'


        if file_name == 'inventory.csv':
            date_in_file = 'purchase_date'

        elif file_name == 'sales.csv':
            date_in_file = 'sales_date'

        elif file_name == 'losses.csv':
            date_in_file = 'loss_date'


        for row in rows:
            
            loss_cause_check = True # Om ervoor te zorgen dat de kolomnaam 'loss_cause' alleen wordt meegenomen (in de iteratie van deze for loop) wanneer het 'losses' bestand wordt gekozen, moet je eerst een bijpassende variabel aanmaken\
                                    # die altijd 'True' is. Ik heb hiervoor de variabel 'loss_cause_check' aangemaakt.
            
            if file_name == 'losses.csv':           # Vervolgens moet je binnen je 'for loop' met een 'if' statement aangeven op welk bestand de variabel 'loss_cause_check' van toepassing moet zijn. Vervolgens geef je met nog een 'if'\
                if row['loss_cause'] != loss_cause: # statement aan dat wanneer de inhoud van de kolomnaam 'loss_cause' niet gelijk is aan wat de gebruiker invult (bij stap 5a) / de input statement 'loss_cause', de bijpassende variabel\
                    loss_cause_check = False        # 'loss_cause_check' 'False' is. En wanneer je dit hebt gedaan, kan je de variabel 'loss_cause_check' toevoegen aan onderstaande 'if' statement op de volgende manier:\
                                                    # loss_cause_check == True.

            if (row['name'] == search_type or row['id'] == search_type) and row[quantity_in_file] == quantity and row[amount_in_file] == input_amount and row[date_in_file] == input_date and loss_cause_check == True\
and row['expiration_date'] == expiration_date:
            
                print('\n')
                rprint(F"[bright_magenta]Product details of product '{search_type}' from the '{file_name.capitalize()[:-4]}' file that you want to modify:[/bright_magenta]")
                rprint(F"[bright_cyan]{row}[/bright_cyan]")
                print('\n')
                
                while True:
                    yes_or_no = input(F"Step 9 = Are you sure you want to modify the 'product detail': '{column_name}' of product: '{search_type}' from the 'current {column_name}': '{row[column_name]}' (as shown above in the\
 'product details') to the 'modified {column_name}': '{product_detail}'? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
                    print('\n')
                    
                    if yes_or_no == 'Y' or yes_or_no == 'y':
                        row[column_name] = product_detail
                        rprint(F"[green]Great![/green]:thumbs_up: The product detail '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file has been modified to '{product_detail}'. You can check the\
 modification of product '{search_type}' below.\n")
                        rprint(F"[bright_cyan]{row}[/bright_cyan]")
                        print('\n')
                        break
                        
                    elif yes_or_no == 'N' or yes_or_no == 'n':
                        rprint(F"[wheat1]Okay. The product detail [green]'{column_name}'[/green] of product [green]'{search_type}'[/green] in the [green]'{file_name.capitalize()[:-4]}'[/green] file will not be modified from\
 [green]'{row[column_name]}'[/green] to [green]'{product_detail}'[/green]. You can see the current [green]'product details'[/green] below.\n")
                        rprint(F"[bright_cyan]{row}[/bright_cyan]")
                        print('\n')
                        break
                    
                    else:
                        rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' Isn't the correct input to modify the product detail '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter 'Y' for\
 Yes or 'N' for No for the correct modification (not case sensitive).[/orange3]\n")
                        continue
                break

        else:
            if file_name == 'losses.csv':       # Om ervoor te zorgen dat ook mijn 'else' statement onderscheid maakt tussen wanneer er wel of geen sprake is van de kolom 'loss cause' uit het losses bestand, heb ik ook in mijn 'else'\
                loss_cause_input = 'loss cause' # statement een 'if' en een 'elif' statement aangemaakt door deze middels een tabt / indent in mijn else statement te zetten. En dit heb ik helemaal zelf bedacht op maandag 08-07-2024 :-).
                print('\n')
                rprint(':scream:')
                rprint("[wheat1]Entered product details:[/wheat1]")
                rprint(F"[bright_cyan]Product: 'ID' or 'name' = [wheat1]'{search_type}'[/wheat1], '{relevant_quantity}' = [wheat1]'{quantity}'[/wheat1], '{relevant_amount}' = [wheat1]'{input_amount}'[/wheat1], '{relevant_date}' =\
 [wheat1]'{input_date}'[/wheat1], '{loss_cause_input}' = [wheat1]'{loss_cause}'[/wheat1] 'expiration date' = [wheat1]'{expiration_date}'[/wheat1], name of the product detail that you want to modify = [wheat1]'{column_name}'[/wheat1] and the\
 modification you want to make for product detail '{column_name}' = [wheat1]'{product_detail}'[/wheat1].[/bright_cyan]")

            elif file_name == 'inventory.csv' or file_name == 'sales.csv':
                print('\n')
                rprint(':scream:')
                rprint("[wheat1]Entered product details:[/wheat1]")
                rprint(F"[bright_cyan]Product: 'ID' or 'name' = [wheat1]'{search_type}'[/wheat1], '{relevant_quantity}' = [wheat1]'{quantity}'[/wheat1], '{relevant_amount}' = [wheat1]'{input_amount}'[/wheat1], '{relevant_date}' =\
 [wheat1]'{input_date}'[/wheat1], 'expiration date' = [wheat1]'{expiration_date}'[/wheat1], name of the product detail you want to modify = [wheat1]'{column_name}'[/wheat1] and the modification you would like to make for product detail\
 '{column_name}' = [wheat1]'{product_detail}'[/wheat1].[/bright_cyan]")

            print('\n')
            rprint(':thumbs_up:')
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! One or more of the entered 'product details' of product '{search_type}' wasn't filled in correctly. Please check the differences between the [wheat1]'Entered product details'[/wheat1]\
 shown above and the [bright_magenta]'Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file'[/bright_magenta] also shown above. And then try it again.[/orange3]\n")


    with open(file_name, 'r+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
# print(modify_product_details())
# print('\n')


'''
Modify quantity. Met deze code pas je alleen de hoeveelheid van een bepaald product aan in een door jou gekozen bestand,
zonder de voorraad van het inventory bestand aan te passen. DEZE CODE DOET HET PER WOENSDAG 28-2-2024.

- Vrijdag 31-05-2024 en zaterdagnacht 01-06-2024 = Aanpassingen van deze functie afgerond door 2 stappen toe te voegen:\
  stap 3 = de 'quantity' en stap 9 = de zekerheidsvraag. Hierdoor is de kans nog kleiner dat de hoeveelheid van het\
  verkeerde product wordt aangepast.
- Woensdagnacht 01-05-2024 rond 01:33 uur = Functie aangepast n.a.v. aanpassingen die ik heb gedaan bij mijn\
  'remove_product()': het toevoegen van mijn 'product_in_file_check(file_name, search_type)' functie 'boven'\
  vraag 4 en 5. En wat tekstuele aanpassingen gedaan.
  - Zondagavond 14-04-2024 rond 21:46 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het prima!!!
- LET OP!!! Deze functie heeft dus geen effect op de voorraad / de hoeveelheden van het inventory bestand. Het gaat\
  dus om een losse / individuele aanpassing van de hoeveelheid van een product.
- Zaterdagnacht 23-03-2024 rond 02:48 uur = Functie aangepast en getest.
'''

def modify_product_quantity():

    print("- Hello user, and welcome to the 'modify product quantity' option.\n")

    print("- Follow the step(s) below to modify the quantity of a product in a selected file. Have fun modifying!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    print("- Step 1 = Enter one of the following files in which you want to modify the quantity: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
    print("- Step 2 = Enter the product 'name' or 'ID' (the product name is not case sensitive).")
    print("- Step 3 = Enter the product 'relevant amount' (for instance 'purchase amount' or 'sales amount' etc.) and use a dot to seperate any decimals.")
    print("- Step 3 = Enter the current product 'quantity'.")
    print("- Step 5 = Enter the product 'relevant date' (for instance 'purchase date' or 'sales date' etc.) as follows: dd-mm-yyyy.")
    print("- Step 6 = Enter the product 'expiration date' as follows: dd-mm-yyyy.")
    print("- Step 7 = Enter 'increase' or 'decrease' to modify the quantity (not case sensitive).")
    print("- Step 8 = Enter the 'number' you want to modify ('increase' or 'decrease') the quantity with.")
    print("- Step 9 = Confirm if you 'do' or 'don't' want to modify the relevant quantity by entering 'Y' for Yes or 'N' for No (not case sensitive).")
    print("- Done!\n")
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following files in which you want to modify the quantity: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            print(F"Great! The '{file_name.capitalize()[:-4]}' file is found.\n")

        elif file_name == 'sales':
            file_name = 'sales.csv'
            print(F"Great! The '{file_name.capitalize()[:-4]}' file is found.\n")
            
        elif file_name == 'losses':
            file_name = 'losses.csv'
            print(F"Great! The '{file_name.capitalize()[:-4]}' file is found.\n")

        else:
            print(F"Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).\n")
            
            continue
        break


    while True:
        search_type = input("Step 2 = Enter the product 'ID' or 'name' (the product name is not case sensitive): ").lower()
        print('\n')

        if product_in_file_check(file_name, search_type) == True:
            print(F"Great! Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' of product '{search_type}' above.\n")
        
        else:
            print(F"Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct product 'name' or 'ID' (the product name is not case sensitive).\n")

            continue
        break


    # Names for the relevant 'quantity' in the relevant file for 'step 3' in the while loop below.
    relevant_quantity = ''
    
    if file_name == 'inventory.csv':
        relevant_quantity = 'purchase quantity'

    elif file_name == 'sales.csv':
        relevant_quantity = 'sold quantity'
    
    elif file_name == 'losses.csv':
        relevant_quantity = "loss quantity"


    while True:
        quantity = (input(F"Step 3 = Enter the current '{relevant_quantity}' of product '{search_type}': "))
        print('\n')

        try:
            int(quantity)

        except ValueError:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The current '{relevant_quantity}' can only contain numbers. '{quantity}' Doesn't only contain numbers. Please enter the correct current '{relevant_quantity}' for product '{search_type}' as shown above.\n")
            
            continue

        # 3 Variables to check for the relevant quantity of the product in the relevant file with my 'product_detail_check()' function.
        purchase_quantity_check = product_detail_check('inventory.csv', search_type, 'purchase_quantity')
        sold_quantity_check = product_detail_check('sales.csv', search_type, 'sold_quantity')
        loss_quantity_check = product_detail_check('losses.csv', search_type, 'loss_quantity')
        
        if file_name == 'inventory.csv' and quantity in purchase_quantity_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_quantity} '{quantity}' of product '{search_type}' matches one of the current '{relevant_quantity}s' in the '{file_name.capitalize()[:-4]}' file. You can compare the entered\
 '{relevant_quantity}' with the current '{relevant_quantity}' shown above in the 'product details'.\n")

        elif file_name == 'sales.csv' and quantity in sold_quantity_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_quantity} '{quantity}' of product '{search_type}' matches one of the current '{relevant_quantity}s' in the '{file_name.capitalize()[:-4]}' file. You can compare the entered\
 '{relevant_quantity}' with the current '{relevant_quantity}' shown above in the 'product details'.\n")
        
        elif file_name == 'losses.csv' and quantity in loss_quantity_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_quantity} '{quantity}' of product '{search_type}' matches one of the current '{relevant_quantity}s' in the '{file_name.capitalize()[:-4]}' file. You can compare the entered\
 '{relevant_quantity}' with the current '{relevant_quantity}' shown above in the 'product details'.\n")

        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered {relevant_quantity}: '{quantity}', doesn't match with one of the current '{relevant_quantity}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the details\
 for product '{search_type}' shown above for the correct current '{relevant_quantity}'.\n")

            continue
        break


    # Names for the relevant 'amount' in the relevant file for 'step 3' in the while loop below.
    relevant_amount = ''
    
    if file_name == 'inventory.csv':
        relevant_amount = 'purchase amount'

    elif file_name == 'sales.csv':
        relevant_amount = 'sales amount'
    
    elif file_name == 'losses.csv':
        relevant_amount = 'loss amount'


    product_in_file_check(file_name, search_type)

    while True:
        input_amount = input(F"Step 4 = Enter the '{relevant_amount}' for product '{search_type}' and use a dot to seperate any decimals. You can double check the '{relevant_amount}' of product '{search_type}' in the 'product details'\
 shown above: ")
        print('\n')

        try:
            float(input_amount)

        except ValueError:
            print(F"Hello user! The '{relevant_amount}' can only contain an amount and a dot to seperate any decimals. '{input_amount}' Doesn't only contain an amount and / or a dot to seperate the decimals. Please enter the correct\
 '{relevant_amount}' for product '{search_type}' and use a dot to seperate any decimals.\n")
            
            continue
        
        # 3 Variables to check for the relevant amount of the product in the relevant file with my 'product_detail_check()' function.
        purchase_amount_check = product_detail_check('inventory.csv', search_type, 'purchase_amount')
        sales_amount_check = product_detail_check('sales.csv', search_type, 'sales_amount')
        loss_amount_check = product_detail_check('losses.csv', search_type, 'loss_amount')

        if file_name == 'inventory.csv' and input_amount in purchase_amount_check:      # Ik heb deze code aangepast omdat ik de volgende foutmelding kreeg (en deze foutmelding kreeg ik ook bij stap 4): 'TypeError: argument of type\
            product_in_file_check(file_name, search_type)                               # 'NoneType' is not iterable'. Dit kwam omdat ik eerst met een 'if' statement moest aangeven dat de variabel 'file_name' gelijk moest zijn aan het\
                                                                                        # betreffende bestand én omdat ik in mijn oude code mijn input statement 'relevant_amount' niet in mijn if statement had verwerkt. En nu dus wel.
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the '{relevant_amount}s' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_amount}' in the product\
 details shown above.\n")
        
        elif file_name == 'sales.csv' and input_amount in sales_amount_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the '{relevant_amount}s' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_amount}' in the product\
 details shown above.\n")
        
        elif file_name == 'losses.csv' and input_amount in loss_amount_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_amount} '{input_amount}' of product '{search_type}' matches one of the '{relevant_amount}s' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_amount}' in the product\
 details shown above.\n")

        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered {relevant_amount}: '{input_amount}', doesn't match with one of the '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the details for product\
 '{search_type}' shown above for the correct '{relevant_amount}'.\n")

            continue
        break


    # Names for the relevant 'date' in the relevant file for 'step 4' in the while loop below.
    relevant_date = ''

    if file_name == 'inventory.csv':
        relevant_date = 'purchase date'
    
    elif file_name == 'sales.csv':
        relevant_date = 'sales date'
    
    elif file_name == 'losses.csv':
        relevant_date = 'loss date'

    product_in_file_check(file_name, search_type)

    while True:
        input_date = input(F"Step 5 = Enter the '{relevant_date}' for product '{search_type}' as follows: dd-mm-yyyy. You can double check the '{relevant_date}' of product '{search_type}' in the 'product details' shown above: ")
        print('\n')

        try:
            convert_to_dutch_date(input_date)
            
        except ValueError:
            print(F"Hello user! The entered {relevant_date}: '{input_date}', isn't the correct way to fill in the '{relevant_date}' for product '{search_type}'. Please enter the correct '{relevant_date}' for product '{search_type}' as\
 follows: dd-mm-yyyy.\n")
        
            continue
        
        
        # 3 Variables to check for the relevant date of the product in the relevant file with my 'product_detail_check()' function.
        purchase_date_check = product_detail_check('inventory.csv', search_type, 'purchase_date')
        sales_date_check = product_detail_check('sales.csv', search_type, 'sales_date')
        loss_date_check = product_detail_check('losses.csv', search_type, 'loss_date')
        
        if file_name == 'inventory.csv' and input_date in purchase_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date}: '{input_date}', matches one of the {relevant_date}s of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_date}' in the 'product details'\
 shown above.\n")

        elif file_name == 'sales.csv' and input_date in sales_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date}: '{input_date}', matches one of the {relevant_date}s of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_date}' in the 'product details'\
 shown above.\n")
        
        elif file_name == 'losses.csv' and input_date in loss_date_check:
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered {relevant_date}: '{input_date}', matches one of the {relevant_date}s of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see the '{relevant_date}' in the 'product details'\
 shown above.\n")

        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered {relevant_date}: '{input_date}', doesn't match one of the '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the details for product\
 '{search_type}' shown above for the correct '{relevant_date}'.\n")

            continue
        break


    while True:
        expiration_date = input(F"Step 6 = Enter the 'expiration date' of product '{search_type}' as follows: dd-mm-yyyy: ")
        print('\n')

        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print(F"Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date' for product '{search_type}'. Please enter the 'expiration date' as follows: dd-mm-yyyy.\n")
            
            continue
        
        expiration_date_check = product_detail_check(file_name, search_type, 'expiration_date')
        
        if expiration_date in expiration_date_check:    
            product_in_file_check(file_name, search_type)
            print(F"Great! The entered expiration date: '{expiration_date}', matches one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see the 'expiration date' in the product\
 details shown above.\n")
        
        else:
            product_in_file_check(file_name, search_type)
            print(F"Hello user! The entered expiration date: '{expiration_date}', doesn't match one of the expiration dates of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the 'product details' above for\
 the correct expiration date.\n")

            continue
        break


# Names for the relevant 'quantity' in the relevant file for 'step 3' in the while loop below.
    relevant_quantity = ''
    
    if file_name == 'inventory.csv':
        relevant_quantity = 'purchase quantity'

    elif file_name == 'sales.csv':
        relevant_quantity = 'sold quantity'
    
    elif file_name == 'losses.csv':
        relevant_quantity = "loss quantity"


    while True:
        modify_type = input(F"Step 7 = Enter 'increase' if you want to increase or 'decrease' if you want to decrease the '{relevant_quantity}' for product '{search_type}' (not case sensitive): ").lower()
        print('\n')

        if modify_type == 'increase' or modify_type == 'decrease':
            
            print(F"Great! It's noted that you want to '{modify_type}' the '{relevant_quantity}' of product '{search_type}' with '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}' and 'expiration date':\
 '{expiration_date}' in the '{file_name.capitalize()[:-4]}' file.\n")

        else:
            print(F"Hello user! '{modify_type}' Isn't the correct input to modify the '{relevant_quantity}' of product '{search_type}'. Please enter 'increase' or 'decrease' for the correct '{relevant_quantity}' modification (not case\
 sensitive).\n")
            
            continue
        break


    while True:
        modification = input(F"Step 8 = Enter the number by which you want to '{modify_type}' the '{relevant_quantity}' of product '{search_type}': ")
        
        try:
            int(modification)

        except ValueError:
            print('\n')
            print(F"Hello user! The '{relevant_quantity}' can only contain numbers. '{quantity}' Doesn't only contain numbers. Please enter the correct '{relevant_quantity}' to '{modify_type}' product '{search_type}'.\n")
            
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


        for row in rows:
            
            if (row['id'] == search_type or row['name'] == search_type) and row[quantity_in_file] == quantity and row[amount_in_file] == input_amount and row[date_in_file] == input_date and row['expiration_date'] == expiration_date and\
                modify_type == 'increase'.lower():
                
                print('\n')

                while True:
                    yes_or_no = input(F"Step 9 = Are you sure you want to '{modify_type}' the '{relevant_quantity}' of product: '{search_type}' with the current '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}',\
 '{relevant_date}': '{input_date}' and 'expiration date': '{expiration_date}' in the '{file_name.capitalize()[:-4]}' file? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
                    
                    if yes_or_no == 'Y' or yes_or_no == 'y':
                        row[quantity_in_file] = int(row[quantity_in_file]) + int(modification)                                                                                                          
                        print('\n')
                        print(F"Great! Product '{search_type}' with {relevant_amount} '{input_amount}', {relevant_date} '{input_date}' and expiration date '{expiration_date}' in the '{file_name.capitalize()[:-4]}' file, has been 'increased'\
 with a quantity of '{modification}'. You can see the result below.\n") 
                        print(F"Result = {row}")
                        break
                    
                    # LET OP!!! Wanneer je na de 'or' operator nog meer operarors gaat gebruiken (zoals de 'and' operator in onderstaande 'if statement'), moet je de 'or' operators tussen haakjes plaatsen, want anders werkt je code / de\
                    # 'if' statement niet.

                    elif yes_or_no == 'N' or yes_or_no == 'n':
                        print('\n')
                        print(F"Okay. Product '{search_type}' with the current '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}', and 'expiration date': '{expiration_date}' in the\
 '{file_name.capitalize()[:-4]}' file, wil not be 'increased' with a quantity of '{modification}'. You can see the details below.\n")
                        print(F"Result = {row}")
                        print('\n')
                        break

                    else:
                        print('\n')
                        print(F"Hello user! '{yes_or_no}' Isn't the correct input to '{modify_type}' the '{relevant_quantity}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter 'Y' for Yes or 'N' for No to\
 '{modify_type}' the '{relevant_quantity}' for product '{search_type}' (not case sensitive).\n")
                        continue
                break


            elif (row['id'] == search_type or row['name'] == search_type) and row[quantity_in_file] == quantity and row[amount_in_file] == input_amount and row[date_in_file] == input_date and row['expiration_date'] == expiration_date and\
                    modify_type == 'decrease'.lower():
                
                print('\n')

                while True:
                    yes_or_no = input(F"Step 9 = Are you sure you want to '{modify_type}' the '{relevant_quantity}' of product: '{search_type}' with the current '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}',\
 '{relevant_date}': '{input_date}' and 'expiration date': '{expiration_date}' in the '{file_name.capitalize()[:-4]}' file? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
                    
                    if yes_or_no == 'Y' or yes_or_no == 'y':
                        row[quantity_in_file] = int(row[quantity_in_file]) - int(modification)
                        print('\n')
                        print(F"Great! Product '{search_type}' with '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}' and 'expiration date': '{expiration_date}' in the '{file_name.capitalize()[:-4]}' file, has been\
 'decreased' with a quantity of '{modification}'. You can see the result below.\n")
                        print(F"Result = {row}")
                        break
            
                    elif yes_or_no == 'N' or yes_or_no == 'n':
                        print('\n')
                        print(F"Okay. Product '{search_type}' with the current '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}', and 'expiration date': '{expiration_date}' in the\
 '{file_name.capitalize()[:-4]}' file, wil not be 'decreased' with a quantity of '{modification}'. You can see the details below.\n")
                        print(F"Result = {row}")
                        print('\n')
                        break

                    else:
                        print('\n')
                        print(F"Hello user! '{yes_or_no}' Isn't the correct input to '{modify_type}' the '{relevant_quantity}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter 'Y' for Yes or 'N' for No to\
 '{modify_type}' the '{relevant_quantity}' for product '{search_type}' (not case sensitive).\n")
                        continue
                break

        else:
            print('\n')
            print(F"Entered product details:")
            print(F"Product: 'ID' or 'name' = '{search_type}', '{relevant_quantity}' = '{quantity}', '{relevant_amount}' = '{input_amount}', '{relevant_date}' = '{input_date}' and 'expiration date' = '{expiration_date}'.")
            print('\n')
            show_product_details(file_name, search_type, expiration_date)
            print(F"Hello user! One or more of the entered 'product details' wasn't filled in correctly. Please check the differences between the 'Entered product details' shown above and the 'Product details for product '{search_type}' in\
 the {file_name.capitalize()[:-4]} file' also shown above. And then try it again.\n")
    

    with open(file_name, 'r+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        print('\n')

# print(modify_product_quantity())
# print('\n')

# HIER BEN IK MET RICH TESTEN!!!
# User function – remove product from a file.

'''
Product verwijderen op bais van 'naam' of 'id' én in combinatie met de houdbaarheidsdatum. DEZE CODE DOET HET PER ZATERDAGNACHT 09-03-2024 ROND 02:39 UUR.
- Dinsdagavond 30-04-2024 én woensdagnacht 01-05-2024 rond 01:18 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en bestandsnamen\
  aanpassen (door ze korter te maken)'. En hij doet het nog prima!!!
- Zondag 24-03-2024 rond 17:05 uur = Functie aangepast én getest en hij deed het nog steeds.
'''

def remove_product():

    rprint("- Hello user, and welcome to the [bright_cyan]'remove product'[/bright_cyan] option.\n")
    
    print("- Follow the step(s) below to remove a product from a selected file. Have fun removing!\n")
    
    rprint("-[bright_magenta] Note 1! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")
    
    rprint("-[bright_magenta] Note 2! Step 5a will only appear when you select the 'Losses' file.[/bright_magenta]\n")
    
    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'remove products from a selected file'")

    table.add_row("- Step 1 = Enter one of the following file names in which you want to remove a product: 'Inventory', 'Sales' or 'Losses'.")
    table.add_row("- Step 2 = Enter the 'ID' or the 'name' of the product that you want to remove (not case sensitive).")
    table.add_row("- Step 3 = Enter the product 'quantity'.")
    table.add_row("- Step 4 = Enter the product 'relevant amount' (for instance 'purchase amount' or 'sales amount' etc.) and use a dot to seperate any decimals.")
    table.add_row("- Step 5 = Enter the product 'relevant date' (for instance 'purchase date' or 'sales date' etc.) as follows: dd-mm-yyyy.")
    table.add_row("- Step 5a = Enter one of the following 'causes of loss': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).")
    table.add_row("- Step 6 = Enter the product 'expiration date'.")
    table.add_row("- Step 7 = Confirm if you 'do' or 'don't' want to modify the product detail by entering 'Y' for Yes or 'N' for No (not case sensitive).")
    table.add_row("- Done!")
    
    console.print(table)
    print('\n')


    while True:
        file_name = input("Step 1 = Enter one of the following file names in which you want to remove a product: 'Inventory', 'Sales' or 'Losses': ").lower()
        print('\n')

        if file_name == 'inventory':
            file_name = 'inventory.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
        
        elif file_name == 'sales':
            file_name = 'sales.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")
        
        elif file_name == 'losses':
            file_name = 'losses.csv'
            rprint(F"[green]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/green]\n")

        else:
            rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter the correct file name (not case sensitive).[/orange3]\n")
            
            continue
        break
    
    
    while True:
        search_type = input("Step 2 = Enter the 'ID' or the 'name' of the product that you want to remove (not case sensitive): ").lower()
        print('\n')
        
        
        if product_in_file_check(file_name, search_type) == True:
            rprint(F"[green]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' above.[/green]\n")
        
        else:
            rprint(F"[orange3]:scream: Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct product 'ID' or 'name' (not case sensitive).[/orange3]\n")

            continue
        break


# Names for the relevant 'quantity' in the relevant file for 'step 3' in the while loop below.
    relevant_quantity = ''
    
    if file_name == 'inventory.csv':
        relevant_quantity = 'purchase quantity'

    elif file_name == 'sales.csv':
        relevant_quantity = 'sold quantity'
    
    elif file_name == 'losses.csv':
        relevant_quantity = 'loss quantity'

    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        quantity = (input(F"Step 3 = Enter the '{relevant_quantity}' of product '{search_type}' that you want to remove, you can see the 'product details' above: "))
        print('\n')

        # 3 Variables to check for the relevant quantity of the product in the relevant file with my 'product_detail_check()' function.
        purchase_quantity_check = product_detail_check('inventory.csv', search_type, 'purchase_quantity')
        sold_quantity_check = product_detail_check('sales.csv', search_type, 'sold_quantity')
        loss_quantity_check = product_detail_check('losses.csv', search_type, 'loss_quantity')
        
        if file_name == 'inventory.csv' and quantity in purchase_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_quantity}': '{quantity}', matches one of the '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")
            
        elif file_name == 'sales.csv' and quantity in sold_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_quantity}': '{quantity}', matches one of the '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and quantity in loss_quantity_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_quantity}': '{quantity}', matches one of the '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_quantity}' details of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered '{relevant_quantity}': '{quantity}', doesn't match with one of the '{relevant_quantity}' details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please\
 check the 'product details' of product '{search_type}' shown above for the correct '{relevant_quantity}'.[/orange3]\n")            
            continue
        break


    # Names for the relevant 'amount' in the relevant file for 'step 4' in the while loop below.
    relevant_amount = ''
    
    if file_name == 'inventory.csv':
        relevant_amount = 'purchase amount'

    elif file_name == 'sales.csv':
        relevant_amount = 'sales amount'
    
    elif file_name == 'losses.csv':
        relevant_amount = 'loss amount'

    print('\n')
    product_in_file_check(file_name, search_type)
    
    while True:
        input_amount = input(F"Step 4 = Enter the 'exact' '{relevant_amount}' of product '{search_type}' that you want to remove including any decimals as shown above in the 'product details'. And use a dot (instead of a comma) to seperate\
 any decimals: ")
        print('\n')

        # 3 Variables to check for the relevant amount of the product in the relevant file with my 'product_detail_check()' function.
        purchase_amount_check = product_detail_check('inventory.csv', search_type, 'purchase_amount')
        sales_amount_check = product_detail_check('sales.csv', search_type, 'sales_amount')
        loss_amount_check = product_detail_check('losses.csv', search_type, 'loss_amount')

        if file_name == 'inventory.csv' and input_amount in purchase_amount_check:      # Ik heb deze code aangepast omdat ik de volgende foutmelding kreeg (en deze foutmelding kreeg ik ook bij stap 4): 'TypeError: argument of type\
            product_in_file_check(file_name, search_type)                               # 'NoneType' is not iterable'. Dit kwam omdat ik eerst met een 'if' statement moest aangeven dat de variabel 'file_name' gelijk moest zijn aan het\
                                                                                        # betreffende bestand én omdat ik in mijn oude code mijn input statement 'relevant_amount' niet in mijn if statement had verwerkt. En nu dus wel.
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_amount}': '{input_amount}', matches one of the '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
            
        elif file_name == 'sales.csv' and input_amount in sales_amount_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_amount}': '{input_amount}', matches one of the '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and input_amount in loss_amount_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_amount}': '{input_amount}', matches one of the '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_amount}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered '{relevant_amount}': '{input_amount}', doesn't match with one of the '{relevant_amount}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check\
 the 'product details' of product '{search_type}' shown above for the 'exact' correct '{relevant_amount}'.[/orange3]\n")
            continue
        break


    # Names for the relevant 'date' in the relevant file for 'step 5' in the while loop below.
    relevant_date = ''

    if file_name == 'inventory.csv':
        relevant_date = 'purchase date'
    
    elif file_name == 'sales.csv':
        relevant_date = 'sales date'
    
    elif file_name == 'losses.csv':
        relevant_date = 'loss date'

    print('\n')
    product_in_file_check(file_name, search_type)
    
    while True:
        input_date = input(F"Step 5 = Enter the '{relevant_date}' of product '{search_type}' that you want to remove (as shown above in the 'product details') as follows: dd-mm-yyyy: ")
        print('\n')

        # 3 Variables to check for the relevant date of the product in the relevant file with my 'product_detail_check()' function.
        purchase_date_check = product_detail_check('inventory.csv', search_type, 'purchase_date')
        sales_date_check = product_detail_check('sales.csv', search_type, 'sales_date')
        loss_date_check = product_detail_check('losses.csv', search_type, 'loss_date')
        
        if file_name == 'inventory.csv' and input_date in purchase_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_date}': '{input_date}', matches one of the '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
            
        elif file_name == 'sales.csv' and input_date in sales_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_date}': '{input_date}', matches one of the '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")
        
        elif file_name == 'losses.csv' and input_date in loss_date_check:
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered '{relevant_date}': '{input_date}', matches one of the '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the\
 '{relevant_date}s' of product '{search_type}' in the 'product details' shown above.[/green]\n")

        else:
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered '{relevant_date}': '{input_date}', doesn't match with one of the '{relevant_date}s' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the\
 'product details' of product '{search_type}' shown above for the correct '{relevant_date}'.[/orange3]\n")            
            continue
        break


    if file_name == 'losses.csv':

        print('\n')
        product_in_file_check('losses.csv', search_type)

        while True:
            loss_cause = (input(F"Step 5a = Enter the relevant 'cause of loss' of product '{search_type}' (as shown above in the 'product details') that you want to remove (not case sensitive): ")).lower()
            print('\n')
            
            if loss_cause in product_detail_check('losses.csv', search_type, 'loss_cause'):
                (product_in_file_check('losses.csv', search_type))
                rprint(F"[green]Great!:thumbs_up: The entered 'cause of loss': '{loss_cause}', matches one of the 'causes of loss' of product '{search_type}' in the 'Losses' file. You can see all the 'causes of loss' of product\
 '{search_type}' in the 'product details' shown above.[/green]\n")
            
            else:
                (product_in_file_check('losses.csv', search_type))
                rprint(F"[orange3]:scream: Hello user. The 'cause of loss' you just entered: '{loss_cause}', isn't a correct 'cause of loss' option in the 'Losses' file. Please enter one of the following 'causes of loss' for product\
 '{search_type}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' as shown above in the 'product details' (not case sensitive).[/orange3]\n")
                
                continue
            break


    print('\n')
    product_in_file_check(file_name, search_type)

    while True:
        expiration_date = input(F"Step 6 = Enter the 'expiration date' of product '{search_type}' (as shown above in the 'product details') that you want to remove as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(expiration_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{expiration_date}' isn't the correct way to fill in the 'expiration date' for product '{search_type}'. Please enter the expiration date as follows: dd-mm-yyyy.[/orange3]\n")
            
            continue


        expiration = convert_to_dutch_date(expiration_date)
        
        expiration_date_check = product_detail_check(file_name, search_type, 'expiration_date') # Met deze code zorg ik ervoor dat de ingevoerde 'houdbaarheidsdatum' altijd overeenkomt met de houdbaarheidsdatum van de hierboven ingevulde\
                                                                                                # 'search_type' product.

        if expiration_date in expiration_date_check:    # LET OP!!! Wanneer je 2 verschillende types (in dit geval: een string met een lijst) probeert te vergelijken, zal dit nooit 'True' zijn / gaat je code niet werken. Ik had bij deze\
                                                        # code namelijk gepropeerd om mijn 'input' statement 'expiration_date' in deze while loop dat een 'string' is te vergelijken met mijn return statement van mijn 'product_detail_check'\
                                                        # functie dat een 'lijst' is. Door deze verkeerde vergelijking met 2 verschillende type code, werkte ondersaande print statement niet. Dit heb ik opgelost door de 'in' operator te\
                                                        # gebruiken i.p.v. de '==' operator, want met de 'in' operator kijk je of er iets 'wel' of 'niet' in een lijst zit.

            print('\n')
            product_in_file_check(file_name, search_type)
            rprint(F"[green]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all the 'expiration\
 dates' of product '{search_type}' in the 'product details' shown above.[/green]\n")
            
            if expiration == current_date().strftime("%d-%m-%Y"):   # LET OP!!! Deze getabte / geïndente 'if' & 'elif' statements inc. de print statements werken alleen als de 'if' statement hierboven 'True' is. Zo niet, dan werkt onderstaande\
                # print(F"Dit is expiration: {expiration}")           # 'else' statement. LET OP!!! Door de '.strftime("%d-%m-%Y")' method / code achter mijn 'current_date()' functie te plaatsen zorg ik ervoor dat het 'tijdstip' van mijn\
                # print(type(expiration))                             # 'current_date()' functie niet zichtbaar is én dat de Nederlandse datum volgorde wordt gehanteerd. LET OP!!! Na overleg met een Winc mentor had ik eerst de '.date()'\
                # print(type(current_date().strftime("%d-%m-%Y")))    # method achter mijn 'current_date()' funtie gezet. Dit omdat de '.today()' method in mijn 'current_date()' functie ook de exacte tijd meegeeft. En mijn 'expiration'\
                                                                    # variabel geeft ook de tijd mee, maar die staat op nul / 0. En hierdoor onstond er een afwijking waardoor de vergelijking niet werkt / Python geen vergelijking kan maken\
                                                                    # en hierdoor kreeg ik onderstaande 'rprint statement' / 'string' ook niet te zien. De '.date()' method geeft enkel en alleen de datum weer, maar dan op de Engelse manier.\
                                                                    # Dus die kan ik beter gebruiken de volgende keer en dan de 'strftime()' method gebruiken om er de nederlandse tijdsaanduiding van te maken in mijn 'current_date()' functie.
                rprint(F"[wheat1]:astonished_face: Please note that the entered 'expiration date' of product '{search_type}': '{expiration_date}', is today.:astonished_face:[/wheat1]\n")

            elif expiration < current_date().strftime("%d-%m-%Y"):
                # print(F"Dit is expiration: {expiration}")
                # print(type(expiration))
                # print(type(current_date()))
                # print(current_date().strftime("%d-%m-%Y"))
                rprint(F"[wheat1]:scream: Please note that the entered 'expiration date' of product '{search_type}': '{expiration_date}', has expired.:scream:[/wheat1]\n")

        else:
            print('\n')
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! The entered 'expiration date': '{expiration_date}', doesn't match with one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check the\
 'product details' of product '{search_type}' shown above for the correct 'expiration date'.[/orange3]\n")
            continue
        break


    with open(file_name, 'r', newline= '',) as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        # Variables for the relevant files which are needed to loop over the relevant columns in the for loop below.
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

        
        for row in rows:

            loss_cause_check = True # Om ervoor te zorgen dat de kolomnaam 'loss_cause' alleen wordt meegenomen (in de iteratie van deze for loop) wanneer het 'losses' bestand wordt gekozen, moet je eerst een bijpassende variabel aanmaken\
                                    # die altijd 'True' is. Ik heb hiervoor de variabel 'loss_cause_check' aangemaakt.

            if file_name == 'losses.csv':           # Vervolgens moet je binnen je 'for loop' met een 'if' statement aangeven op welk bestand de variabel 'loss_cause_check' van toepassing moet zijn. Vervolgens geef je met nog een 'if'\
                if row['loss_cause'] != loss_cause: # statement aan dat wanneer de inhoud van de kolomnaam 'loss_cause' niet gelijk is aan wat de gebruiker invult (bij stap 5a) / de input statement 'loss_cause', de bijpassende variabel\
                    loss_cause_check = False        # 'loss_cause_check' 'False' is. En wanneer je dit hebt gedaan, kan je de variabel 'loss_cause_check' toevoegen aan onderstaande 'if' statement op de volgende manier:\
                                                    # loss_cause_check == True.
            if (row['name'] == search_type or row['id'] == search_type) and row[quantity_in_file] == quantity and row[amount_in_file] == input_amount and row[date_in_file] == input_date and loss_cause_check == True\
 and row['expiration_date'] == expiration_date:
            
                print('\n')
                rprint(F"[bright_magenta]Product details of product '{search_type}' that you want to remove from the '{file_name.capitalize()[:-4]}' file:[/bright_magenta]")
                rprint(F"[bright_cyan]{row}[/bright_cyan]")
                print('\n')

                while True:
                    yes_or_no = input(F"Step 7 = Are you sure you want to remove product '{row['name']}' with product 'ID': '{row['id']}' as shown above in the 'product details' from the '{file_name.capitalize()[:-4]}' file? Press 'Y' for\
 Yes or 'N' for No (not case sensitive): ")
                    print('\n')

                    if file_name == 'losses.csv' and (yes_or_no == 'Y' or yes_or_no == 'y'):
                        loss_cause_input = 'loss cause'
                        rows.remove(row)
                        rprint(F"[green]Great![/green]:thumbs_up: Product '{row['name']}' with product 'ID': '{row['id']}', '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}',\
 'loss cause': '{loss_cause}' and 'expiration date': '{expiration_date}' has been removed from the '{file_name.capitalize()[:-4]}' file.\n")
                        break
                    
                    elif (file_name == 'inventory.csv' or file_name == 'sales.csv') and yes_or_no == 'Y' or yes_or_no == 'y':
                        rows.remove(row)
                        rprint(F"[green]Great![/green]:thumbs_up: Product '{row['name']}' with product 'ID': '{row['id']}', '{relevant_quantity}': '{quantity}', '{relevant_amount}': '{input_amount}', '{relevant_date}': '{input_date}' and\
 'expiration date': '{expiration_date}' has been removed from the '{file_name.capitalize()[:-4]}' file.\n")
                        break

                    elif yes_or_no == 'N' or yes_or_no == 'n':
                        rprint(F"[wheat1]Okay. Product [green]'{row['name']}'[/green] with product [green]'ID'[/green]: [green]'{row['id']}'[/green] has not been removed from the [green]'{file_name.capitalize()[:-4]}'[/green] file. You can\
 see the [green]'product details'[/green] of product [green]'{search_type}'[/green] below.[/wheat1]\n") # Bij deze elif statement heb ik er bewust voor gekozen om aan het begin van de 'rprint statement' de code '{row['name']}' te plaatsen\
                        rprint(F"[bright_cyan]{row}[/bright_cyan]")                                     # en aan het einde van de 'rprint statement' de '{search_type}' code te plaatsen zodat je als programmeur toch een dubbele / extra check\
                        print('\n')                                                                     # hebt of de product 'ID' en de product 'naam' hetzelfde zijn. In bovenstaande codes binnen de 'while loop' heb ik op bepaalde plekken\
                        break                                                                           # mijn 'search_type' code ook vervangen door de '{row['name']}' code om te voorkomen dat je in de print statement 2X het product 'ID' te\
                                                                                                        # te zien krijgt, b.v. in de volgende zin: "Okay. Product '2032' with product 'ID': '2032' has not been removed from the Inventory file."
                    else:
                        rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' Isn't the correct input to remove product '{search_type}' from the '{file_name.capitalize()[:-4]}' file. Please enter 'Y' for Yes if you 'do' or N for No if you\
 'don't' want to remove product '{search_type}' from the '{file_name.capitalize()[:-4]}' file (not case sensitive).[/orange3]\n")

                        continue
                break

        else:
            if file_name == 'losses.csv':       # Om ervoor te zorgen dat ook mijn 'else' statement onderscheid maakt tussen wanneer er wel of geen sprake is van de kolom 'loss cause' uit het losses bestand, heb ik ook in mijn 'else'\
                loss_cause_input = 'loss cause' # statement een 'if' en een 'elif' statement aangemaakt door deze middels een tab / indent in mijn else statement te zetten. En dit heb ik helemaal zelf bedacht op maandag 08-07-2024 :-).
                rprint(':scream:')
                rprint("[wheat1]Entered product details:[/wheat1]")
                rprint(F"[bright_cyan]Product: 'ID' or 'name' = [wheat1]'{search_type}'[/wheat1], '{relevant_quantity}' = [wheat1]'{quantity}'[/wheat1], '{relevant_amount}' = [wheat1]'{input_amount}'[/wheat1], '{relevant_date}' =\
 [wheat1]'{input_date}'[/wheat1], '{loss_cause_input}' = [wheat1]'{loss_cause}'[/wheat1] 'expiration date' = [wheat1]'{expiration_date}'.[/wheat1][/bright_cyan]\n")
                
            elif file_name == 'inventory.csv' or file_name == 'sales.csv':
                rprint(':scream:')
                rprint("[wheat1]Entered product details:[/wheat1]")
                rprint(F"[bright_cyan]Product: 'ID' or 'name' = [wheat1]'{search_type}'[/wheat1], '{relevant_quantity}' = [wheat1]'{quantity}'[/wheat1], '{relevant_amount}' = [wheat1]'{input_amount}'[/wheat1], '{relevant_date}' =\
 [wheat1]'{input_date}'[/wheat1], 'expiration date' = [wheat1]'{expiration_date}'[/wheat1].[/bright_cyan]\n")
            
            rprint(':thumbs_up:')
            product_in_file_check(file_name, search_type)
            rprint(F"[orange3]:scream: Hello user! One or more of the entered 'product details' of product '{search_type}' wasn't filled in correctly. Please check the differences between the [wheat1]'Entered product details'[/wheat1]\
 shown above and the [bright_magenta]'Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file'[/bright_magenta] also shown above. And then try it again.[/orange3]\n")


    with open(file_name, 'w', newline= '') as file:
        writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# print(remove_product())
# print('\n')


# Help functions – calculate costs, revenue and profit.

'''
Met de 'calculate_costs' functie kan je de totale kosten / inkoopprijs van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.

- Woensdag 08-05-2024 en donderdagnacht 09-05-2024 rond 01:57 uur = Functie toch nog aangepast omdat ik een nieuwe functie heb\
  toegevoegd aan mijn datum functies: 'convert_to_strftime(string)'. Hierdoor ben ik weer al mijn functies gaan nalopen\
  waar ik de 'datetime' objecten gebruik zodat ik de functies netter kan maken.
- Maandag 06-05-2024 rond 22:41 uur = Functie wederom aangepast én getest omdat ik per ongeluk deze functie met input statements had\
  gemaakt terwijl dit niet de bedoeling was. Dit omdat ik was vergeten dat ik in mijn 'calculations()' functie (was mijn oude\
  'time_frame_calculation()' functie) code had geschreven waarmee de gebruiker kan kiezen welke berekening hij / zij wil zien:\
  'inkoopkosten', 'omzet' of 'winst'.
- Zaterdagavond 04-05-2024 en zaterdagnacht 05-05-2024 rond 00:22 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het prima!!!
''' 

def calculate_costs(from_date: datetime, until_date: datetime):

    with open('inventory.csv', 'r') as inventory_file:
        reader = csv.DictReader(inventory_file)

        total_costs = 0

        for row in reader:
        
            purchase_date = convert_to_strptime(row['purchase_date'])
            
            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)
            
            # print(input_from_date)
            # print(input_until_date)

            # print(F"Dit is regel 2575 {type(input_from_date)}") # Op deze manier kan je met een 'F-string' zien wat voor 'type' een code / variabel is.
            # print(F"Dit is regel 2576 {type(input_until_date)}")
            # print(F"Dit is regel 2577 {type(from_date)}")
            # print(F"Dit is regel 2578 {type(until_date)}")
            
            if input_from_date <= purchase_date and input_until_date >= purchase_date:
                costs = float(row['purchase_quantity']) * float(row['purchase_amount'])
            
                total_costs += costs
        
        return round(total_costs, 2)

# print(calculate_costs("23-01-2024", "26-01-2024"))
# print(calculate_costs("01-01-2024", "06-05-2024"))
# print('\n')


'''
Met de 'calculate_losses' functie kan je de totale verliezen van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER MAANDAG 13-05-2024 rond 17:17 uur.

- Maandag 13-05-2024 rond 22:41 uur = Op deze dag heb ik deze functie geschreven én getest na de start van mijn taak: 'kolom- en bestandsnamen aanpassen (door ze korter te maken)'
''' 

def calculate_losses(from_date: datetime, until_date: datetime):

    with open('losses.csv', 'r') as losses_file:
        reader = csv.DictReader(losses_file)

        total_losses = 0

        for row in reader:
        
            loss_date = convert_to_strptime(row['loss_date'])
            
            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)
            
            if input_from_date <= loss_date and input_until_date >= loss_date:
                losses = float(row['loss_quantity']) * float(row['loss_amount'])
            
                total_losses += losses
        
        return round(total_losses, 2)

# print(calculate_losses("23-01-2024", "26-01-2024"))
# print(calculate_losses("01-01-2024", "31-05-2024"))
# print('\n')


'''
Met de 'calculate_revenue' functie kan je de totale omzet van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.

- Woensdag 08-05-2024 en donderdagnacht 09-05-2024 rond 02:00 uur = Functie toch nog aangepast omdat ik een nieuwe functie heb\
  toegevoegd aan mijn datum functies: 'convert_to_strftime(string)'. Hierdoor ben ik weer al mijn functies gaan nalopen\
  waar ik de 'datetime' objecten gebruik zodat ik de functies netter kan maken.
- Maandag 06-05-2024 rond 22:41 uur = Functie wederom aangepast én getest omdat ik per ongeluk deze functie met input statements had\
  gemaakt terwijl dit niet de bedoeling was. Dit omdat ik was vergeten dat ik in mijn 'calculations()' functie (was mijn oude\
  'time_frame_calculation()' functie) code had geschreven waarmee de gebruiker kan kiezen welke berekening hij / zij wil zien:\
  'inkoopkosten', 'omzet' of 'winst'.
''' 

def calculate_revenue(from_date: datetime, until_date: datetime):

    with open('sales.csv', 'r') as sales_file:
        reader = csv.DictReader(sales_file)

        total_revenue = 0

        for row in reader:
        
            sales_date = convert_to_strptime(row['sales_date'])

            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)

            if input_from_date <= sales_date and input_until_date >= sales_date:
                revenue = float(row['sold_quantity']) * float(row['sales_amount'])
            
                total_revenue += revenue
        
    return round(total_revenue, 2)
    
# print(calculate_revenue("23-01-2024", "26-01-2024"))
# print(calculate_revenue("01-01-2024", "06-05-2024"))
# print('\n')


'''
Met de 'calculate_profit' functie kan je de totale winst van een door jou opgegeven periode uitrekenen. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.

- Woensdag 08-05-2024 en donderdagnacht 09-05-2024 rond 02:10 uur = Functie toch nog aangepast omdat ik een nieuwe functie heb\
  toegevoegd aan mijn datum functies: 'convert_to_strftime(string)'. Hierdoor ben ik weer al mijn functies gaan nalopen\
  waar ik de 'datetime' objecten gebruik zodat ik de functies netter kan maken.
- Maandag 06-05-2024 rond 23:39 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het prima!!!
''' 

def calculate_profit(from_date: datetime, until_date: datetime):
    
    with open('sales.csv', 'r') as sales_file:
        reader = csv.DictReader(sales_file)

        for row in reader:
    
            product_sales_date = convert_to_strptime(row['sales_date'])

            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)

            if input_from_date <= product_sales_date and input_until_date >= product_sales_date:
                profit = float(calculate_revenue(from_date, until_date)) - float(calculate_costs(from_date, until_date)) - float(calculate_losses(from_date, until_date))# De datum wordt hier toch op de Engelse manier weergegeven en ik wil het op de NL manier.
                # profit = float(calculate_revenue(from_date, until_date)) - float(calculate_costs(from_date, until_date)) # DEZE CODE DOET HET!!!
                
    return round(profit, 2)

# print(calculate_profit("23-01-2024", "26-01-2024"))
# print(calculate_profit("01-01-2024", "31-05-2024"))
# print('\n')


# User functions – calculate costs, revenue and profit.

'''
Met de 'calculations' functie (oude naam was 'time_frame_calculation()' functie) kan je de zelf kiezen wat je wilt\
uitrekenen in een door jou opgegeven periode: kosten, omzet of de winst. DEZE CODE DOET HET PER WOENSDAG 21-02-2024.

- Maandag 03-06-2024 rond 16:00 uur = Tekstuele aangepassingen gedaan m.b.t. 'aanhalingstekens' aangepast in 'apostroffen'\
  én het woord 'losses' toegevoegd in het menu en in de input statement.
- Dinsdagnacht 07-05-2024 rond 00:27 uur = Functie aangepast én getest na de start van mijn taak: 'kolom- en\
  bestandsnamen aanpassen (door ze korter te maken)'. En hij doet het prima!!!
''' 

def calculations():

    rprint("- Hello user, and welcome to the [bright_cyan]'calculations'[/bright_cyan] option.\n")

    rprint("- Follow the [grey78]step(s)[/grey78] below to select which calculation you would like to make: 'costs', 'losses', 'revenue' or 'profit'. Have fun calculating!\n")
    
    rprint("-[bright_magenta] Note! Press 'Ctrl' + 'C' on your keyboard if you want to exit / quit filling in the step(s).[/bright_magenta]\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("Steps to: 'calculate the costs, losses, revenue or profit'")


    table.add_row("- Step 1 = Enter one of the following calculations you would like to make: 'costs', 'losses', 'revenue' or 'profit' (not case sensitive).")
    table.add_row("- Step 2 = Enter the 'from' date as follows: dd-mm-yyyy.")
    table.add_row("- Step 3 = Enter the 'until' date as follows dd-mm-yyyy.")
    table.add_row("- Done!")
    
    console.print(table)
    print('\n')


    while True:
        calculation_type = input("Step 1 = Enter one of the following calculations you would like to make: 'costs', 'losses', 'revenue' or 'profit' (not case sensitive): ").lower()
        
        if calculation_type == 'costs' or calculation_type == 'losses' or calculation_type == 'revenue' or calculation_type == 'profit':
            print('\n')
            rprint(F"[green]Great!:thumbs_up: It is noted that you want to calculate the '{calculation_type}'.[/green]\n")

        else:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{calculation_type}' Isn't the correct input for selecting a calculation. Please enter one of the following calculations: 'costs', 'losses', 'revenue' or 'profit'.[/orange3]\n")
            continue
        break


    while True:
        from_date = input("Step 2 = Enter the 'from' date as follows: dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(from_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{from_date}' Isn't the correct way to fill in the 'from' date. Please enter the correct 'from' date as follows: dd-mm-yyyy.[/orange3]\n")

            continue
        break


    while True:
        until_date = input("Step 3 = Enter the 'until' date as follows dd-mm-yyyy: ")
        
        try:
            convert_to_dutch_date(until_date)
            
        except ValueError:
            print('\n')
            rprint(F"[orange3]:scream: Hello user! '{until_date}' Isn't the correct way to fill in the 'until' date. Please enter the correct 'until' date as follows: dd-mm-yyyy.[/orange3]\n")

            continue
        break    


    if calculation_type == 'costs':
        calculation = (calculate_costs(from_date, until_date))
        
    elif calculation_type == 'losses':
        calculation = (calculate_losses(from_date, until_date))
    
    elif calculation_type == 'revenue':
        calculation = (calculate_revenue(from_date, until_date))
    
    elif calculation_type == 'profit':
        calculation = (calculate_profit(from_date, until_date))

    print('\n')
    return rprint(F"The '{calculation_type}' from the period '{from_date}' until '{until_date}' = '€ {calculation}'.\n")

# print(calculations())
# print('\n')


# User functions - display menu options: 'file', 'date' and 'product'.

def display_file_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'file options'[/bright_cyan] menu.\n")
    
    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the files!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'file options'[/bright_cyan] below to get started!")
    
    # Met onderstaande code maak je tabellen zonder lijnen.
    table.add_row('1', "Create a new file.")
    table.add_row('2', "Clear a file.")
    table.add_row('3', "Export a file to Excel.")
    table.add_row('4', "Exit")

    # LET OP!!! Met onderstaande code maak je tabellen met lijnen.
    # table.add_row("1", "Create a new file.")
    # table.add_row(Rule(style='white'), Rule(style='white'))
    # table.add_row("2", "Clear a file.")
    # table.add_row(Rule(style='white'), Rule(style='white'))
    # table.add_row("3", "Export a file to Excel.")
    # table.add_row(Rule(style='white'), Rule(style='white'))
    # table.add_row("4", "Exit")


    while True:

        console.print(table)
        print('\n')

        option = input("Enter one of the 4 options: ")
        print('\n')

        if option == '1':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            create_new_file()
            
        elif option == '2':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            clear_file()

        elif option == '3':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            export_file_to_excel()

        elif option == '4':
            rprint("[wheat1]Okay. You have chosen to exit the [green]'file options'[/green] menu. See you next time![/wheat1]\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 4.[/orange3]\n")
            
            continue
        break

# print(display_file_options())
# print('\n')


def display_date_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'date options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the dates!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')

    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'date options'[/bright_cyan] below to get started!")
    
    table.add_row('1', "Update the system date.")
    table.add_row('2', "Change the system date.")
    table.add_row('3', "Select a specific system date.")
    table.add_row('4', "Special occasion date / countdown.")
    table.add_row('5', "Exit")


    while True:
        
        console.print(table)
        print('\n')

        option = input("Enter one of the 5 options: ")
        print('\n')

        if option == '1':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            update_system_date()

        elif option == '2':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            change_system_date()

        elif option == '3':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            print(select_specific_date())
            # select_specific_date()        # LET OP!!! Wanneer je enkel en alleen de functie aanroept (dus zonder de functie te printen), krijg je 'None' als return i.p.v. de datum zoals ik dit in mijn 'select_specific_date()' functie heb\
                                            # aangegeven. FF uitzoeken waarom dit zo is.
            print('\n')
        
        elif option == '4':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            special_occasion_date()

        elif option == '5':
            rprint("[wheat1]Okay. You have chosen to exit the [green]'date options'[/green] menu. See you next time![/wheat1]\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 5.[/orange3]\n")

            continue
        break

# print(display_date_options())
# print('\n')


def display_product_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'product options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the products!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')
    
    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'product options'[/bright_cyan] below to get started!")

    table.add_row('1', "View all products.")
    table.add_row('2', "View products within a certain period.")
    table.add_row('3', "Find products.")
    table.add_row('4', "Avoid expired products.")
    table.add_row('5', "Add inventory products.")
    table.add_row('6', "Add sold products.")
    table.add_row('7', "Add loss products.")
    table.add_row('8', "Modify product details.")
    table.add_row('9', "Remove product.")
    table.add_row('10', "Exit")


    while True:
        
        console.print(table)
        print('\n')

        option = input("Enter one of the 10 options: ")
        print('\n')

        if option == '1':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            view_all_products()

        elif option == '2':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            view_products_within_period()

        elif option == '3':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            find_products()
        
        elif option == '4':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            avoid_expired_products()
        
        elif option == '5':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            add_inventory_products()
        
        elif option == '6':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            add_sold_products()
        
        elif option == '7':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            add_loss_products()
        
        elif option == '8':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            modify_product_details()
        
        elif option == '9':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            remove_product()
        
        elif option == '10':
            rprint("[wheat1]Okay. You have chosen to exit the [green]'product options'[/green] menu. See you next time![/wheat1]\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 10.[/orange3]\n")

            continue
        break

# print(display_product_options())
# print('\n')


def display_calculation_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'calculation options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the calculations!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'bold green')
    
    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'calculation options'[/bright_cyan] below to get started!")
    
    table.add_row('1', "Calculate the 'costs', 'losses', 'revenue' or 'profit'.")
    table.add_row('2', "Exit")


    while True:
        console.print(table)
        print('\n')

        option = input("Enter one of the 2 options: ")
        print('\n')

        if option == '1':
            rprint("[green]Great!:thumbs_up: You will now be directed to the selected option.[/green]\n")
            print('\n')
            calculations()

        elif option == '2':
            rprint("[wheat1]Okay. You have chosen to exit the [green]'calculation options'[/green] menu. See you next time![/wheat1]\n")
            break
        
        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 2.[/orange3]\n")

# print(display_calculation_options())
# print('\n')


if __name__ == "__main__":

    print('\n')
    
    # print(create_new_file())
    # print('\n')

    # print(clear_file())
    # print('\n')

    # print(export_file_to_excel())
    # print('\n')

    # print(update_system_date())
    # print('\n')

    # print(change_system_date())
    # print('\n')

    # print(go_to_specific_date())
    # print('\n')

    # print(special_occasion_date())
    # print('\n')

    # print(view_all_products())
    # print('\n')

    # print(view_products_within_period())
    # print('\n')

    # print(find_products())
    # print('\n')

    # print(avoid_expired_products())
    # print('\n')

    # print(add_inventory_products())
    # print('\n')

    # print(add_sold_products())
    # print('\n')

    # print(add_loss_products())
    # print('\n')

    # print(modify_product_details())
    # print('\n')

    # print(modify_product_quantity())
    # print('\n')

    # print(remove_product())
    # print('\n')

    # print(product_calculations())
    # print('\n')
    