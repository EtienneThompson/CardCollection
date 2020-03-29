import os
import sys
import argparse

'''
Things to change:

- Add option to read collection values from file and write those to the file.
- If card's quantity is greater than 4, write to separate file, and then ask
    the user if the quantities are correct. If they are, write that file to
    the main file.
'''

parser = argparse.ArgumentParser()
parser.add_argument("--card", type=str, required=True)
parser.add_argument("--quantity", type=int, required=True)
args = parser.parse_args()

coll_file = os.path.join(os.getcwd(), "collection.txt")
collection = dict()

with open(coll_file, "r") as file:
    lines = coll_file.readlines()

for line in lines:
    line = line.split(",")
    collection.setdefault(line[0], 0)
    collection[line[0]] += int(line[1])
collection[args.card] += args.quantity

with open(coll_file, "a") as file:
    for card, quantity in collection.items():
        coll_file.write(card + "," + quantity)
