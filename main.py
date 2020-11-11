import random
import sys
import pyperclip
from os import system
system('title '+ 'PyPass')

# char dict
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '€', ';', '.', '\'', '/', '\"',
         '?', ',', '<', '>']
# program logo
print('''
\t\t██████  ██    ██     ██████   █████  ███████ ███████ 
\t\t██   ██  ██  ██      ██   ██ ██   ██ ██      ██      
\t\t██████    ████       ██████  ███████ ███████ ███████ 
\t\t██         ██        ██      ██   ██      ██      ██ 
\t\t██         ██        ██      ██   ██ ███████ ███████ 
\n                                  a password generator by CaptKraken
''')
print('#####################################################################################\n'
      '#    Password cracking depends on the length and the randomness of the password.    #\n'
      '#    I recommend having a password with at least 12 characters. just to be safe.    #\n'
      '#####################################################################################')

state = True

while state:
    max = 256
    pw = []
    spacer = '-------------------------------------------------------------------------------------\n'
    def func():
        print(spacer + 'type \'a\' to see information about the program.')
        ans = input('do you want to generate another password? y/n: ')[:1].lower()
        if ans == 'y':
            state = True
        elif ans == 'a':
            print('''
            -----------------------------------------------------------
            created on: 11/11/2020
            by: KIM SONG @CaptKrakenatic
            with Python3 using modules: random, sys, os, and pyperclip.
            -----------------------------------------------------------
            ''')
            func()
        elif ans == 'n':
            print('\nbye bye!')
            sys.exit()
        else:
            print('\n>>enter \'y\', \'n\', or \'a\' only.\n')
            func()

    # generate the password
    def gen(length):
        for n in range(1, length + 1):
            random.shuffle(char)
            pw.append(random.choice(char))
        # randomize the character location even more just for fun.
        random.shuffle(pw)
        endpw = ''

        for m in pw:
            endpw += m

        print('\nyour generated password is: ', endpw)
        pyperclip.copy(endpw)
        print('\n>>password copied.\n')


    try:
        print(spacer)
        al = int(input('password length: '))
        # set conditions
        if al < 8:
            al = 8
            print('\nIt\'s widely suggested that the minimum length of password is 8 characters.')
            gen(al)
        elif al > max:
            print('\nThe maximum length of password that I recommend is 256 characters.')
            print('I think that\'s plenty long, don\'t you?')
            ans = input(f'do you still want to generate a password with {al} characters? y/n: ')[:1].lower()
            if ans == 'y':
                gen(al)
            else:
                state = True
        else:

            gen(al)

    except:
        print('\n>>enter numbers only.\n')

    func()
