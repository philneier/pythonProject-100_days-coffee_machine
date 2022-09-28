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
# cash_accumulated = 0
# #
# # cash_accumulated = 0
# # drink_price = MENU[drink]['cost']
#
# def resource_report():
#
# def money_handling(drink_price):
#     quarters = int(input("how many quarters?"))
#     dimes = int(input("how many dimes?"))
#     nickles = int(input("how many nickles?"))
#     pennies = int(input("how many pennies?"))
#     total_coins = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
#     if total_coins >= drink_price:
#         print(f"You receive ${total_coins - drink_price} in change")
#         return drink_price
#     else:
#         print("Sorry, that's not enough money. Money refunded")
#         money_handling(drink_price)
#
# #
# #
# # order_resources = MENU[drink]['ingredients']
# # for i in order_resources:
# #     if resources[i] >= order_resources[i]:
# #         new_resource_amt = resources[i] - order_resources[i]
# #         resources = new_resource_amt
# #     else:
# #         print(f"Not enough {i} for your {drink}")
#
# def resource_calculation(drink):
#     ingredients_list = MENU[drink]['ingredients']
#     for i in ingredients_list:
#         if resources[i] < ingredients_list[i]:
#             print(f"Sorry, not enough {i} for your {drink}")
#             resource_calculation()
#             # print(f"Remaining reserves: \n{resources}")
#         else:
#             new_reserves = resources[i] - ingredients_list[i]
#             resources[i] = new_reserves
#             #print(f"Remaining reserves: \n{resources}")
#     return resources
#         # print(resources)
#
# def main_program():
#     drink = input("What would you like? (espresso/latte/cappuccino): ")
#     if drink == "report":
#         print(f"Resources:{resources}\nCash Accumulated: {cash_accumulated}")
#         main_program()
#     elif drink == "off":
#         print("goodbye")
#     else:
#         resources = resource_calculation(drink)
#         #print(f"Remaining resources: \n{resources}")
#         drink_price = MENU[drink]['cost']
#         print(f"a {drink} is ${drink_price}.")
#         cash_paid = cash_accumulated + money_handling(drink_price)
#         main_program()
#
# print(cash_accumulated)
# main_program()
# # print("------")
# # resource_calculation('cappuccino')
# # print("------")
# # resource_calculation('espresso')
# # print("------")
# # # print(f"Water: {(resources)['water']}")
# # # print(f"Milk: {(resources)['milk']}")
# # # print(f"Coffee: {(resources)['coffee']}")
# # # #print(f"Money: {cash_accumulated}")
# #
# #
# # # def is_enough_resources(drink):
# #     # print(drink)
# #     # for i in (MENU)['drink']['ingredients']:
# #     #     print(i)
# #
# # # print(is_enough_resources(cuppaccino))
# # # for var in MENU['cappuccino']['ingredients']:
# # #     print(var)
# # #
# for item in MENU:
#     print(MENU[item])
print("---1---")
for i in MENU:
    print(i)
print("---2---")
for i in MENU:
    print(MENU[i])
print("---3---")
for i, v in MENU.items():
    print(i, v)
for i in MENU.items():
    print(i)
print("---4---")
for i in MENU.values():
    print(i)
print("--5----")
for i in MENU.keys():
    print(i)
print("---6---")
drink = 'latte'
print(MENU[drink]['ingredients'])
print("---7---")
drink = 'latte'
for i in MENU[drink]['ingredients']:
    print(i, MENU[drink]['ingredients'][i])
print("---8----")
ingredients_list = MENU[drink]['ingredients']
print(ingredients_list)
print(ingredients_list['water'])
print("---9---")
for i, v in resources.items():
    print(i, v)
# #
# # # for i in ingredients_list:
# # #     order_amount = ingredients_list[i]
# # #     print(i)
# # #     print(order_amount)
# # #     new_reserves = resources[i] - order_amount
# # #     print(new_reserves)
# # #     resources[i] = new_reserves
# # #     print(resources)
