# strip
# zfill

text = "   here is stuff      "

print(text.strip())
print(text.rstrip())
print(text.lstrip())

print("running".strip("gin"))

import string
print(string.punctuation)
print("___here.--  *))".strip(" "+ string.punctuation))

### zfill

print(str(10).zfill(4))
print(str(99999).zfill(4))

