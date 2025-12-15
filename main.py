class Player:
    def __init__(self, name, score=0, level=1):
        self.name = name
        self.score = score
        self.level = level

    def add_points(self, points):
        self.score += points

    def level_up(self):
        self.level += 1

    def __str__(self):
        return f"Name: {self.name}, Score: {self.score}, Level: {self.level}"


p = Player("Ali")
print(p)
p.add_points(50)
print(p)
p.level_up()
print(p)
