#!/usr/bin/env python

from enum import Enum

class Gender(Enum):
    Male = 0,
    Female = 1,
    Nonbinary = 2,
    Fluid = 3

class Character:
    given_name = ''
    surname = ''
    alias = ''
    # Species
    race = ''
    gender = Gender.Male
    age = 0
    profession = ''
    description = ''

    def __init__(self, given_name, surname, gender, age, profession, race = '', alias = '') -> None:
        self.given_name = given_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.profession = profession

        self.race = race
        self.alias = alias
