# 1. Lists
fruits = ["apple", "banana", "mango"]
fruits.append("grape")
fruits.remove("banana")
print(fruits)

# 2. Tuples
point = (10, 20)
print(f"X: {point[0]}, Y: {point[1]}")

# 3. Sets
numbers = {1, 2, 3, 3, 2}
print(numbers)  # Output: {1, 2, 3}

# 4. Dictionary
student = {
    "name": "Aravindh",
    "age": 23,
    "skills": ["Python", "React"]
}
print(student["name"])
student["age"] = 24
student["email"] = "aravindh@email.com"
