#!/usr/bin/env python

import character

class Question:
    title = ''
    answers = { '': None }

    def __init__(self, title) -> None:
        self.title = title
