from traceback import print_tb

x = lambda a, b : a * b
print(x(5,6))

x = lambda a, b, c : a * b + c
print(x(5,6,15))

def myfunction (n):
    return lambda a : a * n
mydoubler = myfunction(2)
print(mydoubler(10))

def myfunction2 (n):
    return lambda a : a * n
mytripler = myfunction2(3)
print(mytripler(10))