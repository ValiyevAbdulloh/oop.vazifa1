class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya -= amount

        if self.energiya < 0:
            self.energiya = 0

    def show_status(self):
        print(f"O‘yinchi: {self.ism}")
        print(f"Energiya: {self.energiya}")


p1 = Player("Hero")

p1.use_energy(35)

p1.show_status()