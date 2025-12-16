from addCard import addCard
from showCards import showCards
from spendTheCard import spendtheCard
from payTheBill import paythebill

def main():
    while True:
        print("\n1: Add credit card")
        print("2: Show credit cards")
        print("3: Spend")
        print("4: Pay bill")
        print("5: Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            addCard()
        elif choice == 2:
            showCards()
        elif choice == 3:
            spendtheCard()
        elif choice == 4:
            paythebill()
        elif choice == 5:
            print("exit")
            break
        else:
            print("Invalid choice.")

main()
