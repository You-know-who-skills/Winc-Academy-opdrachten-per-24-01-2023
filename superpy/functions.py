# Imports

import csv
import sys
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


# User function – export file to Excel.

def export_file_to_excel():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'export file to Excel'[/bright_cyan] option. With this option, you can export a selected file to an Excel file.\n")

        print("- Follow the step(s) below to export a selected file to an 'Excel' file. Have fun exporting!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")
        
        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

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
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/dark_sea_green4]\n")

            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/dark_sea_green4]\n")
                
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found and it is exported to an Excel file.[/dark_sea_green4]\n")

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
    except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


# Help functions – convert and use dates.

def current_date():
    '''
    Returns the 'current date' in the '.today()' method way.
    '''

    return datetime.today()


def convert_to_strptime(datetime_object: datetime):
    '''
    Converts a Dutch date string in to a datetime object.
    '''

    return datetime.strptime(datetime_object, "%d-%m-%Y")


def convert_to_strftime(string: datetime):
    '''
    Converts a datetime object in to a string.
    '''

    return datetime.strftime(string, "%d-%m-%Y")


def convert_to_dutch_date(date_format: datetime):
    '''
    Converts a datetime object in to a Dutch date string: dd-mm-yyyy.
    '''

    return datetime.strptime(date_format, "%d-%m-%Y").strftime("%d-%m-%Y")


# User function – update system date.

def update_system_date():
    
    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'update the system date'[/bright_cyan] option. With this option you can update the system date to the current date.\n")
        
        print("- Follow the step(s) below to update the system date. Have fun updating!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'update the system date'")
            
        table.add_row("- Step 1 = Confirm if you 'do' or 'don't' want to update the system date to the current date, by entering 'Y' for Yes or 'N' for No (not case sensitive).")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            update_system = (input("Step 1 = Confirm if you 'do' or 'don't' want to update the system date to the current date, by entering 'Y' for Yes or 'N' for No (not case sensitive): ")).lower()
            print('\n')

            if update_system == "y":
                rprint("[dark_sea_green4]Great!:thumbs_up: The date of the system has been updated to the current date. You can see the current date below.[/dark_sea_green4]\n")

            elif update_system == "n":
                rprint("[wheat1]:person_gesturing_NO: Okay! The date of the system will not be updated to the current date.[/wheat1]\n")
            
            else:
                rprint(F"[orange3]:scream: Hello user! '{update_system}' isn't the correct input for updating the system date to the 'current date'. Please enter 'Y' if you 'do' or 'N' if you 'don't' want to update the system date to the\
 'current date' (not case sensitive).[/orange3]\n")
                
                continue
            break


        today_date_datetime = current_date()

        if update_system == "y":
            today_date_string = convert_to_strftime(today_date_datetime)

            print(today_date_string)
            print('\n')

            with open('date_file.txt', 'w') as date_file:

                date_file.write(today_date_string)
    
    except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


# User function – change system date.

def change_system_date():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'change the system date'[/bright_cyan] option.\n")
            
        print("- Follow the step(s) below to change the system date by entering the number of 'days' or 'weeks' that you want to change the system date with. Have fun changing!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'change the system date'")
            
        table.add_row("- Step 1 = Enter 'days' if you want to change the system date in a period of 'days', or enter 'weeks' if you want to change the system date in a period of 'weeks' (not case sensitive).")
        table.add_row("- Step 2 = Enter 'past' if you want the system date to go in the 'past' or enter 'future' if you want the system date to go in to the 'future' (not case sensitive).")
        table.add_row("- Step 3 = Enter a 'number' for the couple of 'days' or 'weeks' that you want to change the system date with in the 'past' or 'future'.")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            days_or_weeks = input("Step 1 = Enter 'days' if you want to change the system date in a period of days. Or enter 'weeks' if you want to change the system date in a period of weeks (not case sensitive): ").lower()
            print('\n')

            if days_or_weeks == 'days' or days_or_weeks == 'weeks':
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Let's change the system date for a couple of '{days_or_weeks}'.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! '{days_or_weeks}' isn't the correct input to modify the system date. Please enter 'days' or 'weeks' for the correct system date modification.[/orange3]\n")

                continue
            break


        while True:
            past_or_future = input("Step 2 = Enter 'past' if you want the system date to go in the 'past', or enter 'future' if you want the system date to go in to the 'future' (not case sensitive): ").lower()
            print('\n')

            if past_or_future == 'past' or past_or_future == 'future':
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Let's change the system date for a couple of '{days_or_weeks}' in the '{past_or_future}'.[/dark_sea_green4]\n")

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

        return rprint(F"[dark_sea_green4]Great!:thumbs_up: If we go '{number}' '{days_or_weeks}' into the '{past_or_future}', the date = [bright_cyan]'{string_date}'[/bright_cyan][/dark_sea_green4]\n\n")
    
    except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


# User function – select specific date.

def select_specific_date():
    
    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'select a specific system date'[/bright_cyan] option. With this option you can go to a specific date in the system. Have fun selecting!\n")
        
        print("- Follow the step(s) below to go to a specific date in the system. Have fun selecting!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'select a specific system date'")

        table.add_row("- Step 1 = Enter the 'date' you want the system to go to as follows: 'dd-mm-yyyy'.")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            specific_date = (input("Enter the 'date' you want the system to go to as follows 'dd-mm-yyyy': "))
            print('\n')

            try:
                convert_to_dutch_date(specific_date)
                
            except ValueError:
                rprint(F"[orange3]:scream: Hello user! '{specific_date}' isn't the correct way to fill in the 'specific system date'. Please enter the 'specific date' as follows: dd-mm-yyyy.[/orange3]\n")
                
                continue
            break


        with open('date_file.txt', 'w') as date_file:

            date_file.write(specific_date)
            rprint("[dark_sea_green4]Great!:thumbs_up: The date of the system has been changed to the specific date. You can see the 'specific system date' below.[/dark_sea_green4]\n")

        return rprint(F"[bright_cyan]{specific_date}[/bright_cyan]\n\n")
    
    except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


# User function – special occasion date.

def special_occasion_date():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'special occasion countdown'[/bright_cyan] option.\n")

        print("- Follow the step(s) below to create a countdown for a 'special occasion'. Have fun with the countdown!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")
        
        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

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
                rprint(F"[orange3]:scream: Hello user! '{special_occasion_date}' Isn't the correct way to fill in the 'date' for the 'special occasion countdown'. Please enter the 'date' for the 'special occasion countdown' as follows:\
 dd-mm-yyyy.[/orange3]\n")
                
                continue
            

            input_date = convert_to_strptime(special_occasion_date)
            todays_date = current_date()                           

            if input_date > todays_date:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The 'date' for the 'special occasion countdown': '{special_occasion_date}', has been filled in correctly.[/dark_sea_green4]\n")

            elif input_date < todays_date:                                    
                rprint(F"[orange3]:scream: Hello user! The 'date' you've just entered: '{special_occasion_date}', is a date in the past. And we're not able to time travel... yet.:wink: Please enter the correct 'date' for the 'special\
 occasion countdown' as follows: dd-mm-yyyy.[/orange3]\n")
                
                continue
            break


        special_occasion_sentence = input("Step 2 = Type a 'sentence' that you want to add to the 'special occasion countdown' (for instance: Until Christmas!!!): ")
        print('\n')


        with open('special_occasion.txt', 'w') as file:
        
            datetime_countdown = input_date - todays_date                                                                                                       
            rprint(F"[wheat1]Original countdown in days, hours, minutes, seconds and micro seconds = [bright_cyan]{datetime_countdown}[/bright_cyan][/wheat1]") 
            print('\n')

            full_string_countdown = str(datetime_countdown)

            short_string_countdown = full_string_countdown[0:full_string_countdown.find(',')]
            file.write(F"{short_string_countdown.upper()} {special_occasion_sentence}")

        return rprint(F"[dark_sea_green4]Great!:thumbs_up: You can see the 'date' and the 'sentence' for the 'special occasion countdown' below.\n\n[bright_cyan]{short_string_countdown.upper()} {special_occasion_sentence}[/bright_cyan]\
[/dark_sea_green4]\n\n")

    except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


# Help function – column name check.

def column_name_check(file_name: str):
    '''
    Returns the first row of a CSV file.
    '''
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)

        check_column_name = next(reader)

        rprint(F"[magenta]These are the all the 'product detail names' in the '{file_name.capitalize()[:-4]}' file:[/magenta]")
        rprint(F"[bright_cyan]{check_column_name}[/bright_cyan]")
        print('\n')

    return check_column_name


# Help function – product in file check.

def product_in_file_check(file_name: str, search_type: str):
    '''
    Returns 'True' if a product is found in the selected CSV\
    file and also shows the row(s) in which the product\
    is located.
    '''

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        product_in_file = False

        rprint(F"[magenta]Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file:[/magenta]")

        for row in rows:
            if row['name'] == search_type or row['id'] == search_type:
            
                product_in_file = True
                rprint(F"[bright_cyan]{row}[/bright_cyan]")

        print('\n')
        
        if product_in_file == True:
            return True
        
        elif product_in_file == False:
            rprint("[bright_cyan]{No products found}[/bright_cyan]\n")


# Help function – product detail check.

def product_detail_check(file_name: str, search_type: str, column_name: str):
    '''
    This function:
    - searches for data / product details of a selected product in a selected\
      column in a selected CSV file;
    - returns the found data / product details from the selected column.
    '''

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        column_name_results = []

        for row in rows:
            if row['name'] == search_type or row['id'] == search_type:
                
                column_name_results.append(row[column_name])
            
    return column_name_results


# Help function – show product details.

def show_product_details(file_name: str, search_type: str, expiration_date: str):
    '''
    Shows the details of a product based on the expiration date in a selected CSV file.
    '''

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        rprint(F"[magenta]Product details of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file:[/magenta]")

        for categorize, row in enumerate(rows, start=2):
            
            if (row['name'] == search_type or row['id'] == search_type) and row['expiration_date'] == expiration_date:
                rprint(F"[bright_cyan]{categorize}. {row}[/bright_cyan]")

    print('\n')


# User function – avoid expired products.

def	avoid_expired_products():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'avoid expired products'[/bright_cyan] option.\n")
        
        rprint("- [bright_cyan]Please follow the step(s) below every day to avoid expired products. In this way you can help our planet :globe_showing_Europe-Africa: by not wasting products and you can also help people who are less\
 fortunate.:handshake: Have fun in helping to make our world :globe_showing_Europe-Africa: a better and durable place!:muscle:[/bright_cyan]\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'avoid expired products'")
            
        table.add_row("- Step 1 = Confirm if you 'do' or 'don't' want to check for products that will expire within 3 days in the 'Inventory' file, by entering 'Y' for Yes or 'N' for No (not case sensitive).")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            yes_or_no = input("Step 1 = Confirm if you 'do' or 'don't' want to check for products that will expire within 3 days in the 'Inventory' file, by entering 'Y' for Yes or 'N' for No (not case sensitive): ").lower()
            print('\n')

            if yes_or_no == "y":
                rprint("[dark_sea_green4]Great!:thumbs_up: You can see the search result(s) of the products that will expire within [bright_cyan]3[/bright_cyan] days below.[/dark_sea_green4]\n")
                
                rprint("[dark_sea_green4]Please think of a durable way to use these products before they expire. Thanks in advance for helping to make our world :globe_showing_Europe-Africa: a better and durable place.:muscle: :thumbs_up:\
[red]:red_heart:[/red][/dark_sea_green4]\n\n")
                

            elif yes_or_no == "n":
                rprint("[wheat1]:person_gesturing_NO: Okay! The products that will expire within [dark_sea_green4]3[/dark_sea_green4] days will not be shown.[/wheat1]\n")
                
            else:
                rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' isn't the correct input for checking the products that will expire within 3 days. Please enter 'Y' for Yes if you 'do', or 'N' for No if you 'don't' want to check for\
 products that will expire within 3 days (not case sensitive).[/orange3]\n")

                continue
            break


        with open('inventory.csv', 'r') as inventory_file:
            reader = csv.DictReader(inventory_file)
            rows = list(reader)

            avoid_waste_list = []
            
            for categorize, row in enumerate(rows, start=2):

                today_date = current_date().strftime("%d-%m-%Y")
                
                today_date_without_time = convert_to_strptime(today_date)
                
                expire_date = convert_to_strptime(row['expiration_date'])
                
                expire_days = today_date_without_time + timedelta(3)
                
                if yes_or_no == 'y' and expire_date >= today_date_without_time and expire_date < expire_days:
                    avoid_waste_list.append(row)
                    rprint(F"   [bright_cyan]{categorize}. {row}[/bright_cyan]\n")

            if yes_or_no == 'y' and len(avoid_waste_list) == 0:
                rprint(F"   [bright_cyan]There are no products found that will expire within [dark_sea_green4]3[/dark_sea_green4] days.[/bright_cyan]\n")
                
                rprint("[dark_sea_green4]So good job on helping to make our world :globe_showing_Europe-Africa: a better and durable place.:thumbs_up: :muscle: [red]:red_heart:[/red][/dark_sea_green4]\n")
                
            print('\n')
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# Help function – daily expiration check.

def	daily_expiration_check():

    with open('inventory.csv', 'r') as inventory_file:
        reader = csv.DictReader(inventory_file)
        rows = list(reader)

        avoid_waste_list = []

        rprint("[dark_sea_green4]This is your daily automated [bright_cyan]'product expiration date check'[/bright_cyan]. If there are products in your 'Inventory' file that will expire within [bright_cyan]3[/bright_cyan] days including\
 today, they will appear below.[/dark_sea_green4]\n")
                
        rprint("[dark_sea_green4]Please think of a durable way to use these products before they expire. Thanks in advance for helping to make our world :globe_showing_Europe-Africa: a better and durable place.:muscle: :thumbs_up:\
 [red]:red_heart:[/red][/dark_sea_green4]\n\n")
        
        for categorize, row in enumerate(rows, start=2):

            today_date = current_date().strftime("%d-%m-%Y")
            
            today_date_without_time = convert_to_strptime(today_date)
            
            expire_date = convert_to_strptime(row['expiration_date'])
            
            expire_days = today_date_without_time + timedelta(3)
            
            if expire_date >= today_date_without_time and expire_date < expire_days:
                avoid_waste_list.append(row)
                rprint(F"   [bright_cyan]{categorize}. {row}[/bright_cyan]\n")
            
        if len(avoid_waste_list) == 0:
            rprint("[bright_cyan]   There are no products found in the 'Inventory' file that will expire within [dark_sea_green4]3[/dark_sea_green4] days.[/bright_cyan]\n")
            
            rprint("[dark_sea_green4]So good job on helping to make our world :globe_showing_Europe-Africa: a better and durable place.:thumbs_up: :muscle: [red]:red_heart:[/red][/dark_sea_green4]\n")


# User function – view all products.

def view_all_products():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'view all products'[/bright_cyan] option. You can view all the products from one of the following files: 'Inventory', 'Sales' or 'Losses'.\n")

        print("- Follow the step(s) below to view all products from a selected file. Have fun viewing!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'view all of the products from a selected file'")
            
        table.add_row("- Step 1 = Enter one of the following file names to view all its products: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            file_name = input("Step 1 = Enter one of the following file names to view all its products: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
            print('\n')

            if file_name == 'inventory':
                file_name = 'inventory.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products of the '{file_name.capitalize()[:-4]}' file below![/dark_sea_green4]\n")

            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products of the '{file_name.capitalize()[:-4]}' file below![/dark_sea_green4]\n")
                
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found. You can see all the products of the '{file_name.capitalize()[:-4]}' file below![/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

                continue
            break


        with open(file_name, 'r+') as file:
                reader = csv.reader(file)
                rprint(F"   [bright_cyan]{next(reader)}[/bright_cyan]")

                for categorize, row in enumerate(reader, start=1):
                    rprint(F"[bright_cyan]{categorize}[/bright_cyan]. [dark_sea_green4]{row}[dark_sea_green4]\n")
                
                print('\n')
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – view product dates.

def view_product_dates():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'view products based on a specific date'[/bright_cyan] option.\n")

        rprint("- Follow the [grey78]step(s)[/grey78] below to view the products from a selected file based on one of the following dates: 'purchase date', 'sales date', 'loss date' or 'expiration date', within a selected period. Have fun\
 viewing!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'view products based on a specific date'")
            
        table.add_row("- Step 1 = Enter one of the followoing file names to view its products: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
        table.add_row("- Step 2 = Enter one of the followoing dates that you would like to view within a certain period: 'purchase date', 'sales date', 'loss date' or 'expiration date' (not case sensitive).")
        table.add_row("- Step 3 = Enter the 'from date' as follows: dd-mm-yyyy.")
        table.add_row("- Step 4 = Enter the 'until date' as follows dd-mm-yyyy.")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            file_name = input("Step 1 = Enter one of the followoing file names to view its products: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
            print('\n')

            if file_name == 'inventory':
                file_name = 'inventory.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
                
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")

                continue
            break


        # Variables to select the correct 'relevant date' in the 'while loop' / 'step 2' below.
        if file_name == 'inventory.csv':
            date_in_file = 'purchase date'

        elif file_name == 'sales.csv':
            date_in_file = 'sales date'

        elif file_name == 'losses.csv':
            date_in_file = 'loss date'


        while True:
            date_type = input(F"Step 2 = Enter one of the following dates from the '{file_name.capitalize()[:-4]}' file that you would like to view within a certain period: '{date_in_file}' or 'expiration date' (not case sensitive): ").lower()
            print('\n')

            if date_type == 'expiration date':
                date_in_file = 'expiration date'
            
            if date_type == date_in_file:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: It's noted that you want to view the '{date_in_file}' of the products from the '{file_name.capitalize()[:-4]}' file within a certain period.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! '{date_type}' Isn't the correct 'input date' to view the products from the '{file_name.capitalize()[:-4]}' file. Please enter '{date_in_file}' or 'expiration date' to view the products\
 within a certain period (not case sensitive).[/orange3]\n")

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

            # Variables to select the correct 'relevant date' in the 'relevant file' for the 'for loop' below.
            if file_name == 'inventory.csv':
                relevant_date = 'purchase_date'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Below you can see the search results of all the products with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' from the\
    '{file_name.capitalize()[:-4]}' file.[/dark_sea_green4]\n")

            elif file_name == 'sales.csv':
                relevant_date = 'sales_date'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Below you can see the search results of all the products with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' from the\
    '{file_name.capitalize()[:-4]}' file.[/dark_sea_green4]\n")

            elif file_name == 'losses.csv':
                relevant_date = 'loss_date'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Below you can see the search results of all the products with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' from the\
    '{file_name.capitalize()[:-4]}' file.[/dark_sea_green4]\n")
            
            if date_type == 'expiration date':
                relevant_date = 'expiration_date'


            relevant_date_list = []

            for categorize, row in enumerate(reader, start=1):
            
                file_date = convert_to_strptime(row[relevant_date])
                
                input_from_date = convert_to_strptime(from_date)
                
                input_until_date = convert_to_strptime(until_date)
                
                if input_from_date <= file_date and input_until_date >= file_date:
                    relevant_date_list.append(row)
                    rprint(F"   [bright_cyan]{categorize}. {row}[/bright_cyan]\n")
                    
            if len(relevant_date_list) == 0:
                rprint(F"   [wheat1]:person_gesturing_NO: There were no products found with '{date_in_file}s' between '{convert_to_dutch_date(from_date)}' and '{convert_to_dutch_date(until_date)}' in the '{file_name.capitalize()[:-4]}'\
    file.[/wheat1]\n")
            
            print('\n')
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – find products.

def find_products():
    
    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'find products'[/bright_cyan] option. You can search for a product in one of the following files: 'Inventory', 'Sales' or 'Losses'.\n")
        
        print("- Follow the step(s) below to find the product you are looking for. Have fun finding!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'find products in a selected file'")

        table.add_row("- Step 1 = Enter one of the following file names to find the product you are looking for: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
        table.add_row("- Step 2 = Enter the product 'ID' or 'name' (the product name is not case sensitive).")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            file_name = input("Step 1 = Enter one of the following file names to find the product you are looking for: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
            print('\n')

            if file_name == 'inventory':
                file_name = 'inventory.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
                
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n")
                
                continue
            break


        while True:
            search_type = (input("Step 2= Enter the product 'ID' or 'name' (the product name is not case sensitive): ")).lower()
            print('\n')
            
            if product_in_file_check(file_name, search_type) == True:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' of product '{search_type}' above.[/dark_sea_green4]\n\n")
            
            else:
                rprint(F"[orange3]:scream: Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct product 'name' or 'ID' (the product name is not case sensitive).[/orange3]\n")
                
                continue
            break
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – add inventory products.

def add_inventory_products():
    
    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'add inventory products'[/bright_cyan] option.\n")
        
        print("- Follow the step(s) below to add products to the Inventory file. Have fun adding!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

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
                rprint(F"[orange3]:scream: Hello user! The product 'ID' can only contain numbers. '{id}' Doesn't only contain numbers. Please enter a product 'ID' that only contains numbers.[/orange3]\n\n")
                
                continue

            if len(id) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'ID' can't contain more than '{maximum_digits}' digits. The entered ID: '{id}', contains more than '{maximum_digits}' digits. Please enter an 'ID' that contains no more than\
 '{maximum_digits}' digits.[/orange3]\n\n")

                continue
            
            print('\n')
            id_check = product_in_file_check('inventory.csv', id)
            
            if id_check == True:
                rprint(F"[wheat1]:thinking_face: Please note that product ID [bright_cyan]{id}[/bright_cyan] already exists in the 'Inventory' file. You can see the 'product details' of the existing product ID [bright_cyan]{id}[/bright_cyan]\
 above.[/wheat1]\n\n")

            else:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The product ID '{id}' hasn't been used before in the 'Inventory' file.[/dark_sea_green4]\n\n")
            break


        while True:
            name = input(F"Step 2 = Enter the 'name' for product ID '{id}' (not case sensitive): ").lower()

            print('\n')
            name_check = product_in_file_check('inventory.csv', name)
            
            if name_check == True:
                rprint(F"[wheat1]:thinking_face: Please note that product name [bright_cyan]{name}[/bright_cyan] already exists in the 'Inventory' file. You can see the 'product details' of the existing product name [bright_cyan]{name}\
[/bright_cyan] above.'[/wheat1]\n\n")
                
            else:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The product name '{name}' hasn't been used before in the 'Inventory' file.[/dark_sea_green4]\n\n")
            break


        while True:
            purchase_quantity = input(F"Step 3 = Enter the 'purchase quantity' for product '{name}': ")
            
            try:
                int(purchase_quantity)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'purchase quantity' for product '{name}' can only contain numbers. '{purchase_quantity}' Doesn't only contain numbers. Please enter the correct 'purchase quantity' for product\
 '{name}'.[/orange3]\n\n")            
                
                continue

            if len(purchase_quantity) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'purchase quantity' can't contain more than '{maximum_digits}' digits. The entered 'purchase quantity': '{purchase_quantity}', contains more than '{maximum_digits}' digits. Please\
 enter a 'purchase quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")

                continue
            break


        while True:
            purchase_amount = input(F"Step 4 = Enter the 'purchase amount' for product '{name}' and use a dot in stead of a comma to seperate any decimals: ")
            
            try:
                float(purchase_amount)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{purchase_amount}' Doesn't contain an 'amount' and / or a 'dot' to seperate the decimals. Please enter the correct 'purchase amount' for product '{name}' and use a dot (in stead of a\
 comma) to seperate any decimals.[/orange3]\n\n")

                continue

            input_amount = float(purchase_amount)
            decimal_quantity = round(input_amount, 2)

            if input_amount != decimal_quantity:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'purchase amount' again and only add '2 decimals' when necessary.[/orange3]\n\n")

                continue

            elif len(purchase_amount) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'purchase amount' can't contain more than '{maximum_digits}' digits. The entered 'purchase amount': '{purchase_amount}', contains more than '{maximum_digits}' digits. Please enter a\
 'purchase amount' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")
                
                continue
            break


        while True:
            purchase_date = input(F"Step 5 = Enter the 'purchase date' of product '{name}' as follows: dd-mm-yyyy: ")
            
            try:
                convert_to_dutch_date(purchase_date)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{purchase_date}' Isn't the correct way to fill in the 'purchase date'. Please enter the correct 'purchase date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue
            
            input_date = convert_to_strptime(purchase_date)

            if input_date > current_date():
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The date you just entered: '{purchase_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'purchase date' for product '{name}'.\
[/orange3]\n\n")

                continue
            break


        # The 3 variables below are to create the 'tomorrow_date' variable which is a notification code for when the expiration date of a product is tomorrow. This will help the user to avoid wasting products. See from the 1st 'elif statement'\
        # in 'step 6' below.
        today_date = current_date().date()
        
        tomorrow_date = today_date + timedelta(1)   

        while True:
            expiration_date = input(F"Step 6 = Enter the 'expiration date' of product '{name}' as follows: dd-mm-yyyy: ")
            
            try:
                expiration = convert_to_strptime(expiration_date).date()
            
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date'. Please enter the correct 'expiration date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue
            
            if expiration < today_date:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! Product '{name}' is rotton.:scream: So please throw it away a.s.a.p. or enter the correct expiration date for product '{name}'.[/orange3]\n\n")
                
                continue
            
            elif expiration == today_date:
                print('\n')
                rprint(F"[wheat1]:astonished_face: Hello user! The 'expiration date' of product [bright_cyan]{name}[/bright_cyan] is today.:astonished_face: So you can either: 1: enter the correct expiration date, 2: put it on sale or 3:\
 think of a durable way to do something with product [bright_cyan]{name}[/bright_cyan].[/wheat1]")

            elif expiration == tomorrow_date:
                print('\n')
                rprint(F"[wheat1]:thinking_face: Hello user! The 'expiration date' of product [bright_cyan]{name}[/bright_cyan] is tomorrow.:thinking_face: So you can either: 1: enter the correct expiration date, 2: put it on sale or 3:\
 think of a durable way to do something with product [bright_cyan]{name}[/bright_cyan].[/wheat1]")

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
                writer.writerows(rows)
                print('\n')                        
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The quantity of product '{name}' has been updated, because the 'ID', the 'name', the 'purchase amount', 'the purchase date' and the 'expiration date' are the same. You can check the\
 'product details' below.[/dark_sea_green4]\n")
                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                print('\n')

            else:
                with open('inventory.csv', 'a+', newline='') as inventory_file:
                    writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
                    writer.writerow(product_details)
                    
                    print('\n')
                    rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{name}' has been added to the 'Inventory' file. You can check the 'product details' below.[/dark_sea_green4]\n")
                    rprint(F"   [bright_cyan]{product_details}[/bright_cyan]")
                    print('\n')

    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – add sold products.

def add_sold_products():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'add sold products'[/bright_cyan] option.\n")
        
        print("- By adding a sold product to the 'Sales' file, your 'Inventory' file will automatically be reduced with the same quantity of the products that you've sold.\n")
        
        print("- Follow the step(s) below to add your sold products. Have fun adding!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

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
            print('\n')
            
            if id in product_detail_check('inventory.csv', id, 'id'):
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product ID '{id}' is found in the 'Inventory' file. You can see the 'product details' of product ID '{id}' below.[/dark_sea_green4]\n")
            
            else:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The entered product ID: '{id}', was not found in the 'Inventory' file. You can only add a 'sold product' to the 'Sales' file if the product 'ID' is also found in the 'Inventory' file.\
 Please enter the correct product 'ID'.[/orange3]\n\n")

                continue
            break


        print('\n')
        product_in_file_check('inventory.csv', id)

        while True:
            name = (input("Step 2 = Enter the product 'name' as shown above in the 'product details' (not case sensitive): ")).lower()
            print('\n')

            if name in product_detail_check('inventory.csv', id, 'name'):
                product_in_file_check('inventory.csv', name)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product name '{name}' matches with the product ID '{id}' of this product in the 'Inventory' file. You can see the 'product details' of product '{name}' above.[/dark_sea_green4]\n\n")

            else:
                product_in_file_check('inventory.csv', id)
                rprint(F"[orange3]:scream: Hello user! The entered product 'name': '{name}', doesn't match with product ID '{id}' from the 'Inventory' file. You can only add a 'sold product' to the 'Sales' file if the product 'name'\
 matches the name of this product in the 'Inventory' file. Please check the 'product details' above for the correct product 'name' (not case sensitive).[/orange3]\n\n")

                continue
            break


        while True:
            sold_quantity = (input(F"Step 3 = Enter the 'sold quantity' of product '{name}': "))

            try:
                int(sold_quantity)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'sold quantity' can only contain numbers. '{sold_quantity}' Doesn't only contain numbers. Please enter the correct 'sold quantity' for product '{name}'.[/orange3]\n\n")
                
                continue

            if len(sold_quantity) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'sold quantity' can't contain more than '{maximum_digits}' digits. The entered 'sold quantity': '{sold_quantity}', contains more than '{maximum_digits}' digits. Please enter a 'sold\
 quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")
            
                continue
            break


        while True:
            sales_amount = (input(F"Step 4 = Enter the 'sales amount' of product '{name}' and use a dot in stead of a comma to seperate any decimals: "))

            try:
                float(sales_amount)
                
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{sales_amount}' Doesn't contain an 'amount' and / or a 'dot' to seperate the decimals. Please enter the correct 'sales amount' for product '{name}' and use a 'dot' (in stead of a comma)\
 to seperate any decimals.[/orange3]\n\n")

                continue
            
            input_amount = float(sales_amount)
            decimal_quantity = round(input_amount, 2)

            if input_amount != decimal_quantity:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'sales amount' again and only add '2 decimals' when necessary.[/orange3]\n\n")

                continue

            elif len(sales_amount) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'sales amount' can't contain more than '{maximum_digits}' digits. The entered 'sales amount': '{sales_amount}', contains more than '{maximum_digits}' digits. Please enter a 'sales\
 amount' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")        

                continue
            break


        while True:
            sales_date = (input(F"Step 5 = Enter the 'sales date' of product '{name}' as follows: dd-mm-yyyy: "))

            try:
                convert_to_dutch_date(sales_date)
            
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{sales_date}' Isn't the correct way to fill in the 'sales date'. Please enter the correct 'sales date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue
            
            input_date = convert_to_strptime(sales_date)

            if input_date > current_date():
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'sales date' you just entered: '{sales_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'sales date' for product '{name}'.\
[/orange3]\n\n")

                continue
            break


        print('\n')
        product_in_file_check('inventory.csv', name)

        while True:
            expiration_date = (input(F"Step 6 = Enter the 'expiration date' of product '{name}' as shown above in the 'product details' as follows: dd-mm-yyyy: "))

            try:
                expiration = convert_to_dutch_date(expiration_date)
                
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date'. Please enter the correct 'expiration date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue
            
            expiration_date_check = product_detail_check('inventory.csv', name, 'expiration_date')

            if expiration_date in expiration_date_check:
                print('\n')
                product_in_file_check('inventory.csv', name)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{name}' in the 'Inventory file'. You can see all the 'expiration dates' of\
 product '{name}' in the 'product details' shown above.[/dark_sea_green4]\n")

                if expiration == current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:astonished_face: Please note that the entered expiration date [bright_cyan]{expiration_date}[/bright_cyan] of the sold product with product ID [bright_cyan]{id}[/bright_cyan] and product name\
[bright_cyan]{name}[/bright_cyan] is today.:astonished_face:[/wheat1]")

                if expiration < current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:scream: Please note that the entered expiration date [bright_cyan]{expiration_date}[/bright_cyan] of the sold product with product ID [bright_cyan]{id}[/bright_cyan] and product name\
[bright_cyan]{name}[/bright_cyan] has expired.:scream:[/wheat1]")

            else:
                print('\n')
                product_in_file_check('inventory.csv', name)
                rprint(F"[orange3]:scream: Hello user! The entered expiration date: '{expiration_date}', doesn't match one of the 'expiration dates' of product '{name}' in the 'Inventory file'. Please check the 'product details' above for\
 the correct 'expiration date'.[/orange3]\n\n")

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
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The 'sold quantity' of product '{name}' has been 'updated', because: the 'ID', the 'name', the 'sales amount' the 'sales date' and the 'expiration date' are the same. You can check the\
 updated details below.[/dark_sea_green4]\n")
                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                print('\n')
                
            else:    
                with open('sales.csv', 'a+', newline='') as sales_file:
                    writer = csv.DictWriter(sales_file, fieldnames= reader.fieldnames)
                    writer.writerow(product_details)
                    print('\n')
                    rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the 'sales' file. You can check the details below.[/dark_sea_green4]\n")
                    rprint(F"   [bright_cyan]{product_details}[/bright_cyan]")
                    print('\n')


        with open('inventory.csv', 'r+', newline='') as inventory_file:
            reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
            rows = list(reader)
            
            for row in rows[1:]:
                
                if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                    row['purchase_quantity'] = int(row['purchase_quantity']) - int(sold_quantity)

                    if row['purchase_quantity'] >0 and row['purchase_quantity'] < 3:
                        rprint(F"[wheat1]STOCK UPDATE!!!:astonished_face: The product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date\
[bright_cyan]{row['expiration_date']}[/bright_cyan] needs to be reordered, because there are / is [bright_cyan]{row['purchase_quantity']}[/bright_cyan] left in stock.:astonished_face:[/wheat1]\n\n")

                    elif row['purchase_quantity'] <= 0:
                            row['purchase_quantity'] = 0
                            rprint(F"[wheat1]STOCK UPDATE!!!:scream: Product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date [bright_cyan]{row['expiration_date']}\
[/bright_cyan] needs to be reordered, because there is [bright_cyan]{row['purchase_quantity']}[/bright_cyan] / [bright_cyan]nothing[/bright_cyan] left in stock.:scream:[/wheat1]\n\n")
            
                    else:
                        rprint(F"[dark_sea_green4]STOCK UPDATE!!!:thumbs_up: Product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date\
[bright_cyan]{row['expiration_date']}[/bright_cyan] doesn't need to be reordered, because there are [bright_cyan]{(row['purchase_quantity'])}[/bright_cyan] left in stock.:grinning_face_with_big_eyes:[/dark_sea_green4]\n\n")


        with open('inventory.csv', 'r+', newline='') as inventory_file:
            writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
            writer.writerows(rows)
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – add loss products.

def add_loss_products():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'add product losses'[/bright_cyan] option.\n")

        print("- By adding a product loss to the Losses file, the Inventory file will automatically be reduced with the same quantity of the added product loss.\n")

        print("- Follow the step(s) below to add a product loss. Have fun adding!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'add products to the Losses file'")
            
        table.add_row("- Step 1 = Enter the product 'ID'.")
        table.add_row("- Step 2 = Enter the product 'name' (not case sensitive).")
        table.add_row("- Step 3 = Enter the product 'loss quantity'.")
        table.add_row("- Step 4 = Enter the product 'loss amount' and use a dot in stead of a comma to seperate any decimals.")
        table.add_row("- Step 5 = Enter the product 'loss date' as follows: dd-mm-yyyy.")
        table.add_row("- Step 6 = Enter one of the following 'causes of loss' options: 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).")
        table.add_row("- Step 7 = Enter the product 'expiration date' as follows: dd-mm-yyyy.")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        maximum_digits = '15'

        while True:
            id = (input("Step 1 = Enter the product 'ID': "))
            print('\n')

            if id in product_detail_check('inventory.csv', id, 'id'):
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product ID '{id}' is found in the 'Inventory' file. You can see the 'product details' of product ID '{id}' below.[/dark_sea_green4]\n")
            
            else:
                rprint(F"[orange3]:scream: Hello user! The entered product ID: '{id}', was not found in the 'Inventory' file. You can only add a 'loss product' to the 'Losses' file if the product 'ID' is also found in the 'Inventory' file.\
 Please enter the correct product 'ID'.[/orange3]\n\n")

                continue
            break 


        print('\n')
        product_in_file_check('inventory.csv', id)

        while True:
            name = (input("Step 2 = Enter the product 'name' as shown above in the 'product details' (not case sensitive): ")).lower()
            print('\n')

            if name in product_detail_check('inventory.csv', id, 'name'):
                product_in_file_check('inventory.csv', name)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product name '{name}' matches with the product ID '{id}' of this product in the 'Inventory' file. You can see the 'product details' of product '{name}' above.[/dark_sea_green4]\n\n")

            else:
                product_in_file_check('inventory.csv', id)
                rprint(F"[orange3]:scream: Hello user! The entered product name: '{name}', doesn't match with product ID '{id}' from in the 'Inventory' file. You can only add a 'loss product' to the 'Losses' file if the product 'name'\
 matches the name of this product in the 'Inventory' file. Please check the 'product details' above for the correct product 'name' (not case sensitive).[/orange3]\n\n")

                continue
            break


        while True:
            loss_quantity = (input(F"Step 3 = Enter the 'loss quantity' of product '{name}': "))
            
            try:
                int(loss_quantity)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'loss quantity' can only contain numbers. '{loss_quantity}' Doesn't only contain numbers. Please enter the correct 'loss quantity' for product '{name}'.[/orange3]\n\n")
                
                continue

            if len(loss_quantity) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'loss quantity' can't contain more than '{maximum_digits}' digits. The entered 'loss quantity': '{loss_quantity}', contains more than '{maximum_digits}' digits. Please enter a 'loss\
 quantity' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")
                
                continue
            break


        while True:
            loss_amount = (input(F"Step 4 = Enter the 'loss amount' of product '{name}' and use a dot in stead of a comma to seperate any decimals: "))
            
            try:
                float(loss_amount)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{loss_amount}' Doesn't contain an 'amount' and / or a 'dot' to seperate the decimals. Please enter the correct 'loss amount' for product '{name}' and use a 'dot' (in stead of a comma)\
 to seperate any decimals.[/orange3]\n\n")
                
                continue

            input_amount = float(loss_amount)
            decimal_quantity = round(input_amount, 2)
            
            if input_amount != decimal_quantity:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the 'loss amount' again and only add '2 decimals' when necessary.[/orange3]\n\n")
                
                continue

            elif len(loss_amount) > 15:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The 'loss amount' can't contain more than '{maximum_digits}' digits. The entered 'loss amount': '{loss_amount}', contains more than '{maximum_digits}' digits. Please enter a 'loss\
 amount' that contains no more than '{maximum_digits}' digits.[/orange3]\n\n")

                continue
            break


        while True:
            loss_date = (input(F"Step 5 = Enter the 'loss date' of product '{name}' as follows: dd-mm-yyyy: "))
            
            try:
                convert_to_dutch_date(loss_date)

            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user. '{loss_date}' Isn't the correct way to fill in the 'loss date'. Please enter the correct 'loss date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue

            input_date = convert_to_strptime(loss_date)

            if input_date > current_date():
                print('\n')
                rprint(F"[orange3]:scream: Hello user. The 'loss date' you just entered: '{loss_date}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct 'loss date' for product '{name}'.\
[/orange3]\n\n")
            
                continue
            break


        while True:
            loss_cause = (input(F"Step 6 = Enter one of the following 'causes of loss' options for product '{name}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive): ")).lower()
            
            loss_cause_list = ['broken', 'damaged', 'expired', 'missing', 'theft', 'other']

            if loss_cause in loss_cause_list:
                print('\n')
                rprint(F"[dark_sea_green4]Great!:thumbs_up: '{loss_cause.capitalize()}' is a correct 'cause of loss' option.[/dark_sea_green4]\n\n")

            else:
                print('\n')
                rprint(F"[orange3]:scream: Hello user. The 'cause of loss' you just entered: '{loss_cause}', isn't a correct 'cause of loss' option in the 'Losses' file. Please enter one of the following 'causes of loss' for product\
 '{name}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).[/orange3]\n\n")

                continue
            break


        print('\n')
        product_in_file_check('inventory.csv', name)
        
        while True:
            expiration_date = (input(F"Step 7 = Enter the 'expiration date' of product '{name}' as shown above in the 'product details' as follows: dd-mm-yyyy: "))
            
            try:
                expiration = convert_to_dutch_date(expiration_date)
                
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{expiration_date}' Isn't the correct way to fill in the 'expiration date'. Please enter the correct 'expiration date' for product '{name}' as follows: dd-mm-yyyy.[/orange3]\n\n")
            
                continue
            
            expiration_date_check = product_detail_check('inventory.csv', name, 'expiration_date')

            if expiration_date in expiration_date_check:
                print('\n')
                product_in_file_check('inventory.csv', name)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{name}' in the 'Inventory' file. You can see all the 'expiration dates' of\
 product '{name}' in the 'product details' shown above.[/dark_sea_green4]\n")
                
                if expiration == current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:astonished_face: Please note that the entered expiration date [bright_cyan]{expiration_date}[/bright_cyan] of the loss product with product ID [bright_cyan]{id}[/bright_cyan] and product name\
[bright_cyan]{name}[/bright_cyan] is today.:astonished_face:[/wheat1]")

                if expiration < current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:scream: Please note that the entered expiration date [bright_cyan]{expiration_date}[/bright_cyan] of the loss product with product ID [bright_cyan]{id}[/bright_cyan] and product name\
[bright_cyan]{name}[/bright_cyan] has expired.:scream:[/wheat1]")
                
            else:
                print('\n')
                product_in_file_check('inventory.csv', name)
                rprint(F"[orange3]:scream: Hello user! The entered expiration date: '{expiration_date}', doesn't match with one of the 'expiration dates' of product '{name}' in the 'Inventory' file. Please check the 'product details' above\
 for the correct 'expiration date'.[/orange3]\n\n")

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
                writer.writerows(rows)
                print('\n')
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The 'loss quantity' of product '{name}' has been 'updated', because the 'ID', the 'name', the 'loss amount', the 'loss date', the 'cause of loss' and the 'expiration date' are the same.\
 You can check the updated details below.[/dark_sea_green4]\n")
                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                print('\n')

            else:
                with open('losses.csv', 'a+', newline='') as losses_file:
                    writer = csv.DictWriter(losses_file, fieldnames= reader.fieldnames)
                    writer.writerow(product_details)
                    print('\n')
                    rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{name}' with product ID '{id}' and expiration date '{expiration_date}' has been added to the 'Losses' file. You can check the details below.[/dark_sea_green4]\n")
                    rprint(F"   [bright_cyan]{product_details}[/bright_cyan]")
                    print('\n')

        with open('inventory.csv', 'r+', newline='') as inventory_file:
            reader = csv.DictReader(inventory_file, fieldnames= ['id', 'name', 'purchase_quantity', 'purchase_amount', 'purchase_date', 'expiration_date'])
            rows = list(reader)
            
            for row in rows[1:]:
                
                if row['id'] == id and row['name'] == name and row['expiration_date'] == expiration_date:
                    row['purchase_quantity'] = int(row['purchase_quantity']) - int(loss_quantity)
                    
                    if row['purchase_quantity'] >0 and row['purchase_quantity'] < 3: # If the 'purchase quantity' of a product is 2 or less, it will trigger the print statement shown below.
                        rprint(F"[wheat1]STOCK UPDATE!!!:astonished_face: The product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date\
[bright_cyan]{row['expiration_date']}[/bright_cyan] needs to be reordered, because there are / is [bright_cyan]{row['purchase_quantity']}[/bright_cyan] left in stock.:astonished_face:[/wheat1]\n\n")

                    elif row['purchase_quantity'] <= 0: # If the 'purchase quantity' is less than zero / 0, it wil stay zero / 0 due to this code and the code below.
                            row['purchase_quantity'] = 0
                            rprint(F"[wheat1]STOCK UPDATE!!!:scream: Product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date [bright_cyan]{row['expiration_date']}[/bright_cyan]\
 needs to be reordered, because there is [bright_cyan]{row['purchase_quantity']}[/bright_cyan] / [bright_cyan]nothing[/bright_cyan] left in stock.:scream:[/wheat1]\n\n")

                    else:
                        rprint(F"[dark_sea_green4]STOCK UPDATE!!!:thumbs_up: Product [bright_cyan]{row['name']}[/bright_cyan] with product id [bright_cyan]{row['id']}[/bright_cyan] and expiration date\
[bright_cyan]{row['expiration_date']}[/bright_cyan] doesn't need to be reordered, because there are [bright_cyan]{(row['purchase_quantity'])}[/bright_cyan] left in stock.:grinning_face_with_big_eyes:[/dark_sea_green4]\n\n")


        with open('inventory.csv', 'r+', newline='') as inventory_file:
            writer = csv.DictWriter(inventory_file, fieldnames= reader.fieldnames)
            writer.writerows(rows)

    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – modify product details.

def modify_product_details():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'modify product details'[/bright_cyan] option.\n")

        print("- Follow the step(s) below to modify any detail of a product in a selected file. Have fun modifying!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'modify the product details in a selected file'")
            
        table.add_row("- Step 1 = Enter one of the following file names to modify a product detail: 'Inventory', 'Sales' or 'Losses' (not case sensitive).")
        table.add_row("- Step 2 = Enter the current 'ID' or 'name' of the product that you want to modify (the product name is not case sensitive)")
        table.add_row("- Step 3 = Enter the current product 'expiration date' as follows: dd-mm-yyyy.")
        table.add_row("- Step 4 = Enter the current product 'detail name' that you want to modify, for instance 'expiration date' etc. (not case sensitive and you don't have to put an underscore in the 'product detail name).")
        table.add_row("- Step 5 = Enter the 'modification' you would like to make for the product (not case sensitive).")
        table.add_row("- Step 6 = Confirm if you 'do' or 'don't' want to modify the product detail, by entering 'Y' for Yes or 'N' for No (not case sensitive).")
        table.add_row("- Done!")

        console.print(table)
        print('\n')


        while True:
            file_name = input("Step 1 = Enter one of the following file names to modify a product detail: 'Inventory', 'Sales' or 'Losses' (not case sensitive): ").lower()
            print('\n')

            if file_name == 'inventory':
                file_name = 'inventory.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
                
            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
                
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter one of the following file names: 'Inventory', 'Sales' or 'Losses' (not case sensitive).[/orange3]\n\n")
                
                continue
            break


        while True:
            search_type = input("Step 2 = Enter the current 'ID' or 'name' of the product that you want to modify (the product name is not case sensitive): ").lower()
            print('\n')

            if product_in_file_check(file_name, search_type) == True:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' of product '{search_type}' above.[/dark_sea_green4]\n")
            
            else:
                rprint(F"[orange3]:scream: Hello user! Product 'ID' / 'name' '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct current 'ID' or 'name' of the product (not case sensitive).\
[/orange3]\n\n")

                continue
            break


        print('\n')
        product_in_file_check(file_name, search_type)

        while True:
            expiration_date = input(F"Step 3 = Enter the current 'expiration date' of product '{search_type}' as shown above in the 'product details' as follows: dd-mm-yyyy: ")
            
            try:
                convert_to_dutch_date(expiration_date)
                
            except ValueError:
                print('\n')
                product_in_file_check(file_name, search_type)
                rprint(F"[orange3]:scream: Hello user! The entered current 'expiration date': '{expiration_date}', isn't the correct way to fill in the 'expiration date' for product '{search_type}' from the '{file_name.capitalize()[:-4]}'\
 file. Please enter the current 'expiration date' (as shown above) as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue

            expiration = convert_to_dutch_date(expiration_date)

            expiration_date_check = product_detail_check(file_name, search_type, 'expiration_date')

            if expiration_date in expiration_date_check:
                print('\n')
                product_in_file_check(file_name, search_type)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The entered current 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can\
 see all the 'expiration dates' of product '{search_type}' in the 'product details' above.[/dark_sea_green4]\n")
                
                if expiration == current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:astonished_face: Please note that the entered [bright_cyan]expiration date[/bright_cyan] of product [bright_cyan]{search_type}[/bright_cyan]: [bright_cyan]{expiration_date}[/bright_cyan], is today.\
:astonished_face:[/wheat1]\n")

                if expiration < current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:scream: Please note that the entered [bright_cyan]expiration date[/bright_cyan] of product [bright_cyan]{search_type}[/bright_cyan]: [bright_cyan]{expiration_date}[/bright_cyan], has expired.:scream:\
[/wheat1]\n")

            else:
                print('\n')
                product_in_file_check(file_name, search_type)
                rprint(F"[orange3]:scream: Hello user! The entered current 'expiration date': '{expiration_date}', doesn't match with one of the current 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}'\
 file. Please check the 'product details' above for the correct current 'expiration date'.[/orange3]\n\n")

                continue
            break


        print('\n')
        column_name_check(file_name)
        
        while True:
            column_name = (input(F"Step 4 = Enter the 'product detail name' of product '{search_type}' (as shown above) that you want to modify, for instance 'expiration date' etc. (not case sensitive and you don't have to put an\
 underscore in the 'product detail name'): ")).lower()
            print('\n')
            
            # Below are all the unique column names from the 3 CSV files. I've put these column names in a 'column_name' variable for 2 reasons:
            # 1 = The user doesn't have to type the underscore, 2 = So that I can use them in my 'column_name_check()' function where the underscore is needed.
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
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The entered product detail name '{column_name}' for product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see all the 'product detail names' from\
 the '{file_name.capitalize()[:-4]}' file above.[/dark_sea_green4]\n")

            else:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! The entered current 'product detail name': '{column_name}', doesn't match with one of the current 'product detail names' of product '{search_type}' in the '{file_name.capitalize()[:-4]}'\
 file. Please check the 'product detail names' above for the correct current 'product detail name'.[/orange3]\n\n")

                continue
            break


        print('\n')
        show_product_details(file_name, search_type, expiration_date)

        maximum_digits = '15'

        # Variables for the 'relevant date' in the relevant file for 'step 5' in the while loop below.
        relevant_date = ''

        if file_name == 'inventory.csv':
            relevant_date = 'purchase date'

        elif file_name == 'sales.csv':
            relevant_date = 'sales date'

        elif file_name == 'losses.csv':
            relevant_date = 'loss date'

        try:
            while True:
                product_detail = (input(F"Step 5 = Enter the 'modification' you would like to make for the '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file (not case sensitive). You can see all the current\
 'product details' of product '{search_type}' above: ")).lower()
                
                if column_name == "id" or column_name == 'purchase_quantity' or column_name == 'sold_quantity' or column_name == 'loss_quantity':
                    
                    try:
                        int(product_detail)

                    except ValueError:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! The 'modification' for product detail name '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file can only contain numbers. '{product_detail}'\
 doesn't only contain numbers. Please enter the correct modification for 'product detail name': '{column_name}'.[/orange3]\n\n")
                    
                        continue

                    if len(product_detail) > 15:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! The '{column_name}' can't contain more than '{maximum_digits}' digits. The entered '{column_name}': '{product_detail}', contains more than '{maximum_digits}' digits. Please\
 enter the modification for the '{column_name}' with a limit of '{maximum_digits}' digits.[/orange3]\n\n")
                        
                        continue

                elif column_name == 'purchase_amount' or column_name == 'sales_amount' or column_name == 'loss_amount':
                
                    try:
                        float(product_detail)

                    except ValueError:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! The entered modification: '{product_detail}', doesn't contain an 'amount' and / or a 'dot' to seperate the decimals. Please enter the correct modification for product detail\
 '{column_name}' of product '{search_type}' and use a dot in stead of a comma to seperate any decimals.[/orange3]\n\n")
                        
                        continue
                    
                    product_detail_amount = float(product_detail)
                    decimal_quantity = round(product_detail_amount, 2)
                    
                    if product_detail_amount != decimal_quantity:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! You can only add '2 decimals' after the dot. Please enter the '{column_name}' again and only add '2 decimals' when necessary.[/orange3]\n\n")

                        continue

                    elif len(product_detail) > 15:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! The '{column_name}' can't contain more than '{maximum_digits}' digits. The entered '{column_name}': '{product_detail}', contains more than '{maximum_digits}' digits. Please\
 enter the '{column_name}' with a limit of '{maximum_digits}' digits.[/orange3]\n\n")
                        
                        continue

                elif column_name == 'purchase_date' or column_name == 'sales_date' or column_name == 'loss_date' or column_name == 'expiration_date':
                    
                    try:
                        convert_to_dutch_date(product_detail)
                        
                    except ValueError:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! '{product_detail}' isn't the correct way to fill in the '{relevant_date}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter the\
 '{relevant_date}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                        
                        continue

                    avoid_future_date = convert_to_strptime(product_detail)

                    if column_name == 'purchase_date' and avoid_future_date > current_date() or column_name == 'sales_date' and avoid_future_date > current_date() or column_name == 'loss_date' and avoid_future_date > current_date():
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user! The date you just entered: '{product_detail}', is a date in the future. And we're not able to time travel... yet.:wink: Please enter the correct '{relevant_date}' of product\
 '{search_type}' as follows: dd-mm-yyyy.[/orange3]\n\n")
                        
                        continue

                elif column_name == 'loss_cause':

                    loss_cause_list = ['broken', 'damaged', 'expired', 'missing', 'theft', 'other']

                    if product_detail in loss_cause_list:
                        print('\n')
                        rprint(F"[dark_sea_green4]Great!:thumbs_up: '{product_detail.capitalize()}' is a correct 'cause of loss' option in the '{file_name.capitalize()[:-4]}' file.[/dark_sea_green4]\n")

                    else:
                        print('\n')
                        rprint(F"[orange3]:scream: Hello user. The 'cause of loss' you just entered: '{product_detail}', isn't a correct 'cause of loss' option in the '{file_name.capitalize()[:-4]}' file. Please enter one of the following\
 'causes of loss' options for product '{search_type}': 'broken', 'damaged', 'expired', 'missing', 'theft' or 'other' (not case sensitive).[/orange3]\n\n")

                        continue
                break
        
        except KeyboardInterrupt:
            rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
            sys.exit(0)


        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            for row in rows:
                
                if (row['name'] == search_type or row['id'] == search_type) and row['expiration_date'] == expiration_date:
                    print('\n')
                    rprint(F"[magenta]Product details of product '{search_type}' from the '{file_name.capitalize()[:-4]}' file that you want to modify:[/magenta]")
                    rprint(F"[bright_cyan]{row}[/bright_cyan]")
                    print('\n')
                    
                    try:
                        while True:
                            yes_or_no = input(F"Step 6 = Are you sure you want to modify the 'product detail': '{column_name}' of product: '{search_type}' from the current '{column_name}': '{row[column_name]}' (as shown above in the\
 'product details') to the modified '{column_name}': '{product_detail}'? Press 'Y' for Yes or 'N' for No (not case sensitive): ")
                            print('\n')
                            
                            if yes_or_no == 'Y' or yes_or_no == 'y':
                                row[column_name] = product_detail
                                rprint(F"[dark_sea_green4]Great![/dark_sea_green4]:thumbs_up: The product detail '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file has been modified to '{product_detail}'.\
 You can check the modification of product '{search_type}' below.\n")
                                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                                print('\n')
                                break
                                
                            elif yes_or_no == 'N' or yes_or_no == 'n':
                                rprint(F"[wheat1]:person_gesturing_NO: Okay. The product detail [dark_sea_green4]'{column_name}'[/dark_sea_green4] of product [dark_sea_green4]'{search_type}'[/dark_sea_green4] in the\
[dark_sea_green4]'{file_name.capitalize()[:-4]}'[/dark_sea_green4] file will not be modified from [dark_sea_green4]'{row[column_name]}'[/dark_sea_green4] to [dark_sea_green4]'{product_detail}'[/dark_sea_green4]. You can see the current\
[dark_sea_green4]'product details'[/dark_sea_green4] below.\n")
                                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                                print('\n')
                                break
                            
                            else:
                                rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' Isn't the correct input to modify the product detail '{column_name}' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please enter\
 'Y' for Yes or 'N' for No for the correct modification (not case sensitive).[/orange3]\n\n")
                                continue
                        break

                    except KeyboardInterrupt:
                        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
                        sys.exit(0)


        with open(file_name, 'r+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function – remove products.

def remove_products():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'remove product'[/bright_cyan] option.\n")
        
        print("- Follow the step(s) below to remove a product from a selected file. Have fun removing!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")
        
        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'remove products from a selected file'")

        table.add_row("- Step 1 = Enter one of the following file names in which you want to remove a product: 'Inventory', 'Sales' or 'Losses'.")
        table.add_row("- Step 2 = Enter the 'ID' or the 'name' of the product that you want to remove (not case sensitive).")
        table.add_row("- Step 3 = Enter the 'expiration date' of the product that you want to remove as follows: dd-mm-yyyy.")
        table.add_row("- Step 4 = Confirm if you 'do' or 'don't' want to remove the product from the selected file, by entering 'Y' for Yes or 'N' for No (not case sensitive).")
        table.add_row("- Done!")
        
        console.print(table)
        print('\n')


        while True:
            file_name = input("Step 1 = Enter one of the following file names in which you want to remove a product: 'Inventory', 'Sales' or 'Losses': ").lower()
            print('\n')

            if file_name == 'inventory':
                file_name = 'inventory.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
            
            elif file_name == 'sales':
                file_name = 'sales.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")
            
            elif file_name == 'losses':
                file_name = 'losses.csv'
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The '{file_name.capitalize()[:-4]}' file is found.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! There is no file named '{file_name}'. Please enter the correct file name (not case sensitive).[/orange3]\n\n")
                
                continue
            break


        while True:
            search_type = input("Step 2 = Enter the 'ID' or the 'name' of the product that you want to remove (not case sensitive): ").lower()
            print('\n')
            
            
            if product_in_file_check(file_name, search_type) == True:
                rprint(F"[dark_sea_green4]Great!:thumbs_up: Product '{search_type}' is found in the '{file_name.capitalize()[:-4]}' file. You can see the 'product details' above.[/dark_sea_green4]\n")
            
            else:
                rprint(F"[orange3]:scream: Hello user! Product '{search_type}' was not found in the '{file_name.capitalize()[:-4]}' file. Please enter the correct product 'ID' or 'name' (not case sensitive).[/orange3]\n\n")

                continue
            break


        print('\n')
        product_in_file_check(file_name, search_type)

        while True:
            expiration_date = input(F"Step 3 = Enter the 'expiration date' of product '{search_type}' (as shown above in the 'product details') that you want to remove as follows: dd-mm-yyyy: ")
            
            try:
                convert_to_dutch_date(expiration_date)
                
            except ValueError:
                print('\n')
                rprint(F"[orange3]:scream: Hello user! '{expiration_date}' isn't the correct way to fill in the 'expiration date' for product '{search_type}'. Please enter the expiration date as follows: dd-mm-yyyy.[/orange3]\n\n")
                
                continue


            expiration = convert_to_dutch_date(expiration_date)
            
            expiration_date_check = product_detail_check(file_name, search_type, 'expiration_date')
            
            if expiration_date in expiration_date_check:
                print('\n')
                product_in_file_check(file_name, search_type)
                rprint(F"[dark_sea_green4]Great!:thumbs_up: The entered 'expiration date': '{expiration_date}', matches one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. You can see all\
 the 'expiration dates' of product '{search_type}' in the 'product details' above.[/dark_sea_green4]\n")
                
                if expiration == current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:astonished_face: Please note that the entered [bright_cyan]expiration date[/bright_cyan] of product [bright_cyan]{search_type}[/bright_cyan]: [bright_cyan]{expiration_date}[/bright_cyan], is today.\
:astonished_face:[/wheat1]\n")

                elif expiration < current_date().strftime("%d-%m-%Y"):
                    rprint(F"[wheat1]:scream: Please note that the entered [bright_cyan]expiration date[/bright_cyan] of product [bright_cyan]{search_type}[/bright_cyan]: [bright_cyan]{expiration_date}[/bright_cyan], has expired.:scream:\
[/wheat1]\n")

            else:
                print('\n')
                product_in_file_check(file_name, search_type)
                rprint(F"[orange3]:scream: Hello user! The entered 'expiration date': '{expiration_date}', doesn't match with one of the 'expiration dates' of product '{search_type}' in the '{file_name.capitalize()[:-4]}' file. Please check\
 the 'product details' above for the correct 'expiration date'.[/orange3]\n\n")
                continue
            break


        with open(file_name, 'r', newline= '',) as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
            
            for row in rows:

                if (row['name'] == search_type or row['id'] == search_type) and row['expiration_date'] == expiration_date:
                    print('\n')
                    rprint(F"[magenta]Product details of product '{search_type}' that you want to remove from the '{file_name.capitalize()[:-4]}' file:[/magenta]")
                    rprint(F"[bright_cyan]{row}[/bright_cyan]")
                    print('\n')

                    try:
                        while True:
                            yes_or_no = input(F"Step 4 = Are you sure you want to remove product '{row['name']}' with product 'ID': '{row['id']}' as shown above in the 'product details' from the '{file_name.capitalize()[:-4]}' file? Press\
 'Y' for Yes or 'N' for No (not case sensitive): ")
                            print('\n')

                            if yes_or_no == 'Y' or yes_or_no == 'y':
                                rows.remove(row)
                                rprint(F"[dark_sea_green4]Great![/dark_sea_green4]:thumbs_up: Product '{row['name']}' with product 'ID': '{row['id']}' and 'expiration date': '{expiration_date}' has been removed from the\
 '{file_name.capitalize()[:-4]}' file.\n")
                                print('\n')
                                break
                            
                            elif yes_or_no == 'N' or yes_or_no == 'n':
                                rprint(F"[wheat1]:person_gesturing_NO: Okay. Product [dark_sea_green4]'{row['name']}'[/dark_sea_green4] with product [dark_sea_green4]'ID'[/dark_sea_green4]: [dark_sea_green4]'{row['id']}'[/dark_sea_green4]\
 has not been removed from the [dark_sea_green4]'{file_name.capitalize()[:-4]}'[/dark_sea_green4] file. You can see the [dark_sea_green4]'product details'[/dark_sea_green4] of product [dark_sea_green4]'{search_type}'[/dark_sea_green4]\
 below.[/wheat1]\n")
                                rprint(F"   [bright_cyan]{row}[/bright_cyan]")
                                print('\n')
                                break

                            else:
                                rprint(F"[orange3]:scream: Hello user! '{yes_or_no}' Isn't the correct input to remove product '{search_type}' from the '{file_name.capitalize()[:-4]}' file. Please enter 'Y' for Yes if you 'do' or 'N' for No\
 if you 'don't' want to remove product '{search_type}' from the '{file_name.capitalize()[:-4]}' file (not case sensitive).[/orange3]\n\n")

                                continue
                        break

                    except KeyboardInterrupt:
                        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
                        sys.exit(0)


        with open(file_name, 'w', newline= '') as file:
            writer = csv.DictWriter(file, fieldnames= reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# Help functions – calculate costs.

def calculate_costs(from_date: datetime, until_date: datetime):
    '''
    Returns the 'costs' of a product rounded to 2 decimals within a certain period.
    '''

    with open('inventory.csv', 'r') as inventory_file:
        reader = csv.DictReader(inventory_file)

        total_costs = 0

        for row in reader:
        
            purchase_date = convert_to_strptime(row['purchase_date'])
            
            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)
            
            if input_from_date <= purchase_date and input_until_date >= purchase_date:
                costs = float(row['purchase_quantity']) * float(row['purchase_amount'])
            
                total_costs += costs
        
        return round(total_costs, 2)


# Help function – calculate losses.

def calculate_losses(from_date: datetime, until_date: datetime):
    '''
    Returns the 'losses' of a product rounded to 2 decimals within a certain period.
    '''

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


# Help function – calculate revenue.

def calculate_revenue(from_date: datetime, until_date: datetime):
    '''
    Returns the 'revenue' of a product rounded to 2 decimals within a certain period.
    '''

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


# Help function – calculate profit.

def calculate_profit(from_date: datetime, until_date: datetime):
    '''
    Returns the 'profit' of a product rounded to 2 decimals within a certain period.
    '''

    with open('sales.csv', 'r') as sales_file:
        reader = csv.DictReader(sales_file)

        for row in reader:
    
            product_sales_date = convert_to_strptime(row['sales_date'])

            input_from_date = convert_to_strptime(from_date)
            input_until_date = convert_to_strptime(until_date)

            if input_from_date <= product_sales_date and input_until_date >= product_sales_date:
                profit = float(calculate_revenue(from_date, until_date)) - float(calculate_costs(from_date, until_date)) - float(calculate_losses(from_date, until_date))

    return round(profit, 2)


# User function – calculations.

def calculations():

    try:
        rprint("- Hello user, and welcome to the [bright_cyan]'calculations'[/bright_cyan] option.\n")

        rprint("- Follow the [grey78]step(s)[/grey78] below to select which calculation you would like to make: 'costs', 'losses', 'revenue' or 'profit'. Have fun calculating!\n")
        
        rprint("-[magenta] Note! Press [bright_cyan]'Ctrl' + 'C'[/bright_cyan] on your keyboard if you want to [bright_cyan]stop[/bright_cyan] with filling in this step / these steps.[/magenta]\n")

        console = Console()

        table = Table(show_header = True, header_style = 'dark_sea_green4')

        table.add_column("Steps to: 'calculate the costs, losses, revenue or profit'")

        table.add_row("- Step 1 = Enter one of the following calculations you would like to make: 'costs', 'losses', 'revenue' or 'profit' (not case sensitive).")
        table.add_row("- Step 2 = Enter the 'from' date as follows: dd-mm-yyyy.")
        table.add_row("- Step 3 = Enter the 'until' date as follows dd-mm-yyyy.")
        table.add_row("- Done!")
        
        console.print(table)
        print('\n')


        while True:
            calculation_type = input("Step 1 = Enter one of the following calculations you would like to make: 'costs', 'losses', 'revenue' or 'profit' (not case sensitive): ").lower()
            print('\n')

            if calculation_type == 'costs' or calculation_type == 'losses' or calculation_type == 'revenue' or calculation_type == 'profit':
                rprint(F"[dark_sea_green4]Great!:thumbs_up: It is noted that you want to calculate the '{calculation_type}'.[/dark_sea_green4]\n")

            else:
                rprint(F"[orange3]:scream: Hello user! '{calculation_type}' Isn't the correct input for selecting a calculation. Please enter one of the following calculations: 'costs', 'losses', 'revenue' or 'profit'\
 (not case sensitive).[/orange3]\n\n")
                
                continue
            break


        while True:
            from_date = input("Step 2 = Enter the 'from' date as follows: dd-mm-yyyy: ")
            print('\n')

            try:
                convert_to_dutch_date(from_date)
                
            except ValueError:
                rprint(F"[orange3]:scream: Hello user! '{from_date}' Isn't the correct way to fill in the 'from' date. Please enter the correct 'from' date as follows: dd-mm-yyyy.[/orange3]\n\n")

                continue
            break


        while True:
            until_date = input("Step 3 = Enter the 'until' date as follows dd-mm-yyyy: ")
            print('\n')

            try:
                convert_to_dutch_date(until_date)
                
            except ValueError:
                rprint(F"[orange3]:scream: Hello user! '{until_date}' Isn't the correct way to fill in the 'until' date. Please enter the correct 'until' date as follows: dd-mm-yyyy.[/orange3]\n\n")

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

        return rprint(F"[dark_sea_green4]Great![/dark_sea_green4]:thumbs_up: The '{calculation_type}' from the period '{from_date}' until '{until_date}' = '€ {calculation}'.\n\n")
    
    except KeyboardInterrupt:
        rprint("\n\n[wheat1]Okay. It's noted that you want to [dark_sea_green4]stop[/dark_sea_green4] with filling in this step / these steps. See you next time!:person_raising_hand:[/wheat1]\n\n")
        sys.exit(0)


# User function - display file options.

def display_file_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'file options'[/bright_cyan] menu.\n")
    
    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the files!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'dark_sea_green4')

    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'file options'[/bright_cyan] below to get started!")
    
    table.add_row('1', "Export a file to Excel")
    table.add_row('2', "Exit this menu")

    
    while True:

        console.print(table)
        print('\n')

        daily_expiration_check()
        print('\n')

        option = input("Enter 1 of the 4 options: ")
        print('\n')

        if option == '1':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            export_file_to_excel()

        elif option == '2':
            rprint("[wheat1]Okay. You have selected the [dark_sea_green4]exit[/dark_sea_green4] option. See you next time!:person_raising_hand:[/wheat1]\n\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 4.[/orange3]\n")
            
            continue
        break


# User function - display date options.

def display_date_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'date options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the dates!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'dark_sea_green4')

    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'date options'[/bright_cyan] below to get started!")
    
    table.add_row('1', "Update the system date")
    table.add_row('2', "Change the system date by days or weeks in the past or future")
    table.add_row('3', "Select a specific system date")
    table.add_row('4', "Special occasion countdown / date")
    table.add_row('5', "Exit this menu")


    while True:
        
        console.print(table)
        print('\n')

        daily_expiration_check()
        print('\n')

        option = input("Enter 1 of the 5 options: ")
        print('\n')

        if option == '1':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            update_system_date()

        elif option == '2':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            change_system_date()

        elif option == '3':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            select_specific_date()
            
        elif option == '4':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            special_occasion_date()

        elif option == '5':
            rprint("[wheat1]Okay. You have selected the [dark_sea_green4]exit[/dark_sea_green4] option. See you next time!:person_raising_hand:[/wheat1]\n\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 5.[/orange3]\n")

            continue
        break


# User function - display product options.

def display_product_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'product options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the products!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'dark_sea_green4')
    
    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'product options'[/bright_cyan] below to get started!")

    table.add_row('1', "Avoid expired products")
    table.add_row('2', "View all products")
    table.add_row('3', "View products based on a specific date (purchase date, sold date, loss date or expiration date)")
    table.add_row('4', "Find products")
    table.add_row('5', "Add inventory products")
    table.add_row('6', "Add sold products")
    table.add_row('7', "Add loss products")
    table.add_row('8', "Modify product details")
    table.add_row('9', "Remove product")
    table.add_row('10', "Exit this menu")


    while True:
        
        console.print(table)
        print('\n')

        daily_expiration_check()
        print('\n')

        option = input("Enter 1 of the 10 options: ")
        print('\n')

        if option == '1':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            avoid_expired_products()
            break
        
        if option == '2':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            view_all_products()

        elif option == '3':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            view_product_dates()

        elif option == '4':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            find_products()
        
        elif option == '5':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            add_inventory_products()
        
        elif option == '6':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            add_sold_products()
        
        elif option == '7':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            add_loss_products()
        
        elif option == '8':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            modify_product_details()
        
        elif option == '9':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            remove_products()
        
        elif option == '10':
            rprint("[wheat1]Okay. You have selected the [dark_sea_green4]exit[/dark_sea_green4] option. See you next time!:person_raising_hand:[/wheat1]\n\n")
            break

        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 10.[/orange3]\n")

            continue
        break


# User function - display calculation options.

def display_calculation_options():

    rprint("- Hello user, and welcome to the [bright_cyan]'calculation options'[/bright_cyan] menu.\n")

    print("- After you have entered a valid option from below, you will be directed to the selected option. Have fun with the calculations!\n")

    console = Console()

    table = Table(show_header = True, header_style = 'dark_sea_green4')
    
    table.add_column("#")
    table.add_column("Select one of the [bright_cyan]'calculation options'[/bright_cyan] below to get started!")
    
    table.add_row('1', "Calculate the 'costs', 'losses', 'revenue' or 'profit'.")
    table.add_row('2', "Exit this menu")


    while True:
        console.print(table)
        print('\n')

        daily_expiration_check()
        print('\n')

        option = input("Enter 1 of the 2 options: ")
        print('\n')

        if option == '1':
            rprint("[dark_sea_green4]Great!:thumbs_up: You will now be directed to the selected option.[/dark_sea_green4]\n")
            print('\n')
            calculations()
            break

        elif option == '2':
            rprint("[wheat1]Okay. You have selected the [dark_sea_green4]exit[/dark_sea_green4] option. See you next time!:person_raising_hand:[/wheat1]\n\n")
            break
        
        else:
            rprint("[orange3]:scream: Hello user! You have entered an invalid option. Please enter a valid option from 1 to 2.[/orange3]\n")


if __name__ == "__main__":

    print('\n')
    
    # All user functions.

    # File function(s).
    print(export_file_to_excel())
    print('\n')


    # Date functions.
    print(update_system_date())
    print('\n')

    print(change_system_date())
    print('\n')

    print(select_specific_date())
    print('\n')

    print(special_occasion_date())
    print('\n')


    # Product functions.
    print(avoid_expired_products())
    print('\n')

    print(view_all_products())
    print('\n')

    print(view_product_dates())
    print('\n')

    print(find_products())
    print('\n')

    print(add_inventory_products())
    print('\n')

    print(add_sold_products())
    print('\n')

    print(add_loss_products())
    print('\n')

    print(modify_product_details())
    print('\n')

    print(remove_products())
    print('\n')

    
    # Calculation functions.
    print(calculations())
    print('\n')


    # Display / menu functions.
    print(display_file_options())
    print('\n')

    print(display_date_options())
    print('\n')

    print(display_product_options())
    print('\n')

    print(display_calculation_options())
    print('\n')