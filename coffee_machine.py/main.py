'''
A simple coffee machine that allows users to turn it on/off,
view the drink menu, dispense drinks, and check the machine's earnings.

Attributes:
- money (float): The total earnings of the coffee machine.
- is_on (bool): The state of the coffee machine (True if on, False if off).
- menu (dict): A dictionary representing the available drinks and their details.

Methods:
- machine_on(): Turns on the coffee machine.
- machine_off(): Turns off the coffee machine.
- drink_menu(): Displays the menu of available drinks with their prices and availability.
- dispense_drink(drink): Dispenses the selected drink, updating earnings and availability.
- machine_takings(): Displays the current earnings of the coffee machine.
'''

class CoffeeMachine:
    def __init__(self):
        self.money = 0
        self.is_on = True
        self.menu = {
            'coffee': {'price': 1.20, 'available': 3},
            'latte': {'price': 1.50, 'available': 3},
            'cappuccino': {'price': 1.50, 'available': 3},
            'expresso': {'price': 1.00, 'available': 3},
        }

    def machine_on(self):
        self.is_on = True

    def machine_off(self):
        self.is_on = False

    def drink_menu(self):
        print("\nMENU:")
        for drink, details in self.menu.items():
            print(f"{drink}: £{details['price']:.2f} - AVAILABLE: {details['available']}.")

    def dispense_drink(self, drink):
        if drink not in self.menu:
            print("Invalid selection")
            return
        
        if self.menu[drink]['available'] > 0:
            cost = self.menu[drink]['price']
            self.money += cost
            self.menu[drink]['available'] -= 1
            print(f"Dispensing {drink}... Enjoy!")
        else:
            print(f"{drink} are out of stock.")

    def machine_takings(self):
        print(f"Current earnings are: £{self.money:.2f}")

coffee_machine = CoffeeMachine()

while True:
    print("\nOPTIONS:")
    print("1. Turn On")
    print("2. Turn Off")
    print("3. Display Menu")
    print("4. Dispense Drink")
    print("5. Check Earnings")
    print("6. Quit")

    user_choice = input("\nChoose an option: ").lower()

    if user_choice in ["6", "quit"]:
        break
    elif user_choice in ["1", "turn on", "turnon"]:
        coffee_machine.machine_on()
        print("Coffee machine is switched on")
    elif user_choice in ["2", "turn off", "turnoff"]:
        coffee_machine.machine_off()
        print("Coffee machine switching off...")
        break
    elif user_choice in ["3", "display menu", "displaymenu"]:
        coffee_machine.drink_menu()
        print("Coffee machine is switched off")
    elif user_choice in ["4", "dispense drink", "dispensedrink"]:
        drink_choice = input("Please choose a drink: ")
        coffee_machine.dispense_drink(drink_choice)
    elif user_choice in ["5", "check earnings", "checkearnings"]:
        coffee_machine.machine_takings()
    else:
        print("Invalid selection")
        break