"""
A simple menu calculator program that allows users to order items from a predefined menu.

The program displays a menu of items with corresponding numbers and prices. Users can input the numbers associated with the items they want to order.
The program calculates the total bill based on the user's selections and displays the ordered items with their prices and a final total bill.

Menu:
1. Chicken Strips - £3.50
2. Fries - £2.50
3. Chicken Burger - £4.00
4. Chicken Wrap - £3.50
5. Large Drink - £1.75
6. Medium Drink - £1.50
7. Milk Shake - £2.25
8. Salad - £3.75
9. Small Drink - £1.25

The program continuously takes orders until the user indicates they're finished by typing 'no' or 'n' or just 'enter'.
"""

menu = {
    '1': {'item': 'Chicken Strips', 'price': 3.50}, 
    '2': {'item': 'Fries', 'price': 2.50}, 
    '3': {'item': 'Chicken Burger', 'price': 4.00}, 
    '4': {'item': 'Chicken Wrap', 'price': 3.50}, 
    '5': {'item': 'Large Drink', 'price': 1.75}, 
    '6': {'item': 'Medium Drink', 'price': 1.50}, 
    '7': {'item': 'Milk Shake', 'price': 2.25}, 
    '8': {'item': 'Salad', 'price': 3.75}, 
    '9': {'item': 'Small Drink', 'price': 1.25}, 
}

print("Menu".center(20, '='))
for k, v in menu.items():
    print(f"{k}. {v['item'].ljust(20, '.')}£{v['price']:.2f}")

total = 0
order_num = 0
while True:
    user_choice = input("\nOrder: ")

    for key in user_choice:
        if key in menu:
            order_num += 1
            total += menu[key]['price']
            print(f"Order {order_num}: {menu[key]['item'].ljust(20, '.')}£{menu[key]['price']:.2f}")
    extra = input("\nWould you like anything else? ")
    if extra in ["no", "n", ""]:
        print("Thank you for your order.")
        break
    else:
        True
    
print(f"\nYour total bill is: £{total:.2f}")