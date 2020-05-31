import os
from TCGPlayerApi import tcgplayerapi


api = tcgplayerapi.TCGPlayerAPI()
collection = dict()

coll_file = os.path.join(os.getcwd(), "collection.csv")
with open(coll_file, "r") as file:
    lines = file.readlines()

total_price = 0
for line in lines[2:]:
    data = line.split(",")
    # Set the key to a combination of card name and card set so cards with the
    # same name but different sets don't overlap.
    key = f"{data[0]}_{data[1]}"
    collection.setdefault(key, dict())
    collection[key]["card_name"] = data[0]
    collection[key]["set"] = data[1]
    collection[key]["quantity"] = int(data[2])
    collection[key]["indiv_price"] = float(data[3])
    collection[key]["total_price"] = float(data[4])

    # Fetch the updated price.
    updated_price = api.get_price(data[0], data[1])

    if updated_price[0] != -1:
        updated_price = round(float(updated_price[0][1:]), 2)
        quantity_price = updated_price * collection[key]["quantity"]
        collection[key]["indiv_price"] = updated_price
        collection[key]["total_price"] = quantity_price
        total_price += quantity_price
    else:
        # Use the previous values.
        quantity_price = float(data[4])
        total_price += quantity_price

    print(
        f"{data[0]} - {data[1]} - Quantity: {int(data[2])} - Total Price: "
        f"${quantity_price}")

total_price = round(total_price, 2)
print(f"Total Price: ${total_price}")

with open(coll_file, "w") as file:
    file.write(str(lines[0]))
    file.write(f"Total Price: ${total_price}\n")
    for key in collection.keys():
        entry = ""
        for data in collection[key].keys():
            entry += f"{collection[key][data]},"
        file.write(entry.strip(",") + "\n")

api.close()
