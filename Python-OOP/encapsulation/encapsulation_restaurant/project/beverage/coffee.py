from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    _MILLILITERS = 50
    _PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, self._PRICE, self._MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value