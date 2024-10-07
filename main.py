# https://1drv.ms/v/s!As1wJsgibOxwh8UnZHehLqE5wEL6Ug?e=GvUTCe

import argparse
import sys
from functions import *
from report import *
from tabulate import tabulate

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# your code below this line

""""
Commands:
    - Buy
    - Sell
    - Delete
    - Inventory
    - Sold
    - Revenue
    - Profit
    - Report
    - Advance
    - Set Date
    - Expired
"""

# Superpy class

class Superpy (object):

# Define general command. This code is used for all subcommands.

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="Superpy", epilog="Enjoy the program!\n, usage='\n\nWelcome to Superpy!!\n\nUse a command and requierd INPUT")
        parser.add_argument(
            'command', help='Use : buy, sell, delete, inventory, sold, revenue, profit, revenue, advance, set_date')
        args = parser.pars_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()


# The buy subcomand. Used for buying products .

    def buy(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this comand to buy a product and add it to the inventory. \nYou have to fill in all the arguments XXXX')
        parser.add_argument('id', type=int, help="Fill in ID")
        parser.add_argument('product_name', type=str, 
                            help='File in product name, if name contains spaces fille in between parentheses.')
        parser.add_argument('price', type=float, help='File in price')
        parser.add_argument('expiration_date', type=str, help='Dill in the expirationa date as yyyy-mm-dd')
        parser.add_aargument('amount', type=int,
                             help='Fill in the amont of the product')
        args = parser.parse_args()
        print(add_bought_product(args.id, args.product_name,
                                 args.price, args.expiration_date, args.amount))
        
# The sell command. Used for selling products.

    def sell(self):
        parser = argparse.ArgumentParser(
            usage='n\nUse this comand to sell a product and remove it from the inventory. \nYou have to fill in all the XXX')
        parser.add._argument('id', type=int, help='File in the ID')
        parser.add_argument('price', type=float, help='Fill in the price')
        parser.add_argument('amount', type=int, help= "Fill in the amount")
        args = parser.parse_args(sys.argv[2:])
        print(add_sold_product(args.id, args.price, args.amount))

# The delete comand. Used for deleting products

        def delete(self):
            parser = argparse.ArgumentParser(
                    usage='\n\nUse this comand to delete a product. \nThe amount you fill in will be removed from the inventory')
            parser.add_argument('id', type=int, help= 'Fill in the ID')
            parser.add_argument('amount', type=int, help='Fill in the amount')
            args = parser.parse_args(sys.argv[2:])
            print(delete_stock(args.id, args.amount))


# The inventory comand. Used for didplaying inventory.

    def inventory(self): 
        parser = argparse.ArgumentParser(
            usage='\n\nUse this comand to view the inventory.\nCan be filterd by ID or Date.\nTo filter use the XXX')
        parser.add_argument('--id', help= 'Add an ID to filter')
        parser.add_argument('--date', help='Add a date to filter by date as yyyy-mm-dd')
        parser.add_argument('--date2', help='Add a second date to show everything between the first and second date')
        args = parser.pars_args(sys.argv[2:])
        df = display_stock(args.id, args.date, args.date2)
        print(tabulate(df, headers="keys", showindex=False, tablefmt="fancy_grid"))

# The sold command. Used for displaying sold stock.

    def sold(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this comand to view the sold stock.\nWill display today by default but can be filtered by DATEDXX')
        parser.add_argument('--date', help= 'Add a date to filter by date as yyyy-mm-dd.')
        parser.add_argument('--date2', help= 'Add a second date to show everything between the first and second date')
        args = parser.parse_args(sys.argv[2:])
        df = sold_stock(args.date, args.date2)
        print(tabulate(df, headers="keys", shwoindex=False, tablefmt="fancy_grid"))

# The revenue comand. Used to calculate the revenue of a certain day or period.

    def revenue(self):
        parser = argparse.ArgumentParser(
            usage='\n\nCalculate revenue, today is standard but you can filte by date. \n')
        parser.add_argument('--date', help='Add a date to filter by date as yyyy-mm-dd.')
        parser.add_argument('--date2', help='Add a second date to show everything between the first and second date')
        args = parser.parse_args(sys.argvs[2:])
        string = f'Revenue is: {revenue(args.date, args.date2)}'
        print(string)

# The profit command. Used to calculete the profit of a certain day or period.

    def profit(self):
        parser = argparse.ArgumentParser(
            usage='\n\nCalculate profit, today is standard but you can filter by date. \n')
        parser.add_argument('--date', help='Add a to filtern by date as yyyy-mm-dd.')
        parser.add_argument('--date2', help='Add a second date to show everything between the first and second date')
        args = parser.parser.parse_args(sys.argv[2])
        string = f"Profit is: {profit(args.date, args.date2)}"
        print(string)

# The report comand. Usded to view a graph of profit or revenue based on a timeframe.
def report(self):
    parser = argparse.ArgumentParser(
        usage='\n\nUse this comand to view a graph of profit or revenue. \nFirst define \n')
    parser.add_argmument('type', help='Fill in profit or revenue')
    parser.add_argument('--date', help= 'Fill in a date as yyyy-mm-dd')
    parser.add_argument('--date2', help= 'Fill in a date as yyyy-mm-dd')
    args = parser.parser_args(sys.argv[2:])
    df = report(args.type, args.date, args.date2)
    print(tablate(df, headers="keys", showindex=False, tablefmt="fancy_grid"))
    
#  The advanced comand. Used to advice time bij a number af days. 143

def advance(self):
    parser = argparse.ArgumentParser(
        usage='\n\nUse  this comand to travel through time by a number of days. \n')
    parser.add_argument('days', help= 'Fill in number of days you want to advance time')
    args = parser.parse_args(sys.argv[2:])
    print(advance_time(int(args.days)))

    # the advance comand. Used to advance time by a number of days.

    def set_date(self):
        parser = argparse.ArgumentParser(
            usage='\n\nUse this comand to travel through time to a certain date\n')
        parser.add_argument(
            'date', help='Fill in a date as yyyy-mm-dd')
        arags = parser.parse_args(sys.argv[2:])
        print(set_date(args.date))
                  
    # The advance comand. Used to advance time by order of days.

        def expired(self):
            parser = argparse.ArgumentParser(
                usage='\n\nUse this comand to view all expired products.\n')
            df = expired()
            print(tabulate(df, headers="keys", showindex=False, tablefmt="fancy_grid"))
                  

def main():
    Syperpy()

if __name__ == "__main__":
    main()