# sentence = "here is some text"
sentence = 'here is some   text'

empty = "" # ''

# print(len(sentence), len(empty))

# print("" == '')
#
# print(id("a"), id("a"))

# print([] == []) # should be true
# print([] is [])

import random
letters = ['c', 'd', 'a', 'z']
# mixedup = random.shuffle(letters) # a problem!
# newlist = letters # nope! can't do this
newlist = letters.copy() # letters[:]
random.shuffle(newlist)

# print("letters", letters)
# # print("mixedup", mixedup)
# print("newlist", newlist)
# print(id(letters), id(newlist))

#####
# get a list out of a string
print(sentence)
# print(sentence.split(" ")) #never!
print(sentence.split()) # yes!

words = sentence.lower().split()

print("Text".lower() in words)
#basic data cleaning, lower all sides to check

has_here = "Here".lower() in words
min_words_met = len(words) > 2

# print(has_here, min_words_met)

# if has_here and min_words_met:
#     print("Yes! it qualifies!")

#####

has_203 = False
has_205 = False

# take new class req both
# custom errors if you're missing one or both
if has_203 and has_205:
    print("Yes you can take the new class")
elif has_203 or has_205:
    # print("you're missing one!")
    if has_203:
        print("missing 205!")
    else:
        print("missing 203!")
else:
    print("missing both")

####

# working with lists

print(sentence)
print(len(sentence))
print(len(words))

print(words[0]) # indexing wil give you the object back
print(words[0:1]) # the : means I'm slicing
# slicing a list always gives you back a list

## list methods

### add stuff into a list

fresh = []

fresh.append("banana") # always adds at the end
print(fresh)
fresh.append("apple")
print(fresh)
fresh.insert(0, "pear")
print(fresh)

### change a value

fresh[1] = "bananas" # specify the index position

print(fresh)
# read more here: https://www.w3schools.com/python/python_ref_list.asp

nums = list(range(10))

for i, num in enumerate(nums):
    nums[i] *= 15

print(nums)

print([n* 15 for n in nums])

