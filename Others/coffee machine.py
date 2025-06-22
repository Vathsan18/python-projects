
def restore_resources(ci):
    global resources
    for i in ci:
        resources[i] += ci[i]

def make_coffee(ci):
    global resources
    for i in ci:
        if i in resources:
            resources[i] -= ci[i]
    for i in resources:
        if resources[i] < 0:
            print("Sorry! Insufficient ingredients in machine. Please refill to continue.")
            print()
            restore_resources(ci)
            return False
    return True


def make_payment(ml, cost):
    global resources
    try:
        ml[0] = int(input("Enter no. of pennies: ")) * 0.01
        ml[1] = int(input("Enter no. of nickels: ")) * 0.05
        ml[2] = int(input("Enter no. of demis: ")) * 0.10
        ml[3] = int(input("Enter no. of quarters: ")) * 0.25
        for i in ml:
            if i < 0:
                raise TypeError
    except :
        print("Please enter valid no. of coins.")
    print()
    tm = sum(ml)
    if tm < cost:
        print(f"Insufficient money! Here is {tm} in return.")
        return False
    else:
        resources["money"] += cost
        if tm - cost > 0:
            print(f"Here is change of {round((tm - cost),2)}.")
        return True

def view_resources():
    global resources
    print(f'''
water   - {resources["water"]}/300mL
milk    - {resources["milk"]}/100mL
coffee  - {resources["coffee"]}/100g
monry   - {resources["money"]}''')


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
    "money" : 0
}

order = True
flavors = {
    1 : "espresso",
    2 : "latte",
    3 : "cappuccino"
}

ingredients = {1 : ["water",300],
               2 : ["milk",200],
               3 : ["coffee",100]}

while order:
    ml = [0, 0, 0, 0]
    inpt = int(input(f'''What would you like to have? 
    1. espresso         - {MENU["espresso"]["cost"]}
    2. latte            - {MENU["latte"]["cost"]}
    3. cappuccino       - {MENU["cappuccino"]["cost"]}
    4. view resources
    5. refill resources
    6. Quit
    
    Enter [1/2/3/4/5/6] '''))
    print()
    if inpt in [1,2,3]:
        coffee = flavors[inpt]
        ci = MENU[coffee]["ingredients"]
        is_made = make_coffee(ci)
        if is_made:
            is_paid = make_payment(ml, MENU[coffee]["cost"])
        else:
            continue
        if is_made and is_paid :
            print(f"Here is your {coffee}. Have a nice day!")
        elif is_made and not is_paid :
            restore_resources(ci)
    elif inpt == 4:
        view_resources()
    elif inpt == 5:
        for i in [1,2,3]:
            add_item = ingredients[i][0]
            resources[add_item] = ingredients[i][1]
        print("Ingredients are refilled.")
        view_resources()

    else:
        print('Thank you!')
        quit()
    print()

