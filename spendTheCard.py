import json
from loadData import loadData, FILE_PATH

def spendtheCard():
    username = input("Enter username: ")
    password = input("Enter password: ")
    card_num = input("Enter card number: ")
    try:
        spend_amount = int(input("Enter amount to spend: "))
    except ValueError:
        print("Invalid amount!")
        return

    data = loadData()
    for card in data:
        if card["username"] == username and card["password"] == password and card["ccnum"] == card_num:
            if spend_amount > card["limit"]:
                print("Cannot process: insufficient limit.")
            else:
                card["limit"] -= spend_amount
                card["outstanding"] += spend_amount
                print(f"Transaction successful! Available limit: {card['limit']}, Outstanding: {card['outstanding']}")
                with open(FILE_PATH, "w") as f:
                    json.dump(data, f, indent=4)
            return

    print("Invalid username, password, or card number.")
