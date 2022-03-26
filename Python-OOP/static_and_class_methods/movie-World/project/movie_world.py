from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    dvd_limit = 15
    customer_limit = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.dvd_limit

    @staticmethod
    def customer_capacity():
        return MovieWorld.customer_limit

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if customer.rented_dvds:
                            for customer_dvd in customer.rented_dvds:
                                if customer_dvd.id == dvd_id:
                                    return f"{customer.name} has already rented {dvd.name}"
                        elif dvd.is_rented:
                            return f"DVD is already rented"
                        elif customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} " \
                                f"to rent this movie"
                        else:
                            dvd.is_rented = True
                            customer.rented_dvds.append(dvd)
                            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        str_result = ""
        for c in self.customers:
            str_result += f"{repr(c)}\n"
        for d in self.dvds:
            str_result += f"{repr(d)}\n"
        return str_result

#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)