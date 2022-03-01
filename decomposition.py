"""
    Decomposition techniques in mathematical programming,
    in particular linear programming, take advantage of the
    structure of the problems and the characteristics of the
    resolution method to solve smaller problems sequentially,
    ensuring the convergence of the complete problem to the
    optimum.
"""


class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._condition = 'en_reposo'
        self._motor = Motor(cylinders=4)

    def acelerar(self, type='despacio'):
        if type == 'rapida':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._condition = 'en movimiento'


class Motor:

    def __init__(self, cylinders, type='gasolina'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, capacidad):
        pass
