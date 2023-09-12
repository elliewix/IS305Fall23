


def take_two(word_a, word_b):
    assert len(word_a) > 0 and len(word_b) > 0
    new_string = ""
    new_string += word_a.title()
    new_string += " ; "
    new_string += word_b.upper()
    # print(word_a, word_b, new_string)
    return new_string

def dostuff():
    result = ""


    return result

print(take_two("one", "two"))
result = take_two("three", "four")
print(result)
print(take_two("", "five"))




print("hello")
text = "here is some text"
words =  text.split()
words2 = ""

# assert len(words) > 0, "words should not have been empty"
# assert len(words2) > 0
assert len(words) < 5, "expected len of words to be less than 5, got " + str(len(words))

print(words)
print(words2)