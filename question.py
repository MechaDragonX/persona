#!/usr/bin/env python

from xmlrpc.client import Boolean
import character

class Question:
    title = ''
    answers = { '': None }

    def __init__(self, title) -> None:
        self.title = title
    
    def __addAnswer(self, answer, character):
        self.answers.update({answer: character})

    def importAnswers(self, answers, characters) -> Boolean:
        if len(answers) != len(characters):
            return False

        i = 0
        while i < len(answers):
            self.answers.update({answers[i]: characters[i]})
