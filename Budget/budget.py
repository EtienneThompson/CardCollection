import os
import argparse
import datetime

def read_budget():
    '''Read the file and return the last thing written.'''
    with open("budget.txt", 'r') as file:
        contents = file.readlines()
    return float(contents[-1].split()[-1])

def read_allotment():
    '''Reads the specified allotment at the top of budget.txt.'''
    with open("budget.txt", 'r') as file:
        contents = file.readlines()
    return float(contents[0].split()[-1])

def write_budget(new_amount):
    '''Write the given amount to the file.

    Arguments:
        new_amount (float):
            The updated budget to be written to the file.
    '''
    with open("budget.txt", 'a') as file:
        file.write(f"{datetime.datetime.now().date()}: {new_amount}\n")

def update_allotment(new_amount):
    '''Update the Weekly Allotment amount in budget.txt with the new_amount.

    Arguments:
        new_amount:
            The amount to update the Weekly Allotment to become.
    '''
    with open("budget.txt", 'r') as file:
        contents = file.readlines()
    contents[0] = f"{contents[0].split(':')[0]}: {new_amount}\n"
    with open("budget.txt", 'w') as file:
        for line in contents:
            file.write(line)

def main():
    # Get the current budget.
    budget = read_budget()

    # Setup the different command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--spend",
        type=float,
        help="Spend an amount from the current budget.")
    parser.add_argument(
        "-a",
        "--add",
        type=float,
        help="Add an amount to the current budget.")
    parser.add_argument(
        "-w",
        "--weekly",
        action="store_true",
        help="Add the weekly allotment.")
    parser.add_argument(
        "-u",
        "--update",
        type=float,
        help="Update the weekly allotment to the provided value.")
    args = parser.parse_args()

    # Perform functions based on provided arguments.
    if args.add:
        budget += args.add
        write_budget(budget)
    if args.spend:
        budget -= args.spend
        write_budget(budget)
    if args.weekly:
        allotment = read_allotment()
        budget += allotment
        write_budget(budget)
    if args.update:
        update_allotment(args.update)

    # Print the budget after performing functions.
    print(
        f"Current budget: {budget}"
        f"{'0' if len(str(budget)) - str(budget).index('.') <= 2 else ''}")

if __name__ == "__main__":
    main()