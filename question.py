#!/usr/bin/env python

from character import Character

class Question:
    title = ''
    answers = { '': None }

    def __init__(self, title) -> None:
        self.title = title

    def import_answers(self, answers, characters) -> bool:
        if len(answers) != len(characters):
            return False

        i = 0
        while i < len(answers):
            self.answers.update({answers[i]: characters[i]})
            i += 1
