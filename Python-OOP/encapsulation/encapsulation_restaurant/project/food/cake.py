from project.food.dessert import Dessert


class Cake(Dessert):
    _GRAMS = 250
    _CALORIES = 1000
    _PRICE = 5

    def __init__(self,name):
        super().__init__(name, self._PRICE, self._GRAMS, self._CALORIES)