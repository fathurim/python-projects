MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15000,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30000,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def check_resource(drink_resource):
    for item in drink_resource:
        if drink_resource[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True 

def count_resource(drink_resource):
    for item in drink_resource:
        resources[item] -= drink_resource[item]

def insert_coin(choice):
    global profit
    money = int(input("Please input your money: Rp. "))
    if money < choice['cost']:
        print("Sorry, that's not enough money.")
        return False
    elif money == choice['cost']:
        profit += money
        print('Thanks, I will process your order.')
        return True
    else:
        exchange = money - choice['cost']
        profit += choice['cost']
        print(f"Here is Rp. {exchange} in change.")
        return True

while is_on:
    choice = input("What would you like? ('espresso', 'latte', or 'cappuccino'): ")

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources.get('milk', 0)} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: Rp. {profit}")
    
    elif choice in MENU:
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            if insert_coin(drink):
                count_resource(drink['ingredients'])
                print(f"Here is your {choice}. Enjoy!")
