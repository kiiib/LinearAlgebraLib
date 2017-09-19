from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise ValueError('The coordinates must be an iterable')

    def magnitude(self):

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n)
        #     new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    

my_vector = Vector([1,2,3])
# print(my_vector)
# my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])
print(my_vector.plus(my_vector3))
# print(my_vector == my_vector2)
# print(my_vector2 == my_vector3)