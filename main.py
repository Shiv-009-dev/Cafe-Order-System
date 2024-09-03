Menu = {
    "Cheese Burger": 80,
    "Cheese Sandwich": 100,
    "French Fries": 90,
    "Hot Dog": 100,
    "Fruit Salad": 50,
    "Cocktails": 150,
    "Milk Shake": 120,
    "Iced Tea": 60,
    "Orange Juice": 40,
    "Lemon Tea": 50,
    "Coffee": 10,
}

print("Welcome to the Cafe!\n")
print("*MENU*")
for item, price in Menu.items():
    print(f"{item}: Rs. {price}")

order_total = 0
while True:
    item = input("\nEnter the name of the item you want to order: ").strip()
    if item in Menu:
        order_total += Menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Ordered item '{item}' is NOT available!")

    more_items = input("Do you want to add another item? (YES/NO): ").strip().upper()
    if more_items != "YES":
        break

print(f"\nThe total amount you have to pay is Rs. {order_total}")
