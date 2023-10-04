

# while (something to check)
# while (boolean expression that equals true...):
#   do this stuff

count = 0

while count < 10:
    count += 1
    # print(count)

count = 0
while not count == 10:
    count += 1
    # print(count)

count = 0

while True:
    if count > 10:
        break
    else:
        count += 1
    # print(count)

####
import random
random.seed(8)

# defined num of rolls

sides = 10
total = 0
num_rolls = 10000
for _ in range(num_rolls):
    roll = random.randint(1,sides)
    total += roll
# print(total / num_rolls)

# indefinite num
random.seed(50)

sides = 6
total = 0
rolls = 0

# while total < 20:
#     roll = random.randint(1, 6)
#     total += roll
#     rolls += 1
#     # allows it to go over

#
# while True:
#     roll = random.randint(1,6)
#     if total + roll > 20:
#         break
#     else:
#         total += roll
#         rolls += 1
#
# print(total, rolls)

all_results = []
for _ in range(100):
    while True:
        roll = random.randint(1,6)
        if total + roll > 20:
            break
        else:
            total += roll
            rolls += 1
    results = (total, rolls)
    # results = {'total': total, 'rolls': rolls}
    all_results.append(results)

# print(all_results)
from collections import Counter
# print(all_results)


# print(Counter(all_results))

print(list(enumerate("ischool")))

a = "horse"
b = "snake"

# print(list(zip(a,b)))

for i, letter in enumerate(a):
    # print(letter, b[i])
    if i == 0:
        print("starting!")
    elif i == len(a) - 1:
        print("ending!")
    print(letter)