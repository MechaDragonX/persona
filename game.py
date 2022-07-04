#!/usr/bin/env python

from character import Character
from question import Question
from quiz import Quiz

class Game:
    quiz: Quiz = None
    answers_chosen: list[str] = []
    characters_chosen: list[Character] = []

    def __init__(self, quiz) -> None:
        self.quiz = quiz
