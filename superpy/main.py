# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# Imports

from argparse import *
from functions import *

print('\n')

# De argpars roep je als volgt op in je terminal: py .\main.py

parser = ArgumentParser(description = "Hello user, and welcome to SuperPy: your supermarket inventory management system. Have fun managing!")

subparsers = parser.add_subparsers(dest= "command")

# File options menu.
file_option = subparsers.add_parser("file", help= "- Use this option to 'create' or 'clear' a file, or to 'export' a file to Excel. The 'file options menu' will show you which options you can choose. When you've chosen an option, a step by\
 step explination will guide you through the chosen file option.\n")  # Met de 'add_parser' code geef je met een 'argument' aan wat de 'command' code moet zijn (+ de helptekst). En in dit geval is de command code 'file'.

# Date options menu.
date_option = subparsers.add_parser("date", help= "- Use this option to 'update' or 'change' the system date. Or to go to a specific date. Or to create a special occasion date. The 'date options menu' will show you which options you can choose.\
 When you've chosen an option, a step by step explination will guide you through the chosen date option.\n")

# Product options menu.
product_option = subparsers.add_parser("product", help= "- Use this option to 'view', 'find', 'add', 'modify' and 'remove' products. With this option you can also 'avoid expired products' and calculate the 'costs', 'losses', 'revenue' or\
 'profit'. The 'product options menu' will show you which options you can choose. When you've chosen an option, a step by step explination will guide you through the chosen product option.\n") 

calculate_option = subparsers.add_parser('calculate', help= "- Use this option to calculate the 'costs', 'losses', 'revenue' or 'profit' in a selected file. The 'calculate options menu' will show you which options you can select. When\
 you've selected an option, a step by step explination will guide you through the selected calculate option.\n")

# Parse arguments
args = parser.parse_args()          # De '.parse_args' code bevat alle argumenten die ik in de hierboven vermelde subparser argumenten heb geplaatst. En in dit geval zijn het de argumenten: 

if args.command == "file".lower():  # Met de 'args.command' code geef je aan wat de 'command' code moet zijn die ik hierboven bij de 'subparsers = parser.add_subparsers(dest= "command")' heb gedefinieerd. En in dit geval is het 'file'.
    display_file_options()

if args.command == "date":
    display_date_options()

if args.command == "product":       # Met deze code geef je aan wat de 'command' code moet zijn die ik hierboven bij en de 'subparsers = parser.add_subparsers(dest= "command")' heb gedefinieerd. En in dit geval is het 'file'.
    display_product_options()

if args.command == "calculate":
    display_calculation_options()
    
    
# LET OP!!! Omdat ik alleen maar met 'input statements' heb gewerkt in mijn 'functions.py' bestand, heb ik in geen één van mijn 'gebruikers functies' argumenten gebruikt. Daarom hoef ik in mijn 'main.py' bestand ook geen '.add_argument'
# code te gebruiken voor 'postional arguments' of 'optional arguments'. Een voorbeeld van wanneer je de argparse code 'wel' met argumenten / arguments kunt gebruiken heb ik op blz. 23 van mijn Word doc. Superpy Eindopdracht staan.

# 'Positional arguments' (= zonder 2 min / -- tekens, zie blz. 23 van mijn Word doc. Superpy Eindopdracht):
# LET OP!!! Wanneer je dus functies hebt die 'wel' 1 of meer argumenten hebben én je gebruikt 'positional arguments', dan vraag je dit op onderstaande manier op in je terminal:
# NAAM COMMAND NAAM_1E_ARGUMENT NAAM_2E_ARGUMENT.

# 'Optional argument'  (= met 2 min tekens / -- ):
# LET OP!!! Wanneer je dus functies hebt die 'wel' 1 of meer argumenten hebben én je gebruikt 'optional arguments', dan vraag je dit op onderstaande manier op in je terminal:
# NAAM COMMAND --NAAM_1E_ARGUMENT --NAAM_2E_ARGUMENT.