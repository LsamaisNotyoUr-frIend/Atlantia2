import random
melri = input('Ada would you like to play').strip().upper()
els = 0
number = random.randint(1, 100)
if melri == 'YES':
    ellie = True
    while ellie:
        geh = int(input("guess a number any number"))
        if geh == number:
            els += 1
            print('you have won')
            print(f'you made {els} guesses')
            N = input('would you like to play again').strip().upper()
            if N == 'YES':
                continue
            else:
                break
        elif geh > number:
            print('Hint: take it easy a little bit')
            print('try again')
            els += 1
            if els == 3:
                print('you have failed')
                dennen = input('would you like to play again').strip().upper()
                if dennen == 'YES':
                    continue
                else:
                    break
        elif geh < number:
            print('Add a little more effort')
            print('try again')
            els += 1
            if els == 3:
                print('you have failed')
                dennen = input('would you like to play again').strip().upper()
                if dennen == 'YES':
                    continue
                else:
                    break
else:
    print('Bye')






