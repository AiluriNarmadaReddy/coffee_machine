import menu as mn


def make_coffee(type_coffee):
    print(f"here is your {mn.MENU[str(type_coffee)]['item']}")


def changed_resources(type_coffee):
    mn.resources["water"] = mn.resources["water"] - mn.MENU[str(type_coffee)]["ingredients"]["water"]
    mn.resources["coffee"] = mn.resources["coffee"] - mn.MENU[str(type_coffee)]["ingredients"]["coffee"]
    if type_coffee ==2 or type_coffee ==3:
        mn.resources["milk"] = mn.resources["milk"] - mn.MENU[str(type_coffee)]["ingredients"]["milk"]
