type(3) # <class 'int'>
type('two') # <class 'str'>
type(3.0) # <class 'float'>
len('hi') # length = 2

def greet():
    print('Aloha')

greet() # 'Aloha'
greet # function greet at 0x1065785 (direction)

def double(x):
    return x * 2

double(3) # 6
