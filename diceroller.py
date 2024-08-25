
import random

print('Welcome to Yolia\'s Dice! <3')

## enter what sided dice: select from D3, D4, D6, D8, D10, D10, D12, and D100
#dicetype = input('What kind of dice would you like to roll?')
#dicetype = int(dicetype)

## enter number of dice
#x = input('How many dice would you like to roll?')
#diceamount = parse_input(x)

print('How many dice would you like to roll?')

## user validation
while True:
    try:
        chosen_num = int(input('Enter a number between 1 and 10: '))
        if (chosen_num > 0 and chosen_num < 10):
            break
        else:
            print('Invalid input. Please try again.')
    except:
        print('Please enter a numerical value.')

def rollD6(diceamount):
    totalSum = 0
    possibleFaces = [1, 2, 3, 4, 5, 6]
    for die in range(diceamount):
        roll = random.choice(possibleFaces)
        print('Result', die + 1, ':', roll)
        totalSum += roll
    print('Total Sum: ', totalSum)

rollD6(chosen_num)