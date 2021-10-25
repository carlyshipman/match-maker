#Carly Shipman
#Matchmaker


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
MAX_SCORE = 5 *len(QUESTION)
response = []
compatability = []

print(INTRODUCTION)

#ask all questions

for i in range(len(QUESTION)):
	def requestaValidNumberBetween1and5():
		UserResponse2String= str(input(QUESTION[i]))
		print("you entered: "+ UserResponse2String)

		if not UserResponse2String.isnumeric():
			print("This is not a number!")
			return False
		else:
			UserResponse2Int = int(UserResponse2String)
			if (UserResponse2Int < 1) or (UserResponse2Int > 5):
				print("\n This is not a number between 1 and 5 >:(")
				return False
			else:
				return True
	
	userHasEnteredANumberBetween1and5 = False
	while not userHasEnteredANumberBetween1and5:
		userHasEnteredANumberBetween1and5 = requestaValidNumberBetween1and5()
		print(userHasEnteredANumberBetween1and5)
		if not (userHasEnteredANumberBetween1and5):
			print("please try again.")
	
	response.append(UserResponse2String)
	questionCompatibility = 5 - abs(userResponse2String - DESIRED_RESPONSE[i])
    	compatability.append(questionCompatibility)

	# String formatting with parameters and placeholders.
    	print('Question %d compatability: %d' % (i+1, questionCompatibility))

	
#Carly Shipman
#Matchmaker


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
response = []
compatability = []

print(INTRODUCTION)

#ask all questions


def requestaValidNumberBetween1and5():
    for i in range(len(QUESTION)):
		UserResponse2String= str(input(QUESTION[i]))
		    print("you entered: "+ UserResponse2String)

		if not UserResponse2String.isnumeric():
			print("This is not a number!")
			return False
		else:
			UserResponse2Int = int(UserResponse2String)
			if (UserResponse2Int < 1) or (UserResponse2Int > 5):
				print("\n This is not a number between 1 and 5 >:(")
				return False
			else:
				return True
	
	userHasNotEnteredANumberBetween1and5 = False
	while not userHasNotEnteredANumberBetween1and5:
		userHasNotEnteredANumberBetween1and5 = requestaValidNumberBetween1and5()
		print(userHasNotEnteredANumberBetween1and5)
		if not (userHasNotEnteredANumberBetween1and5):
			print("please try again.")
	
	response.append(UserResponse2String)
	questionCompatibility = 5 - abs(userResponse2String - DESIRED_RESPONSE[i])
    compatability.append(questionCompatibility)

	# String formatting with parameters and placeholders.
    print('Question %d compatability: %d' % (i+1, questionCompatibility))

	
