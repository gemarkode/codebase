import keyboard
import time
import string

print('Welcome to the mastermind game!')
print('')
time.sleep(1)
print('For the game to start press the enter key')
keyboard.wait('enter')
print('')
print('')
print('This game is all about guessing the right combination of some random characters')
print('')
time.sleep(3)
print('Now you will be given 6 digits')
print('The Master combination will be 5 digits and it is up to you to guess the correct combination')
print('')
time.sleep(3)
print('For each digit you will be getting 4 tries to make the right combination')
print('')
print('Goodluck!')
print('')
print('Press enter to start the game!')
keyboard.wait('enter')

chars = []
charsAsString = ''
for x in range(6):
    char = random.choice(string.ascii_lowercase)
    chars += char
    charsAsString += char
chars.pop(random.randint(0,5))
random.shuffle(chars)
print('Your random characters:' + charsAsString, chars)
tries = 0
combination
while True:
    key = keyboard.read_key()
    if key == chars[0]:
        combination += key
        print('That one is correct! move on to the next character')
        print('')
        print('Current combination: ' + combination)
        print('Available characters: ' + charsAsString)
        tries = 0
        chars.pop(0)
        if not len(chars) > 0:
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('! You are a mastermind !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            exit()
    else:
        if tries == 3:
            print('')
            print('Game over')
            exit()
        tries = tries + 1
        print('')
        print('That is not the one, Keep looking')
        print('Current tries: '+str(tries))
