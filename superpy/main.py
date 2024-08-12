# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# Imports

from argparse import *
from functions import *

print('\n')

parser = ArgumentParser(description = "Hello user, and welcome to SuperPy: your supermarket inventory management system. Have fun managing!")

subparsers = parser.add_subparsers(dest= "command")

# File options menu.
file_option = subparsers.add_parser('files', help= "- Use this option to 'create' or 'clear' a file, or to 'export' a file to Excel. The 'file options menu' will show you which options you can choose from. When you've selected an option, a\
 step by step explination will guide you through the selected 'file' option.\n")

# Date options menu.
date_option = subparsers.add_parser('dates', help= "- Use this option to 'update' or 'change' the system date. Or to 'select a specific system date'. Or to 'create a special occasion date'. The 'date options menu' will show you which\
 options you can choose from. When you've selected an option, a step by step explination will guide you through the selected 'date' option.\n")

# Product options menu.
product_option = subparsers.add_parser('products', help= "- Use this option to 'view', 'find', 'add', 'modify' and 'remove' products from a selected file. With this option you can also 'avoid expired products' to help make our world a\
better and durable place!. The 'product options menu' will show you which options you can choose from. When you've chosen an option, a step by step explination will guide you through the selected 'product' option.\n") 

calculate_option = subparsers.add_parser('calculations', help= "- Use this option to calculate the 'costs', 'losses', 'revenue' or 'profit'. The 'calculate options menu' will show you which options you can choose from. When you've selected\
an option, a step by step explination will guide you through the selected 'calculate' option.\n")


# Parse arguments
args = parser.parse_args()

if args.command == "files":
    display_file_options()
    
if args.command == "dates":
    display_date_options()
    
if args.command == "products":
    display_product_options()
    
if args.command == "calculations":
    display_calculation_options()
