


text1 = "01 02 \t03      04"
text2 = "dog;cat;fish;snake"

ids = text1.split()
# ids = text1.split(" ") # never use
animals = text2.split(";")

print(ids, animals)

for i in range(len(ids)):
    # print(ids[i], animals[i])
    person = ids[i]
    pet = animals[i]
    print(person, pet)

print(list(zip(ids, animals)))
# print(list(zip(animals, ids)))

# print(list(zip(range(10), range(5))))

# for something in zip(ids, animals):
#     print(something)

for pair in zip(ids, animals):
    # print(pair)
    person = pair[0]
    pet = pair[1]
    # print(person, pet)

for person, pet in zip(ids, animals):
    print(person, pet)

