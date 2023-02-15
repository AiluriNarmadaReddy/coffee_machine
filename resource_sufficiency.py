import menu as mn


def water_sufficiency(type_coffee):
    if mn.MENU[str(type_coffee)]["ingredients"]["water"] > mn.resources["water"]:
        #print("water: not sufficient in coffee machine ")
        return False
    else:
        #print("sufficient water")
        return True


def coffee_sufficiency(type_coffee):
    if mn.resources["coffee"] < mn.MENU[str(type_coffee)]["ingredients"]["coffee"]:
        #print("coffee: not sufficient in coffee machine ")
        return False
    else:
        #print("sufficient coffee")
        return True


def milk_sufficiency(type_coffee):
    if type_coffee == 1:
        #print("milk not required for espresso")
        return True
    if type_coffee == 2 or type_coffee == 3:
        if mn.resources["milk"] < mn.MENU[str(type_coffee)]["ingredients"]["milk"]:
            #print(" milk: not sufficient in coffee machine ")
            return False
        else:
            #print("sufficient milk")
            return True
