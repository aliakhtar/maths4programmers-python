from ch06.Vector import *

from math import isclose


class TitanicPassenger(Vector):

    def __init__(self, survived, p_class, age, siblings, kids, fare,
                 name="<virtual>", sex="<virtual>"):
        self.survived = survived
        self.p_class = p_class
        self.age = age
        self.siblings = siblings
        self.kids = kids
        self.fare = fare
        self.name = name
        self.sex = sex

    def add(self, other):
        # survival_prob = (self.survived + other.survived) / 2
        return TitanicPassenger(
            self.survived + other.survived,
            self.p_class + other.p_class,
            self.age + other.age,
            self.siblings + other.siblings,
            self.kids + other.kids,
            self.fare + other.fare
        )

    def scale(self, s):
        return TitanicPassenger(
            self.survived * s,  # needed to correctly calc avgs
            self.p_class * s,
            self.age * s,
            self.siblings * s,
            self.kids * s,
            self.fare * s
        )

    def __repr__(self):
        return "TitanicPassenger(survived={}, p_cls = {}, age = {}, siblings = {}, kids = {}, fare = {}, name = {}, " \
               "sex = {} ".format(self.survived, self.p_class, self.age, self.siblings, self.kids, self.fare, self.name,
                                  self.sex)

    @classmethod
    def zero(cls):
        return TitanicPassenger(
            0,
            0,
            0,
            0,
            0,
            0
        )

    @classmethod
    def approx_eq(cls, a, b):
        return \
            isclose(a.p_class, b.p_class) and \
            isclose(a.age, b.age) and \
            isclose(a.siblings, b.siblings) and \
            isclose(a.kids, b.kids) and \
            isclose(a.fare, b.fare)
