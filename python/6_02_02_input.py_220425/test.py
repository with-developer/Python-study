import random

max_num = -1
for i in range (0, 100) :
    random_num = random.randrange(0, 1000)
    if random_num > max_num :
        max_num = random_num

print("가장 큰 수는 : ", max_num)

min_num = 1000
for i in range (0, 100) :
    random_num = random.randrange(0, 1000)
    if min_num > random_num :
        min_num = random_num

