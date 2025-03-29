import random
number_of_guess = 5
random_number = int(random.randint(1, 30))
print(random_number)
while number_of_guess >= 1:
    n = int(input("Guess a number between 1 to 30\n", ))
    if n == random_number:
        print("you guessed it Correct!")
        break
    elif n > random_number:
        print("DOWN")
        number_of_guess -= 1
        print(f'you have {number_of_guess} amout of guesses left\n')
        if random_number>1:
            number_of_guess-=1
        continue
    elif n < random_number:
        print("UP")
        number_of_guess -= 1
        print(f'you have {number_of_guess} amout of guesses left\n')
        continue
if number_of_guess<=0:
    print(f'You have used all your chance, the correct answer was {random_number}')