#I fucking failed this one because I didn't use global variables, like they fucking said not to...
#but guess what - I used a list and got it to work without a global.
#and made the currency numbers pretty, too. Ready for the next one.
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
cash_accumulated = []
def check_resources(drink):
    ingredients_list = MENU[drink]['ingredients']
    for i in ingredients_list:
        if resources[i] < ingredients_list[i]:
            print(f"Sorry, not enough {i} for your {drink}")
            main_program()
#            resource_calculation()
#             # print(f"Remaining reserves: \n{resources}")
def adjust_resources(drink):
    ingredients_list = MENU[drink]['ingredients']
    for i in ingredients_list:
        new_reserves = resources[i] - ingredients_list[i]
        resources[i] = new_reserves
            #print(f"Remaining reserves: \n{resources}")
    return resources
#         # print(resources)

def collect_money(drink):
    drink_price = MENU[drink]['cost']
    print(f"A {drink} is ${drink_price}.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    total_coins = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    if total_coins >= drink_price:
        change = '${:,.2f}'.format(total_coins - drink_price)
        print(f"You receive ${change} in change")
        adjust_resources(drink)
        cash_accumulated.append(drink_price)
        #return drink_price
        #return cash_accumulated
    else:
        print("Sorry, that's not enough money. Money refunded")
        main_program()


def main_program():
    #cash_accumulated = 0
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "report":
        for i, v in resources.items():
            print(i, v)
        total_cash = '${:,.2f}'.format(sum(cash_accumulated))
        print(f"Cash accumulated: {total_cash}")
        #print(cash_accumulated)
        main_program()
    elif drink == "off":
        print("Thank you. Goodbye")
    else:
        check_resources(drink)
        collect_money(drink)
        main_program()

main_program()