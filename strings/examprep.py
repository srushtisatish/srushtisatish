name=input("enter a string:")
rev=""
new=""
for ch in name[::-1]:
    rev+=ch
for i in range(len(rev)):
    if i%2==0:
        new+=rev[i].upper()
    else:
        new+=rev[i]
print(new)
