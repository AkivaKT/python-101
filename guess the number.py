import random

def letsguess():
    guess = input('Guess a number from 1 to 100: ')
    try:
        int(guess)
        return (int(guess), True)
    except:
        return (guess, False)

nvm = random.randint(1, 100)
nvmofguesses = 0
guess = letsguess()
gamefinished = False

while (guess[0] != nvm or gamefinished == False):
    if  (guess[1] == True and guess[0] < 100 and guess[0] > 0):
        nvmofguesses += 1
        if (guess[0] > nvm):
            print ('Guess too high')
            guess = letsguess()
        elif (guess[0] < nvm):
            print('Guess too low')
            guess = letsguess()
        else:
            if (nvmofguesses > 1):
                print ('You took {} guesses'.format(nvmofguesses))
            else:
                print ('You took 1 guess')
            gamefinished = True
            
    else:
        if type(guess[0]) == str:
            try:
                float(guess[0])
                print('{} is not a whole number. Try again'.format(guess[0]))
                guess = letsguess()
            except:
                print('{} is not a number. Try again'.format(guess[0]))
                guess = letsguess()
        else:
            print ('{} is not whitn 1-100'.format(guess[0]))
            guess = letsguess()
