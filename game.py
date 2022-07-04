#!/usr/bin/env python

# from character import Character
# from question import Question
from quiz import Quiz

class Game:
    set = None
    answers_chosen = []
    characters_chosen = []

    def __init__(self, quiz) -> None:
        self.set = quiz
