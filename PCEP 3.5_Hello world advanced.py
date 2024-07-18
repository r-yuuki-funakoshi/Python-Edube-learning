import string
string.ascii_lowercase
list(string.ascii_lowercase)
print(list(string.ascii_lowercase))

i=0
for i in range(len(list(string.ascii_lowercase))):
    print(list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("h"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("h",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("e"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("he",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("l"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hel",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("l"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hell",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("o"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hello ",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("w"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hello w",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("o"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hello wo",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("r"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hello wor",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("l"):
        break
for i in range(len(list(string.ascii_lowercase))):
    print("hello worl",list(string.ascii_lowercase)[i])
    if i==list(string.ascii_lowercase).index("d"):
        break
print("hello world")
