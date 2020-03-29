import os

collection = dict()

coll_file = os.path.join(os.getcwd(), "collection.txt")
with open(coll_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        data = line.split(",")
        collection.setdefault(data[0], dict())
        collection[data[0]]["Quantity"] = int(data[1])
