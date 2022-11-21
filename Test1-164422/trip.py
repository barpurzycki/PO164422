class Trip:
    def __init__(self, goal: str, price: float):
        self.goal = goal
        self.price = price

    def wyswietl(self):
        print(self.goal, self.price)
