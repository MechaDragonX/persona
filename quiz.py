#!/usr/bin/env python

from character import Character
from question import Question

class Quiz:
    name = ''
    characters: list[Character] = []
    questions: list[Question] = []

    def __init__(self, name, characters, questions) -> None:
        self.name = name
        self.characters = characters
        self.questions = questions
