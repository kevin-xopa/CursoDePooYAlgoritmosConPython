# we create the Coordinate class
class Coordinate:
    # we create a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # we generate a method that receives an instance of the class Coordinate
    def distance(self, other_cordinate):
        x_diff = (self.x - other_cordinate.x)**2
        y_diff = (self.y - other_cordinate.x)**2
        return (x_diff + y_diff)**0.5


# if this file can be run from terminal, we can run it
if __name__ == '__main__':

    # we create two objects
    coord_1 = Coordinate(3, 30)
    coord_2 = Coordinate(4, 8)
    # we call the method distance and print the return value
    print(coord_1.distance(coord_2))

    # check that coord_2 is an instance of the class Coordinate
    print(isinstance(coord_2, Coordinate))
