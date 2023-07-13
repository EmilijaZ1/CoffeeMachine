from resources import MENU, resources

selected = input("what would you like? (espresso/latte/cappucino): ")
print(MENU[selected])
coffee = MENU[selected]

#check resourses

water_left = float(resources['water']) - float(MENU[selected]['ingredients']['water'])
milk_left = float(resources['milk']) - float(MENU[selected]['ingredients']['milk'])
coffee_left = float(resources['coffee']) - float(MENU[selected]['ingredients']['coffee'])

if water_left < 0 and milk_left < 0 and coffee_left < 0:
    print("Not enough resources")
else:
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    print(total)
    change = total - float(MENU[selected]['cost'])
    if change < 0:
        [print("not enough money")]
    else:
        print(f"Here is change")
        print(change)


