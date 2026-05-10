# OBJECTS
# (1) What is object
# (2) Iterable objects & RANGE
# (3) DICTIONARY
# (4) Error handling system

import array        # package/module
import math         # package
from math import ceil

print("==== What is object =====")

# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polymorphism

result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)


print("====    Iterable objects va  range ===")
# Iterable objects > string dict tuple list range map filter

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "mit":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

print("====     dictionary ===")
# dictionary is JSON object

person     = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name = person_obj["name"]
name    = person_obj.get("name")
hobby   = person_obj.get("hobby")
balance = person_obj.get("balance", 0)

print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]

for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)}")



print("=== Error handling system =====")

# type errors => KeyError, AttributeError, Exception

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("General Error:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")


