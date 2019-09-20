#! /usr/bin/env python3

# this is a single line comment

'''
    this 
    is 
    a 
    multiple 
    lines 
    comment
'''

# Creating Variables
# https://www.w3schools.com/python/python_variables.asp
def hello():
    greeting = "Hi! Welcome to Python Programming 101" #this is a in line comment
    print(greeting)
    print("this is a double quote string")
    print('this is a single quote string')
    x = 'this is a variable holding a string'
    print(x)

# Python Data Types
# https://www.w3schools.com/python/python_datatypes.asp
def datatypes():
    x = "Hello World" #str
    print(x)

    x = 20 #int
    print(x)

    x = 20.5 #float
    print(x)

    x = 1j #complex
    print(x)

    x = ["apple", "banana", "cherry"] #list
    print(x)

    x = ("apple", "banana", "cherry") #tuple
    print(x)

    x = range(7) #range
    print(x)

    x = {"name" : "John", "age" : 36} #dict	
    print(x)

    x = {"apple", "banana", "cherry"} #set
    print(x)	
    
    x = frozenset({"apple", "banana", "cherry"}) #frozenset
    print(x)	
    
    x = True #bool
    print(x)	
    
    x = b"Hello" #bytes
    print(x)

# Python Arithmetic Operators (Operadores Aritméticos)
# https://www.w3schools.com/python/python_operators.asp
def arithmetic(a, b):    
    result = a + b
    print('a + b =', result)

    result = a - b
    print('a - b =', result)

    result = a * b
    print('a * b =', result)

    result = a / b
    print('a / b =', result)

    result = a % b
    print('a % b =', result)

    result = a ** b
    print('a ** b =', result)

    result = a // b
    print('a // b =', result)

# Python Assignment Operators
# https://www.w3schools.com/python/python_operators.asp
def assignment():
    x = 5
    print('x ==', x)

    x += 3
    print('x += 3 ==', x)

    x -= 2
    print('x -= 2 ==', x)

    x *= 2
    print('x *= 2 ==', x)

    x /= 2
    print('x /= 2 ==', x)

    x %= 2
    print('x %= 2 ==', x)

    x = -10
    x //= 3
    print('-10 //= 3 ==', x)

    x **= 2
    print('x **= 2 ==', x)

# Python Comparison Operators (Operadores Relacionais)
# https://www.w3schools.com/python/python_operators.asp
def comparison():
    x, y = 3, 5
    print('x == y', x == y)

    x, y = 3, 5
    print('x != y', x != y)

    x, y = 3, 5
    print('x < y', x < y)

    x, y = 3, 5
    print('x > y', x > y)

    x, y = 3, 3
    print('x >= y', x >= y)

    x, y = 5, 5
    print('x <= y', x <= y)

# Python Logical Operators (Operadores Lógicos)
# https://www.w3schools.com/python/python_operators.asp
def logical():
    print(3 < 5 and 5 > 3)
    print(3 < 5 or 5 == 3)
    print(5 == 3 or 3 < 5)
    print(not 3 == 3)

# Python Identity Operators
# https://www.w3schools.com/python/python_operators.asp
def identity():
    x = ''
    y = 'b'
    print(x is y)
    print(x is not y)

# Python Membership Operators
# https://www.w3schools.com/python/python_operators.asp
def membership():
    print('y' in 'yes')
    print('y' in 'no')
    print('y' not in 'no')

# Python Conditions and If statements (Conditions Statements / Estruturas de Decisão)
# https://www.w3schools.com/python/python_conditions.asp
def conditional():
    # if
    a, b = 33, 200
    if b > a:
        print("b is greater than a")

    # elif
    a, b = 33, 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    
    # else
    a, b = 200, 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    # short hand If
    a, b = 200, 33
    if a > b: print("a is greater than b")

    # short hand If ... Else
    a, b = 2, 330
    print("A") if a > b else print("B")

    # and
    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are True")

    # or
    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("At least one of the conditions is True")

    # nested if
    x = 41
    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

# Python Loops (Repetion Statements / Loop Statements / Loops / Estruturas de Repetição)
# https://www.w3schools.com/python/python_while_loops.asp

# Python Functions
# https://www.w3schools.com/python/python_functions.asp

