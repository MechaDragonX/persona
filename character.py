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
