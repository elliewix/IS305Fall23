# numbers = list(range(100, 135))
#
# numbers.insert(10, 999)
#
# chunk = [] # this one will collect max 3 nums
# all_chunks = [] # will collect all those trio chunks
#
# for i, num in enumerate(numbers):
#     chunk.append(num)
#     if len(chunk) == 3:
#         all_chunks.append(chunk)
#         chunk = []
#     elif (i + 1) == len(numbers): # check if last index position
#         all_chunks.append(chunk)
#
# print("this is the chunk", chunk)
# print("this is all chunks", all_chunks)
#
#
numbers = list(range(100, 135))

numbers.insert(10, 999)
numbers.insert(15, 999)

chunk = [] # this one will collect max 3 nums
all_chunks = [] # will collect all those trio chunks

for i, num in enumerate(numbers):
    # chunk.append(num)
    if num == 999:
        all_chunks.append(chunk)
        chunk = []
    elif (i + 1) == len(numbers): # check if last index position
        chunk.append(num)
        all_chunks.append(chunk)
    else:
        chunk.append(num)

print("this is the chunk", chunk)
print("this is all chunks", all_chunks)


