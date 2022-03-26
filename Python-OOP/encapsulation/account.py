class Account:
    def __init__(self, account_id, balance, pin):
        self._account_id = account_id
        self.balance = balance
        self.__pin = pin

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    def get_id(self, pin):
        if pin == self.pin:
            return self.account_id
        else:
            return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin"


account = Account(1234, 44, 4444)
print(account.get_id(1234))
print(account.get_id(4444))
print(account.balance)
print(account.change_pin(4444, 1234))
print(account.change_pin(1234, 9999))
