#Carly Shipman
#Matchmaker Lite - Part 2

INTRODUCTION = '''
Matchmaker 2021


Hello, here you can learn if you and I
are a perfect match! To see, anwser the
following questions with an number 1-5.
1 meaning completely disagree, 3 means
in between,and 5 meaning completely agree.
after completing each question, you will
receive a compability score. The higher,
the more compabitable we are. Good luck!

'''

QUESTION = [
    'Ironman is the best MCU character',
    'Calculus is dumb',
    'Running is really fun',
    'Matcha tastes like grass',
    'Hippo Campus is the best band ever'
]

DESIRED_RESPONSE =[
    5, #strongly agree
    1, #strongly disagree
    5, #srongly agree
    2, #agree
    5, #strongly agree
]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

# Ask alll questions


response = []
compatability = []

# Ask all questions.
for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    #Todo: Validate response and ask quesion again if necessary

    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatability.append(questionCompatibility)

    # String formatting with parameters and placeholders.
    print('Question %d compatability: %d' % (i+1, questionCompatibility))


totalCompatability = 0
for c in compatability:
    totalCompatability += c

totalCompatability *= 100 / MAX_SCORE
print('Total Compatability: %d\n\n' % (totalCompatability))

#Todo: Determine compatability ranges