# 1. Greet function
def greet(name):
    print(f"Hi {name}!")

greet("Aravindh")

# 2. Sum function
def add(a, b):
    return a + b

print("Sum:", add(3, 5))

# 3. Check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))

# 4. Exception example
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Can't divide by zero!")
