#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini


class Flower:

    def __init__(self, name):
        self.name = name

    def bloom(self):
        print("flower is blooming")

    def die(self):
        print("flower is dead")


class Iris(Flower):
    def __init__(self):
        super().__init__("IRIS")

    def bloom(self):
        super().bloom()
        print("the flower is " + self.name)

    def die(self):
        print("dead!!!!!!!")


class Violet(Flower):
    def __init__(self):
        super(Violet, self).__init__("VIOLET")

    def bloom(self):
        print("violet is blooming")


flower = Flower("Rose")
flower.bloom()
flower.die()

violet = Violet()
violet.bloom()
violet.die()

iris = Iris()
iris.bloom()
iris.die()


