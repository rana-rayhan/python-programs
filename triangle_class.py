class Triangle:
    base = 0
    height = 0

    # constructor --**
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # function --**
    def display(self, tName):
        area = 0.5 * self.base * self.height
        print(f"{tName} area: {area}")


# class objects
t1 = Triangle(10, 20)
t2 = Triangle(20, 30)

t1.display("T1")
t2.display("T2")
