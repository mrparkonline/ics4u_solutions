# 09/14/2020
# Tutorial Session 1

# Q1) Waterloo Office Problem
'''
Check if the office is open!
- Opens at 8:00
- Closes at 17:30 (5:30pm)
'''

# import secondFile

'''
- Two inputs: Hour and Minute
- Conditional Statements (if and stuff)
- Comparison operators
- Algorithm
- Documentation / Commenting
- Numeric representation of time ex: 830/1730
'''

# office opens at 8
# closes at 5:30 pm (17:30)

def officeHour1(hour, minute):
    '''
    officeHour1() checks if the waterloo office is open or not

    arguments
    -- hour : integer
    -- minute : integer

    return
    -- Boolean : True if the office is open
    '''

    if hour < 8 or hour > 17:
        return False # office closed
    else:
        # hour >= 8 and hour <= 17
        if hour == 17:
            if minute >= 30:
                return False
            else:
                return True
        else:
            return True
# end of officeHour1

def officeHour2(hour, minute):
    ''' officeHour2 will conver hour and minutes into a large integer to do comparisons.'''

    if minute < 10:
        minute = '0' + str(minute)

    numeric_representation = int(str(hour)+str(minute))

    if numeric_representation >= 800 and numeric_representation < 1730:
        return True
    else:
        return False

# end of officeHour2
def hourInput(prompt):
    ''' hourInput() to help us make sure that hour inputted is from 0 to 24 inclusively

    argument
    -- prompt : string (message for the user)

    return
    -- integer : proper hour value
    '''

    hour = int(input(prompt))

    while hour < 0 or hour > 24:
        print('invalid hour input.')
        hour = int(input(prompt))
    # end of while

    return hour
# end of hourInput()

def minuteInput(prompt):

    minute = int(input(prompt))

    while minute < 0 or minute > 59:
        print('invalid minute input.')
        minute = int(input(prompt))
    # end of while

    return minute
# end of minuteInput()

hour = hourInput('Enter the current hour in 24H system: ')
minute = minuteInput('Enter the current minute: ')

print('Is the office open at:', hour, minute)
print(officeHour2(hour, minute))
