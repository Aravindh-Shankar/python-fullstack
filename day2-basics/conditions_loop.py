# 1. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Check max of 3 numbers
a, b, c = 5, 7, 2
if a > b and a > c:
    print("A is biggest")
elif b > c:
    print("B is biggest")
else:
    print("C is biggest")

# 3. While loop countdown
x = 5
while x > 0:
    print("Countdown:", x)
    x -= 1

# 4. For loop - Print all numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 5. Break and Continue example
for i in range(1, 10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
