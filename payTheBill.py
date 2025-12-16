import json
from loadData import loadData, FILE_PATH

def paythebill():
    username = input("Enter username: ")
    password = input("Enter password: ")
    card_num = input("Enter card number: ")
    try:
        pay_amount = int(input("Enter amount to pay: "))
    except ValueError:
        print("Invalid amount!")
        return

    data = loadData()
    for card in data:
        if card["username"] == username and card["password"] == password and card["ccnum"] == card_num:
            if pay_amount > card["outstanding"]:
                print("Payable amount cannot exceed outstanding!")
            else:
                card["outstanding"] -= pay_amount
                card["limit"] += pay_amount
                print(f"Transaction success! Available limit: {card['limit']}, Outstanding: {card['outstanding']}")
                with open(FILE_PATH, "w") as f:
                    json.dump(data, f, indent=4)
            return

    print("Invalid username, password, or card number.")
