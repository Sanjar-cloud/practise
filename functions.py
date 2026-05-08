
'''FUNCTIONS
(1)  DEFINE vs CALL
(2) Parameter vs Argument
(3) Keyword & default arguments
(4) Scope
'''


######### DEFINE parameter va  CALL argument #########

# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!

# DEFINE - parameter
def greet(a):
    print(f"How do you do, {a}")

def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

# CALL - argument
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


     ###### Keyword va default arguments ##########

# DEFINE
def give_greet(name, age):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

# CALL
result3 = give_greet(name="Justin", age=28)
print("result:", result3)

result4 = give_greet(name="Justin", age=28)
print("result4:", result4)



########## scope tushunchasi #############

b = 100 # 3.   ## agar faqat (a) ni ozini bersak b tashqaridan oladi
                                
# DEFINE
def calculate(a, b): # 2
    c = a * b # 1
    print(f"the c value: {c}")

# CALL
calculate(5, 50)
