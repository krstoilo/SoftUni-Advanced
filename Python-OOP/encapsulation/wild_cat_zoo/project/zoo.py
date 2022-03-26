class Zoo:
    def __init__(self, name, budget, animals_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animals_capacity = animals_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def workers_capacity(self):
        return self.__workers_capacity
    
    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value
        
    @property
    def animals_capacity(self):
        return self.__animals_capacity
    
    @animals_capacity.setter
    def animals_capacity(self, value):
        self.__animals_capacity = value

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    def add_animal(self, animal, price):
        if self.budget < price:
            return "Not enough budget"
        elif self.budget >= price and self.__animals_capacity > 0:
            self.animals.append(animal)
            self.__animals_capacity -= 1
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        else:
            return f'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        for w in self.workers:
            if worker_name == w.name:
                self.workers.remove(w)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if self.budget >= total_salaries:
            self.budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.budget}'
        else:
            return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_care_amount = sum(a.money_for_care for a in self.animals)
        if self.budget >= total_care_amount:
            self.budget -= total_care_amount
            return f'You tended all the animals. They are happy. Budget left: {self.budget}'
        else:
            return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        lions = []
        tigers =[]
        cheetahs = []
        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a)
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a)
            elif a.__class__.__name__ == "Cheetah":
                cheetahs.append(a)
        l_str = "\n".join(repr(l) for l in lions)
        t_str = "\n".join(repr(t) for t in tigers)
        c_str = "\n".join(repr(c) for c in cheetahs)
        return f'''You have {len(self.animals)} animals
----- {len(lions)} Lions:
{l_str}
----- {len(tigers)} Tigers:
{t_str}
----- {len(cheetahs)} Cheetahs:
{c_str}'''

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(w)
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(w)
            elif w.__class__.__name__ == "Vet":
                vets.append(w)
        k_str = "\n".join(repr(k) for k in keepers)
        c_str = "\n".join(repr(c) for c in caretakers)
        v_str = "\n".join(repr(v) for v in vets)
        return f'''You have {len(self.workers)} workers
----- {len(keepers)} Keepers:
{k_str}
----- {len(caretakers)} Caretakers:
{c_str}
----- {len(vets)} Vets:
{v_str}'''



