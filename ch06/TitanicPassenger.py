from ch06.Vector import *

class TitanicPassenger(Vector):

    def __init__(self, survived, p_class, sex,  age, siblings, kids, fare):
        self.survived = survived
        self.p_class = p_class
        self.sex = sex
        self.age = age
        self.siblings = siblings
        self.kids = kids
        self.fare = fare

    def add(self, other):
        pass

    def scale(self, other):
        pass

    @classmethod
    def zero(cls):
        pass