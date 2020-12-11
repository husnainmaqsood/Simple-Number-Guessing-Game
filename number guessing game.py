
import random

number = random.randint(0,100)

guess = False

while(guess==False):
	n = int(input('Enter your guess: '))

	if(n == number):
		print('Congratulations !!! You guessed correctly')
		guess = True
	elif(n > number):
		print('Your guess is greater than the number')
	elif(n < number):
		print('Your guess is smaller than the number')
	elif(n < 0):
		break
