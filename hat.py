def rog():
    score_board = 'your current score is'
    command = input('do you want to play drive tut').strip().lower()

    if command == 'yes':
        while True:
            command = input('      Main Menu\nhelp\nstart\nstop\nquit\n').strip().lower()
            if command == 'help':
                print("""start: starts the car\naccelerate: makes it go faster, type accelerate to speed up
stop: stops the car\nquit ends the game\ntype "ok" to go back to the game""")
                f = input('...').strip().lower()
                if f == 'ok':
                    continue
            elif command == 'start':
                enter = (input('''use these buttons to drive your car \n w,a,s,d
 ''').strip().lower())
                p = 0
                while p < 100:
                    if enter == 'w':
                        print('your car has moved forward')
                        p += 1
                        print(f'{score_board} {p}')
                    elif enter == 'a':
                        print('your car has moved to the left')
                        print(f'{score_board} {p}')
                    elif enter == 'd':
                        print('your car has moved to the right')
                        print(f'{score_board} {p}')
                    elif enter == 's':
                        print('your car has moved backwards')
                        p -= 1
                        print(f'{score_board} {p}')
                    elif enter == 'a' and 'd':
                        print('your car is drifting')
                        p += 1
                        print(f'{score_board} {p}')
                    else:
                        print('invalid command\n restart')
                        continue
                else:
                    print('you have reached the end of our game thank you for playing')
                    ult = input('would you like the play replay').strip().lower()
                    if ult == 'yes':
                        continue
                    else:
                        break
            elif command == 'stop':
                print('your car is stopped')
                kit = input('would you like the restart').strip().lower()
                if kit == 'yes':
                    continue
                else:
                    break
            elif command == 'quit':
                break
            else:
                print('i dont understand that')
                continue

    else:
        print('good bye'.title())

rog()

# def aminu(e):
#     maximum = e[0]
#     for number in e:
#         if number > maximum:
#             maximum = number
#     return (maximum)
#
# file_path = "my notes"
# file = open(file_path)
# content = file.read()
# print(content)
# file.close()
# with open(file_path) as file:
#     content = file.read()
#     print(content)
# with open(file_path, mode="a") as file:
#     content = file.write("5")
#     print(content)
# import math
#
# hind = math.sqrt(36)
# print(hind)
# import datetime
# today = datetime.datetime.now().day
# day = datetime.datetime.now().month
# year = datetime.datetime.now().year
# print(f'{today}/{day}/{year}')
