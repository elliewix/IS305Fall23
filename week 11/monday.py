

phrase = "here is some text and here is some more"

words = phrase.split()

letters = []
for w in words:
    w_letters = list(w)
    # print(w_letters)
    # letters.append(w_letters) # we don't want the whole list
    # letters += w_letters # you can concat
    # letters.extend(w_letters) # or extend

# same thing but as a comp
[letters.extend(list(w)) for w in phrase.split()]

# print(letters)
from collections import Counter

counted_letters = dict(Counter(letters)) # you'll want to recast it
# print(counted_letters)
counted_letters['name'] = "stuff" # adding a val into a dict
# print(counted_letters)

# for key, val in dict.items()

# for key, value in counted_letters.items():
#     print(key, value)

# empty_row = len(counted_letters) * [0]
headers = list(counted_letters.keys())
print(headers)
# print(empty_row)

my_word = dict(Counter("text"))

print(my_word)

empty_row = len(counted_letters) * [0]
for letter, count in my_word.items():
    # print(letter, count)
    # print(letter, headers.index(letter))
    empty_row[headers.index(letter)] = count
    # in your empty row, get access to the right
    # position, then set that value as count