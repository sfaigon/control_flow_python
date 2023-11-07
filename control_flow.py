# exercise-01 Vowel or Consonant


vowel = "aeiou"
letter = input("Please enter a letter from the alphabet (a-z or A-Z): ").lower()
if letter in vowel:
  print(f"{letter} is a vowel")
elif letter == "y":
    print(f"{letter} is sometimes a vowel")
else:
  print(f"{letter} is a consonant")




# exercise-02 Length of Phrase

word = ""
while word != "quit":
    word = input("Please enter a word or phrase: ")
    if word != "quit":
        print(f"What you entered is {len(word)} characters long")




# exercise-03 Calculate Dog Years



age = int(input("Input a dog's age: "))
sum = 0
for i in range(age):
    if i<2:
        sum += 10
    else:
        sum += 7
print(f"The dog's age in dog years is {sum}")






# exercise-04 What kind of Triangle?


print(" Enter the lengths of three side of a triangle:")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a == b and b == c:
    triangle = "equilateral"
elif a == b or b == c or a == c:
    triangle = "isosceles"
else:
    triangle = "scalene"
print(f"A triangle with side {a}, {b}, and {c} is a {triangle} triangle")





# exercise-05 Fibonacci sequence for first 50 terms

num = 0
sum = 1
print("Term: 0 / number: 0")
print("Term: 1 / number: 1")
for i in range(2,50):
    holder = sum
    sum = sum + num
    num = holder
    print(f"Term: {i} / number: {sum}")
    




# exercise-06 What's the Season?




mm = input("Enter the month of the year (Jan - Dec):").lower()
dd = int(input("Enter the day of the month:"))
season = None
if mm == "dec":
    if dd > 20:
        season = "Winter"
    else:
        season = "Fall"
elif mm in ("jan", "feb"):
    season = "Winter"
elif mm == "mar":
    if dd > 19:
        season = "Spring"
    else:
        season = "Winter"
elif mm in ("apr", "may"):
    season = "Spring"
elif mm == "jun":
    if dd > 20:
        season = "Summer"
    else:
        season = "Spring"
elif mm in ("jul", "aug"):
    season = "Summer"
elif mm == "sep":
    if dd > 21:
        season = "Fall"
    else:
        season = "Summer"

if season != None:
    print(f"{mm} {dd} is in {season}")
else:
    print("Date format entered in incorrect")
