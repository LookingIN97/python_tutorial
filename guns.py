
# super class
class Guns():
    def __init__(self):
        self.fireable = True
        self.random_possibility = 0.5
        self.dmg = None
        self.bullets = None
        self.magezine = None

    def fire(self):
        print("Damage dealt: ", self.dmg)

    def reload(self):
        if self.bullets != self.magezine:
            self.bullets = self.magezine


# sub class
class M4(Guns):
    def __init__(self, bullets):
        self.fireable = True
        self.random_possibility = 0.5
        self.dmg = 80
        self.range = 100
        self.bullets = bullets
        self.magezine = 30

    def add_aim(self, level):
        if level == 1:
            self.range = 200
        elif level == 2:
            self.range = 300


if __name__ == "__main__":
    # object
    first_m4 = M4(30)
    # objectName <----- className()
    first_m4.fire()
    # objectName.attribute()
    #            method()
    first_m4.add_aim(2)
