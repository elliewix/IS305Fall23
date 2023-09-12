text1 = "here is some text for you"
text2 = "one two three four five six"

words1 = text1.split()
words2 = text2.split()

print(words1)
print(words2)

# hmm, don't want the cross product
for word_i in words1:
    for word_j in words2:
        print(word_i, word_j)

# what about looping separately?

for word_i in words1:
    print(word_i)

for word_j in words2:
    print(word_i, word_j)

# hmm nope.....

print()
print()
# let's work with index positions

print(words1[0], words2[0])
print(words1[1], words2[1])

# mutual index pattern
for i in range(len(words1)):
    print(i, words1[i], words2[i])

# functional style

print(list(zip(words1, words2)))

