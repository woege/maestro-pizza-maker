# The maestro pizza maker is aware of the fact that the fat content of the ingredients is random and it is not always the same.
# Since fat is the most important factor in taste, the maestro pizza maker wants to know how risky his pizza menu is.

# TODO: define 2 risk measures for the pizza menu and implement them (1 - Taste at Risk (TaR), 2 - Conditional Taste at Risk (CTaR), also known as Expected Shorttaste (ES)

import numpy as np
import scipy.stats as st

from maestro_pizza_maker.pizza import Pizza
from maestro_pizza_maker.pizza_menu import PizzaMenu


def taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Similarity between the Taste at Risk and the Value at Risk is not a coincidence or is it?
    # Hint: Use function taste from Pizza class, but be aware that the higher the taste, the better -> the lower the taste, the worse
    mean_taste = np.mean(pizza.taste)
    std_taste = np.std(pizza.taste)
    z_score = st.norm.ppf(quantile)
    tar = mean_taste - z_score*std_taste
    return tar


def taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a menu
    # quantile is the quantile that we want to consider
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;)
    taste_menu = np.array([])
    for pizza in menu.pizzas:
        taste_menu = np.append(taste_menu, pizza.taste)

    mean_taste_menu = np.mean(taste_menu)
    std_taste_menu = np.std(taste_menu)
    z_score = st.norm.ppf(quantile)
    tar_menu = mean_taste_menu - z_score*std_taste_menu
    return tar_menu, taste_menu


def conditional_taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Simmilarity between the Conditional Taste at Risk and the Conditional Value at Risk is not a coincidence or is it?
    tar = taste_at_risk_pizza(pizza, quantile)
    ctar = np.mean(pizza.taste[pizza.taste < tar])
    return ctar


def conditional_taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a menu
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;) (same as for the taste at risk)
    tar_menu, taste_menu = taste_at_risk_menu(menu, quantile)
    ctar_menu = np.mean(taste_menu[taste_menu < tar_menu])
    return ctar_menu
