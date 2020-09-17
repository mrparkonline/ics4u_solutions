# 09.16.2020
# Q1) Create a Python program that determines the most occurring number in a list.

'''Ideas:
Loop through the list
Count the occurance of each item
Store the maximum
'''

#testing_list = list('hello, world!')
testing_list = []
print(testing_list)

# how do we populate testing_list as user input
loop = True
while loop:
    current_item = int(input('Enter a value you want to add into the list: '))

    testing_list.append(current_item) # adding a value to the end
    # testing_list += [current_item]

    exit_status = input('do you want to stop inputting? (y/n): ')

    if exit_status in 'yY':
        loop = False
# end of input


#test2 = [1,2,2,3,3,3]

greatest_count = 0 # initialization
the_resulting_item = None # None is a special keyword for Nothing

for item in testing_list:
    #print(item, 'occurs', testing_list.count(item), 'times.')

    if testing_list.count(item) > greatest_count:
        greatest_count = testing_list.count(item)
        the_resulting_item = item
    elif testing_list.count(item) == greatest_count:
        if item != the_resulting_item:
            the_resulting_item = None
# end of for loop

print('The most occuring item:', the_resulting_item)
