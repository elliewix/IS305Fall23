import csv

# with open("pokemon_names_and_descriptions.csv", "r", encoding="utf-8") as infile:
#     csvin = csv.reader(infile)
#     # full style, which is just fine
#     # headers = next(csvin)
#     # data = [r for r in csvin] # data = list(csvin)
#     headers, *data = csvin


with open("pokemon_names_and_descriptions.csv", "r", encoding="utf-8") as infile:
    headers, *data = csv.reader(infile)

print(headers)
print(len(data))

# print(data[:10])

counted_letters = {}

for row in data:
    name = row[1].lower()
    # print(name)
    for char in name:
        if char in counted_letters:
            counted_letters[char] += 1
        else:
            counted_letters[char] = 1

print(counted_letters)

all_rows = []

for char, count in counted_letters.items():
    row = [char, count]
    all_rows.append(row)

out_headers = ["character", "count"]

with open("char_counts.csv", "w", encoding="utf-8", newline="") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(out_headers)
    csvout.writerows(all_rows)


# functions

def takealist(orig):
    # print(id(l))
    l = orig.copy()
    l[0] = "cats"
    return l

my_l = ['a','b']
takealist(my_l)
# print(id(my_l))
print(my_l)
print(takealist(my_l))