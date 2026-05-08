# Dunder __builtins__, __init__

message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTIONS > print() len() input() type() str() int()
(3) CONSTANTS > True False None
'''

print(dir(__builtins__))


# ////////////
print("===== number =======")

# in JAVA, variable is a name storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator    # state
print(result1, result2)


# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

curse = course.replace("FullStack", "")
print(f"the result (4): {curse}")
print(course)


# //////////
print("======= boolean =========")

# functions > type() input() bool() int() str()

y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY: True 100 -100 "MIT"
# FALSY: False 0 '' None

test_falsy = "" or False or None or 0
print("test_falsy:", bool(test_falsy))

test_truthy = "mit"
print("test_truthy:", bool(test_truthy))