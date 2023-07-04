from enum import Enum

import numpy as np
import pandas as pd

from maestro_pizza_maker.pizza import Pizza
from maestro_pizza_maker.ingredients import PizzaIngredient, IngredientType
from maestro_pizza_maker.pizza_menu import PizzaMenu

class TestPizzaIngredients(Enum):
    TEST_SAUCE_1 = PizzaIngredient(
        name="TEST SAUCE1",
        price=1.5,
        type=IngredientType.SAUCE,
        protein=2.5,
        fat=np.array([0,1,2,3]),
        carbohydrates=3.5,
        calories=5.5,
    )
    TEST_DOUGH_1 = PizzaIngredient(
        name="TEST DOUGH1",
        price=2.5,
        type=IngredientType.DOUGH,
        protein=3.5,
        fat=np.array([4,5,6,7]),
        carbohydrates=4.5,
        calories=6.5,
    )
    TEST_SAUCE_2 = PizzaIngredient(
        name="TEST SAUCE2",
        price=6.5,
        type=IngredientType.SAUCE,
        protein=7.5,
        fat=np.array([10,11,12,13]),
        carbohydrates=8.5,
        calories=9.5,
    )
    TEST_DOUGH_2 = PizzaIngredient(
        name="TEST DOUGH2",
        price=3.5,
        type=IngredientType.DOUGH,
        protein=4.5,
        fat=np.array([14,15,16,17]),
        carbohydrates=5.5,
        calories=6.5,
    )

simple_test_pizza_1 = Pizza(
        sauce=TestPizzaIngredients.TEST_SAUCE_1,
        dough=TestPizzaIngredients.TEST_DOUGH_1,
    )

simple_test_pizza_2 = Pizza(
        sauce=TestPizzaIngredients.TEST_SAUCE_2,
        dough=TestPizzaIngredients.TEST_DOUGH_2,
    )


def test_average_fat() -> None:
    true_sauce_fat = TestPizzaIngredients.TEST_SAUCE_1.value.fat
    true_dough_fat = TestPizzaIngredients.TEST_DOUGH_1.value.fat
    true_avg_fat = (true_sauce_fat + true_dough_fat).mean()
    test_avg_fat = simple_test_pizza_1.average_fat
    
    np.testing.assert_almost_equal(test_avg_fat, true_avg_fat)


def test_name() -> None:
    name_1 = simple_test_pizza_1.name
    name_2 = simple_test_pizza_2.name
    assert name_1 != name_2


def test_taste() -> None:
    true_sauce_fat = TestPizzaIngredients.TEST_SAUCE_1.value.fat
    true_dough_fat = TestPizzaIngredients.TEST_DOUGH_1.value.fat
    true_taste = 0.05 * true_dough_fat + 0.2 * true_sauce_fat
    test_taste = simple_test_pizza_1.taste

    np.testing.assert_almost_equal(true_taste, test_taste)


def test_to_dataframe() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])

    df = pizza_menu.to_dataframe(sort_by="price", descendent=True)
    true_price = np.array([simple_test_pizza_2.price, simple_test_pizza_1.price])
    test_price = np.array(df["price"])
    np.testing.assert_almost_equal(true_price, test_price)


def test_chepeast_pizza() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])

    true_cheapest = simple_test_pizza_1.name
    test_cheapest = pizza_menu.cheapest_pizza.name
    assert true_cheapest == test_cheapest


def test_get_most_fat_pizza() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])
    
    true_most_fat = simple_test_pizza_2
    test_most_fat = pizza_menu.get_most_fat_pizza(0.5)
    assert true_most_fat == test_most_fat


def test_most_caloric_pizza() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])

    true_cheapest = simple_test_pizza_2.name
    test_cheapest = pizza_menu.most_caloric_pizza.name
    assert true_cheapest == test_cheapest


def test_add_pizza() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1])
    pizza_menu.add_pizza(simple_test_pizza_2)

    true_pizzas = [simple_test_pizza_1, simple_test_pizza_2]
    test_pizzas = pizza_menu.pizzas
    assert true_pizzas == test_pizzas


def test_remove_pizza() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])
    pizza_menu.remove_pizza(simple_test_pizza_2.name)

    test = pizza_menu.pizzas[0].name
    true = simple_test_pizza_1.name
    assert true == test

    try:
        pizza_menu.remove_pizza(12345)
    except ValueError as e:
        assert e.args[0] == "Pizza 12345 not in menu"


def test_length() -> None:
    pizza_menu = PizzaMenu(pizzas=[simple_test_pizza_1, simple_test_pizza_2])
    true_len = 2
    test_len = len(pizza_menu)
    assert true_len == test_len



