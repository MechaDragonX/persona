#!/usr/bin/env python

import enum

class Gender(enum.Enum):
    Male = 0,
    Female = 1,
    Nonbinary = 2,
    Fluid = 3

class Character:
    given_name = ''
    surname = ''
    other_name = ''
    gender = Gender.Male
    age = 0
    profession = ''
    description = ''

    def __init__(self, given_name, surname, gender, age, profession) -> None:
        self.given_name = given_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.profession = profession
