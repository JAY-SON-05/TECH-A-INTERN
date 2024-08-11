import random

attempts = 0
def easy_or_hard():
    global attempts
    attempts -= 1
    user = int(input('Make a guess: '))
    while attempts > 0:
        if user == comp:
            return (f'your guess is right, Number:{comp}')
        if user > comp:
            print (f'Your guess is too high')
            print (f'You have {attempts} attempts Remaining')
            return (easy_or_hard())
        if user < comp:
            print (f'Your guess is too low')
            print (f'You have {attempts} attempts Remaining')
            return (easy_or_hard())
    return (f"You are out of guesses.. You lose\nNumber is {comp}")

comp = random.randrange(1,51)
print('Welcomes to Guess a Number Game\nLet me think of a number between 1 to 50')
level = input('Choose level of difficulty... Type(easy or hard): ').lower()

if level == 'easy':
    attempts = 10
    print (f'You have 10 attempts')
    print(easy_or_hard())
if level == 'hard':
    attempts = 5
    print (f'You have 5 attempts')
    print(easy_or_hard())
