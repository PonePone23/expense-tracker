class Expense:

    def __init__(self, name, category,amount):
        self.name = name
        self.category = category
        self.amount = amount

    # def __str__(self):
    #     print(f"{self.name} {self.category} {self.amount}")

    def __repr__(self):
        return f"{self.name}, {self.category} , ${self.amount}"