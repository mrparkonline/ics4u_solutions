# 20 Questions

print('Welcome to 20 Questions.')
print('Elon Musk will guess the natural number you are thinking of ...')
print('Please think of a number between 1 to 100 inclusively.')
print('------------')

low = 1
upper = 100
loop = True # this helps iterate
q_counter = 0 # this limits the number of questions

while loop and q_counter < 20:
    middle = (low + upper) // 2

    print('Is', middle, 'your number?')
    user_input = input('Y or N?: ')
    q_counter += 1

    if user_input in 'Nn':
        # we guessed wrong
        print('Is your number higher or lower than', middle,'?')
        user_input = input('H or L?: ')
        q_counter += 1

        if user_input in 'Hh':
            low = middle + 1
        else:
            upper = middle
    else:
        # we are correct!
        loop = False
        print('Program finished')
        print('It took', q_counter, 'tries.')
    # end of 1st condition
# end of while loop.
