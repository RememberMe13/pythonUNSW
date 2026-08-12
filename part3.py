import random

def square(n):
    return n * n

print(square(5))



print()
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Henry")
greet("Joe", "Yo")
greet("Bob", greeting="Gday")



print()
def ticket_price(age):
    if age < 5:
        return 0
    elif age <= 17:
        return 8
    elif age <= 64:
        return 12
    else:
        return 6

    # Uses return instead of print so result can be further modified
print("Price:", ticket_price(15))




def noLook():
    secret = 42
    return secret

print(noLook())




print()
l = ["Milk", "Bread", "Lettuce"]
l.append("Clams")
l.remove("Bread")

print(l, "Length: ", len(l))

for i, n in enumerate(l):
    print(i, n)




print()
d = {"Alex": 16, "Sam": 18}
print("Alex:", d.get("Alex"))



print()
def roll():
    return random.randint(1, 6)

for i in range(3):
    print(roll())



color = ["red", "green", "red", "blue", "green"]
sCol = set(color)
print(sCol)
print(f"Number of items in set: {len(sCol)}")
