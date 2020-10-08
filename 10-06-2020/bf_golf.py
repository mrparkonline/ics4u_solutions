# Brute Force GolF Solution
# Golf Problem

# Step 1: Handling Inputs from CCC nicely

total_distance = int(input())
num_clubs = int(input())
clubs = [int(input()) for x in range(num_clubs)]

# print('Our clubs:', clubs)

# Step 2: How should we solve this problem?

# check the sum of the clubs to see if it is less than the distance
# sum_clubs = sum(clubs)

possible_distance = [None for x in range(0,total_distance+1)]
for club_distance in clubs:
    possible_distance[club_distance] = 1

print(possible_distance)
input()

start_distance = min(clubs) # minimum of my clubs

while start_distance <= total_distance:
    if possible_distance[start_distance]: # it isn't none
        for club_distance in clubs:
            new_distance = start_distance + club_distance

            if new_distance <= total_distance:
                if possible_distance[new_distance]: # it isn't None
                    possible_distance[new_distance] = min(possible_distance[new_distance], possible_distance[start_distance]+1)
                else:
                    # the new distance has never been travelled before
                    possible_distance[new_distance] = possible_distance[start_distance]+1

    start_distance += 1
    print('----')
    print(possible_distance)
    print('----')
    #input()

print(possible_distance)
