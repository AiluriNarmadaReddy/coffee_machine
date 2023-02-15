import resource_sufficiency as rs
import menu as mn
import process_coins as pc
import make_coffee as mk
import add_resources as ad

# TODO:1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
type_coffee = 7
while type_coffee != 5:
    type_coffee = int(input("CHOOSE YOUR OPTION \n1.espresso\n2.latte\n3.cappuccino\n4.do you require the "
                            "report\n5.off the coffe machine\n6.add resources to the coffee machine"))
    # TODO:2.Turn off the Coffee Machine by entering “off” to the prompt.
    if type_coffee == 5:
        print("\n\ncoffee machine turned off")
    # TODO:3.Print report.
    elif type_coffee == 4:
        print(mn.resources)
    elif type_coffee == 6:
        ad.add_resources()

    # TODO:4.Check resources sufficient?
    if type_coffee != 4 and type_coffee != 5 and type_coffee!=6:
        print("water sufficiency:")
        print(rs.water_sufficiency(type_coffee))
        print("coffee sufficiency")
        print(rs.coffee_sufficiency(type_coffee))
        print("milk_sufficiency")
        print(rs.milk_sufficiency(type_coffee))
    # TODO:5.Process coins.
    # TODO:6.Check transaction successful?
        if rs.water_sufficiency(type_coffee) and rs.coffee_sufficiency(type_coffee) == True and rs.milk_sufficiency(
            type_coffee) == True:
            pc.process_coins(type_coffee)
            # TODO:7.Make Coffee.
            mk.make_coffee(type_coffee)
            mk.changed_resources(type_coffee)

