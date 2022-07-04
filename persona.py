#!/usr/bin/env python

from character import Character
from character import Gender
from game import Game
from question import Question
from quiz import Quiz

retsuko = Character('Retsuko', '', Gender.Female, 25, 'accountant', 'red panda', 'Aggretsuko')
retsuko.description = 'A timid, softly-spoken, and polite young woman who works diligently. She is a skilled singer due to her habit of singing death metal karaoke to destress.'

fenneko = Character('Fenneko', '', Gender.Female, 25, 'accountant','fennec fox')
fenneko.description = 'A quiet, perceptive, and can easily figure out what her co-workers are thinking just by watching their mannerisms. She is a self-proclaimed pro social media stalker.'

haida = Character('Haida', '', Gender.Male, 25, 'accountant', 'hyena')
haida.description = 'He is passive, indecesive, neurotic, often visibly anxious, and can be prone to bursts of anger. His lack of confidence is the biggest obstacle in his life.'

characters = [ retsuko, fenneko, haida ]

affinity = [ retsuko, fenneko, haida ]
q1 = Question('You have a crush on someone! What do you do?')
answers = [ 'ヘ(♥﹏♥ヘ)', 'I don\'t have crushes. I simply watch from the sidelines and shit on my friends.', 'U-uhhh I...don\'t do anything. Cuz, what if they don\'t like me back?' ]
q1.import_answers(answers, affinity)

q2 = Question('Oh no! You guys broke up! What do you do?')
answers = [ 'Fill my hole with a VR partner', 'Eh. Oh well. I\'d just move on and stalk someone else.', 'Be depressed and let it effect my interactions with others.' ]
q2.import_answers(answers, affinity)

q3 = Question('The day is over! What do you do?')
answers = [ 'Do my own thing or be forced to work overtime', 'Force people to go drinking with me', 'Drown my sorrows in alcohol and rant to my friends' ]
q3.import_answers(answers, affinity)

q4 = Question('You notice your friend making poor decisions. What do you do?')
answers = [ 'I can\'t be close enough with anyone at work to call them friends... Leave them alone.', 'Stage an intervention.', 'Consult a mutual friend about what to do.' ]
q4.import_answers(answers, affinity)

q5 = Question('Your job just isn\'t satisfying. What do you do?')
answers = [ 'Start a side gig.', 'I\'ve already been doing a side gig, so I don\'t care', 'Quit for greener pastures' ]
q5.import_answers(answers, affinity)

questions = [ q1, q2, q3, q4, q5 ]
aggretsuko = Quiz('Which Aggretsuko Character Are You?', characters, questions)
game = Game(aggretsuko)

print()
