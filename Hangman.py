from Hangman_art import stages, logo
from random import choice
words=['strawberry']
new_word=list(choice(words))
print(logo)
underscores = ['_'] * len(new_word)
number_of_tries=6
where_it_is=1
while number_of_tries > 0:
    print(stages[number_of_tries])
    for i in underscores:
        print(i,end=" ")
    print("")

Guess = input("Enter a letter\n")
    for i in new_word:
        if i == Guess:
            Location=new_word.index(i)
            underscores[location]=i
            where_it_is = where_it_is + 1
            continue
        if i != n:
            number_of_tries=number_of_tries-1
if number_of_tries=0:
    print("you have lost all your chances")
    print(f'the answer was{new_word}')




