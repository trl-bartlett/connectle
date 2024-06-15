MENU = {  
    "espresso": {  
        "ingredients": {  
            "water": 50,  
            "coffee": 18,  
        },  
        "cost": 1.5,  
    },  
    "latte": {  
        "ingredients": {  
            "water": 200,  
            "milk": 150,  
            "coffee": 24,  
        },  
        "cost": 2.5,  
    },  
    "cappuccino": {  
        "ingredients": {  
            "water": 250,  
            "milk": 100,  
            "coffee": 24,  
        },  
        "cost": 3.0,  
    }  
}  
  
resources = {  
    "water": 300,  
    "milk": 200,  
    "coffee": 100,  
}  
  
# variables and functions  
ON = True  
profit = 0  
  
  
# print report  
def report():  
    print(f"Water: {resources['water']}")  
    print(f"Milk: {resources['milk']}ml")  
    print(f"Coffee: {resources['coffee']}g")  
    print(f"Money: ${profit}")  
  
  
# check if there are enough resources for chosen drink  
def is_resource_sufficient(order_ingredients):  
    """returns false if not enough resources, true if enough """  
    for item in order_ingredients:  
        if order_ingredients[item] >= resources[item]:  
            print(f"sorry there is not enough {item}")  
            return False  
        return True  
  
# process payment  
def process_coins():  
    """returns total payment from coins"""  
    print("please insert coins")  
    total = int(input("how many quarters:")) * 0.25  
    total += int(input("how many dimes:")) * 0.1  
    total += int(input("how many nickels:")) * 0.5  
    total += int(input("how many pennies:")) * 0.01  
    return total  
  
  
# check successful transaction  
def is_transaction_successful(money_received, drink_cost, ):  
    """returns true of payment is sufficient, false if not"""  
    if money_received >= drink_cost:  
        change = round(money_received - drink_cost, 2)  
        if change == 0:  
            print("thank you for exact change!")  
        else:  
            print(f"here is ${change} in change.")  
        global profit  
        profit += drink_cost  
        return True  
    else:  
        print("sorry that's not enough money...")  
        return False  
  
  
# make coffee  
def make_coffee(drink_name, order_ingredients):  
    for item in order_ingredients:  
        resources[item] -= order_ingredients[item]  
    print(f"here is your {drink_name}!")  
  
  
while ON:  
    # prompt user for coffee choice  
    choice = input("What would your like? Espresso, Latte, or Cappuccino?: ")  
    # check for turning off machine  
    if choice == "off":  
        ON = False  
    # check for report  
    elif choice == "report":  
        report()  
    # if espresso is chosen...  
    else:  
        drink = MENU[choice]  
        is_resource_sufficient(drink['ingredients'])  
        if is_resource_sufficient(drink['ingredients']):  
            payment = process_coins()  
            if is_transaction_successful(payment, drink['cost']):  
                make_coffee(choice, drink['ingredients'])