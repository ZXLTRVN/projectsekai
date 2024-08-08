import random

print('Welcome to  Yolia\'s Dice')

# enter what sided dice: select from D3, D4, D6, D8, D10, D10, D12, and D100
dicetype = input('What kind of dice would you like to roll?')
dicetype = int(dicetype)

# enter number of dice
x = input('How many dice would you like to roll?')
diceamount = parse_input(x)


threesided = random.randint(1,3)
foursided = random.randint(1,4)
sixsided = random.randint(1,6)
eightsided = random.randint(1,8)
tensided = random.randint(1,10)
twelvesided = random.randint(1,12)
hundredsided = random.randint(1,100)

if dicetype == 'D3':
    print("You rolled",threesided)
elif dicetype == 'D4':
    print("You rolled",foursided)
elif dicetype == 'D6'
    print("You rolled",sixsided)
elif dicetype == 'D8'
    print("You rolled",eightsided)
elif dicetype == 'D10'
    print("You rolled",tensided)
elif dicetype == 'D12'
    print("You rolled",twelvesided)
elif dicetype == 'D100'
    print("You rolled",hundredsided)

mod = input('Input modifier:')
mod = int(mod)


repeat = True
while repeat:
    print("Your final result is",random.randint(1,6))
    print("Do you want to roll again? Y/N")
    repeat = "Y" in input()

#a modifier to add to the result.