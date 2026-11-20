class Ticket:
    def __init__(self, film_nomi, chipta_narxi, chipta_soni):
        self.film_nomi = film_nomi
        self.chipta_narxi = chipta_narxi
        self.chipta_soni = chipta_soni

    def total_cost(self):
        return self.chipta_narxi * self.chipta_soni

    def show_info(self):
        print(f"Film: {self.film_nomi}")
        print(f"Umumiy xarajat: {self.total_cost()}")


t = Ticket("Avatar", 40000, 3)

print(t.total_cost())
t.show_info()