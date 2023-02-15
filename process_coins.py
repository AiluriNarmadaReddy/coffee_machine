# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

import menu as mn


def process_coins(type_coffee):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    no_of_quarters = int(input("enter the number of quarters"))
    no_of_dimes = int(input("enter the number of dimes"))
    no_of_nickles = int(input("enter the number of nickles"))
    no_of_pennies = int(input("enter the number of pennies"))
    total_amount = (no_of_quarters * quarters) + (no_of_dimes * dimes) + (no_of_nickles * nickles) + (
                no_of_pennies * pennies)
    if total_amount < mn.MENU[str(type_coffee)]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_amount > mn.MENU[str(type_coffee)]["cost"]:
        print(f"you inserted {total_amount}\n but the coffee is {mn.MENU[str(type_coffee)]['cost']}\n")
        print(f"refunded amount is {total_amount - mn.MENU[str(type_coffee)]['cost']}")
        return True
    else:
        print(f"money inserted is sufficient to give you coffee")
        return True
