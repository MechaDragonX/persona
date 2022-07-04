#!/usr/bin/env python

# import character
# import question
import quiz

class Game:
    set = None
    answers_chosen = []
    characters_chosen = []

    def __init__(self, quiz) -> None:
        self.set = quiz
