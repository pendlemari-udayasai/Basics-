#-----------------
#DECORATORS
#-----------------
#A decorator is a function that allows us to modify or extend the behavior of another function without changing its original code.
#Decorators use the @ symbol and are applied before the function definition.
#They are commonly used for logging, authentication, validation, and measuring execution time.
#Decorators help make code more reusable, flexible, and organized.

## ==========================
# DECORATORS IN PYTHON
# ==========================
# Example 1: Basic Decorator
def decorator_function(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper
@decorator_function
def greet():
    print("Hello, Python!")
greet()

# Example 2: Decorator with Function Arguments
def welcome_decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
    return wrapper
@welcome_decorator
def greet_user(name):
    print("Hello", name)
greet_user("UDAY")

# Example 3: Decorator for Login Check
def login_required(func):
    def wrapper():
        print("User is logged in")
        func()
    return wrapper
@login_required
def dashboard():
    print("Welcome to the Dashboard")
dashboard()

# Example 4: Decorator for Execution Message
def message_decorator(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution completed")
    return wrapper
@message_decorator
def display():
    print("Learning Python Decorators")
display()

#----PROBLEMS-----
#1st one
def decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper
@decorator
def greet():
    print("hello")
greet()

#2nd one
def decorator(func):
    def wrapper(name):
        print("starting...")
        func(name)
        print("done")
    return wrapper
@decorator
def greet(name):
    print("hello",name)
greet("ravi")
#3rd one

def decorator(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result*2
    return wrapper
@decorator
def multiply():
    return 25
print(multiply())

#4th one
user_role="student"
def decorator(func):
    def wrapper():
        if user_role!="admin":
            print("Access denied")
        else:
            func()
    return wrapper
@decorator
def delete_data():
    print("data deleted")
delete_data()

#5th one
def decorator(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper
@decorator
def get_msg():
    return "hello world"
print(get_msg())

#6th one
def decorator(func):
    count=0
    def wrapper():
        nonlocal count
        count+=1
        print("called",count,"times")
        func()
    return wrapper
@decorator
def hello():
    print("hello")
#how many we call,it called that much times
hello()
hello()
hello()

#7th one

def decorator(func):
    def wrapper():
        result=func()
        return "ID:"+result
    return wrapper
@decorator
def get_name():
    return "ravi"
print(get_name())

#8th one
def initializing(func):
    def wrapper():
        print("initializing")
        func()
        print("cleanup completed")
    return wrapper
@initializing
def task():
    print("function logic runs")
task()

#9th one
def negative_result(func):
    def wrapper(a,b):
        result=func(a,b)
        if result<0:
            return 0
        else:
            return result
    return wrapper
@negative_result
def subtract(a,b):
    return a-b
print(subtract(5,3))

#10th onw

def type_validator(func):
    def wrapper(arg):
        if not isinstance(arg,str):
            print("Error:invalid input type")
        else:
            return func(arg)
    return wrapper
@type_validator
def show_message(text):
    print("message:",text)
show_message("hello")
show_message(123)