#Game brainstorming, game goals are to make a guessing game that also uses math logic to make user guess the number. Consider steps: one guess two numbers between 1 and 100, take sum of twn numbers and then maybe make the sum the new max?, repeat? trying to use classes and objects

print("Another cliche number guessing game\n")
print("Your objective is to guess 2 numbers between 1 and the sum of two numbers of your choice\n")
print("Once correctly guessed, you then need to guess a number between 1 and the sum of the two numbers from previous step\n")
import random

class Numberz():
	#class variable
	def __init__(self):
		
		#print(datetime.now())
		self.name = input("What is your name? \n\t:")
		print("Hello {}".format(self.name))
		self.num1 = input("What is your first number\n\t:")
		self.num2 = input("What is your second number\n\t:")
		self.num_sum = int(self.num1) + int(self.num2)
		self.guess_this = random.randint(1,self.num_sum)
		guess_this = self.guess_this
	
	def game_1(self):
		print("The sum of both of your numbers is {}".format(self.num_sum))
		print("You have unlimited guesses to choose correct number between 1 and {}".format(self.num_sum))
		guess = 0
		guess_counter = 0
		while guess != self.guess_this:
			guess = int(input("Guess:"))
			if guess < self.guess_this:
				print("Too low")
				guess_counter += 1
			elif guess > self.guess_this:
				print("too high")
				guess_counter += 1
		guess_counter += 1 
		print("Correct guess!")
		print("It took you {} guess(es)".format(guess_counter))
		print("Moving on to next challenge")
		
	def game_2(self):
		print("-"* 50)
		print("Your next challenge is to guess the correct factor that is the product of the number you guessed mutiplied by a number between 1 and 10")
		print("\nMeaning if your number was 2 and the random number was 4, the product equals 8 and the factors could be 1,2,4,8")
		print("\nHint: the higher the numbers you chose in the previous step may make the game more challenging!!")
		print(self.guess_this)
		new_rand_int = random.randint(1,10)
		#print(new_rand_int)
		multiple = new_rand_int * self.guess_this
		print("The product is {}".format(multiple))
		print("You have 2 tries to guess the correct factor")
		print("The possible options are:")
		
		multiple_list = []
		for i in range(1,multiple):
			
			if multiple % i == 0:
				multiple_list.append(i)
		print(multiple_list)
		rand_factor = random.choice(multiple_list)
		#print(rand_factor)
		try_counter = 0 
		guessed_correcty = False
		while try_counter < 2 and guessed_correcty == False:
			factor_guess = int(input("Guess the correct factor of {}\n\t:".format(multiple)))
			if rand_factor == factor_guess:
				print("correct!!\nThe correct guess:")
				guessed_correcty = True
				return factor_guess
			elif rand_factor != factor_guess: # needs a third conditional that will produce fail (duplicates one more try)
				try_counter += 1 
				print("One try left")
			
		return ("You failed to guess the correct number, please try again.")
		
	def game_3(self):
		
		

numberz_1 = Numberz()
numberz_1.game_1()
print(numberz_1.game_2())

