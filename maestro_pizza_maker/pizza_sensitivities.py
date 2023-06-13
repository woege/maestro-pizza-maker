# The maestro pizza maker wants to fully understand of the properties of his pizza menu.
# Therefore he defines the follwing variables in the pizza industry known as "pizza menu sensitivities":
# 1. Delta - delta represents the rate of change between the price of the pizza and the amount of protein in the pizza
# 2. Gamma - gamma represents the rate of change between the price of the pizza and the amount of carbohydrates in the pizza
# 3. Vega - vega represents the rate of change between the price of the pizza and the amount of average_fat in the pizza

# TODO: implement the delta measure for a pizza menu
# hint: simple linear regression might be helpful

from maestro_pizza_maker.pizza_menu import PizzaMenu


def menu_sensitivity_protein(menu: PizzaMenu) -> float:
    # TODO: implement the delta measure for a pizza menu
    pass


def menu_sensitivity_carbs(menu: PizzaMenu) -> float:
    # TODO: implement the gamma measure for a pizza menu
    pass


def menu_sensitivity_fat(menu: PizzaMenu) -> float:
    # TODO: implement the vega measure for a pizza menu
    pass
