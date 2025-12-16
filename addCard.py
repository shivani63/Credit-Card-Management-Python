import json
from loadData import loadData, FILE_PATH

def addCard():
    username = input("Enter username: ")
    password = input("Enter password: ")
    ccnum = input("Enter credit card number: ")
    try:
        limit = int(input("Enter credit card limit: "))
    except ValueError:
        print("Invalid limit!")
        return

    data = loadData()  

    new_card = {
        "username": username,
        "password": password,
        "ccnum": ccnum,
        "limit": limit,
        "outstanding": 0
    }
    data.append(new_card)  

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("Credit card added successfully!")
