"""
Создайте класс Pizza, который принимает список ингредиентов.
Класс поддерживает:
 атрибут order_number, который возвращает текущий номер заказа
 атрибут ingredients, который возвращает список, принятый в конструкторе
 функции (pepperoni, hawaiian, margherita) создания видов пицц, ингредиенты которых заранее известны (см. таблицу).
Name - Ingredients
hawaiian - ham, pineapple
pepperoni - bacon, mozzarella, oregano
margherita - mozzarella, olives, tomatoes
Примеры:
p1 = Pizza(['bacon', 'parmesan', 'ham'])    # order 1
p2 = Pizza.pepperoni()                  # order 2
p1.ingredients ➞ ['bacon', 'parmesan', 'ham']
p2.ingredients ➞ ['bacon', 'mozzarella', 'oregano']
p1.order_number ➞ 1
p2.order_number ➞ 2
"""


class Pizza:
    order_number = 0
    ingredients = []

    def __init__(self, list_of_ingredients):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self.ingredients = list_of_ingredients

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def pepperoni(cls):
        return cls(["bacon", "mozzarella", "oregano"])

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "olives", "tomatoes"])


p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.pepperoni()
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)
print(p2.order_number)
