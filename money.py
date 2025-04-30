

class Monkey:
    def __init__(self, name, favorite_food):
        self.name = name
        self.favorite_food = favorite_food
        self.energy = 100

    def eat(self):
        print(f"{self.name} is eating {self.favorite_food} 🍌")
        self.energy += 10
        print(f"Energy increased to {self.energy}.")

    def swing(self):
        if self.energy >= 20:
            print(f"{self.name} swings from tree to tree! 🌴")
            self.energy -= 20
            print(f"Energy now at {self.energy}.")
        else:
            print(f"{self.name} is too tired to swing. Needs to eat!")

    def sleep(self):
        print(f"{self.name} is sleeping... 😴")
        self.energy = 100
        print(f"{self.name} feels refreshed! Energy restored to {self.energy}.")

# Example usage
if __name__ == "__main__":
    george = Monkey("George", "bananas")
    
    george.swing()
    george.eat()
    george.swing()
    george.swing()
    george.sleep()
