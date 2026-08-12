num = input("Please enter a number: ")

try:
    num = int(num)
except:
    print("Please enter a number. Exiting.")
    exit()

if num > 10:
    print("Big number")
else:
    print("Small number")


passw = input("\nPlease enter your password: ")
if passw == "python":
    print("Access granted")
else:
    print("Access denied")



test = input("\nPlease enter test score: ")
try:
    test = int(test)
except:
    print("Please enter a number. Exiting.")
    exit()

if test >= 50:
    print("Pass")
elif test >= 40:
    print("Supplementary")
else:
    print("Fail\n")




for i in range(1, 6):
    print(i)

print()

for i in range(1, 6):
    if (i % 2 == 0):
        print(i)
    else:
        continue


print()
i = 0
while i <= 0:
    i = int(input("Please enter a number: "))

print("\nDone")





l = input("\nPlease type a letter: ")
if l in ("aeiou"):
    print("That is a vowel")
else:
    print("That is not a vowel")




print()
for i in range(1, 21):
    if (i % 5 == 0):
        continue
    else:
        print(i)


print()
v = 5
while v > 0:
    print(v)
    v -= 1

print("\nDone")
