class Circle:
    def __init__(self):
        measurement = input("Enter the radius or diameter: ")
        while not (measurement.isdigit() and float(measurement) > 0):
            measurement = input("Invalid. Enter a positive number: ")
        measurement = float(measurement)
        if measurement <=0:
            raise ValueError("It should be positive.")
        if measurement <=1:
            self.radius = measurement / 2
            self.diameter = measurement
        else:
            self.radius = measurement
            self.diameter = measurement * 2

    def area(self):
            return 3.14 * self.radius ** 2

    def perimeter(self):
            return 2 * 3.14 * self.radius
c = Circle()
print("Area:", c.area())
print("Perimeter:", c.perimeter())



