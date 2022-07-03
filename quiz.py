#!/usr/bin/env python

import character
import question

class Quiz:
    name = ''
    characters = []
    questions = []

    def __init__(self, name, characters, questions) -> None:
        self.name = name
        self.characters = characters
        self.questions = questions
