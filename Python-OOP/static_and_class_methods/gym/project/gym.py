from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self,customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ""
        customer_id = 0
        trainer_id = 0
        plan_id = 0
        equipment_id = 0
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += repr(subscription) + "\n"
                customer_id = subscription.customer_id
                trainer_id = subscription.trainer_id
                plan_id = subscription.exercise_id
        for plan in self.plans:
            if plan.id == plan_id:
                equipment_id = plan.equipment_id
        for customer in self.customers:
            if customer.id == customer_id:
                result += repr(customer) + "\n"
        for trainer in self.trainers:
            if trainer.id == trainer_id:
                result += repr(trainer) + "\n"
        for equipment in self.equipment:
            if equipment.id == equipment_id:
                result += repr(equipment) + "\n"
        for plan in self.plans:
            if plan.id == plan_id:
                result += repr(plan)
        return result


