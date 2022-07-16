# Define a function which takes two arguments(strings) and
# returns the string with largest length. If both the strings have equal length,
# print both the strings one below the other.
# Hint :- use len() builtin function..


def function_name():
    n=input("Enter any string:")
    n1=input("Enter the string:")
    a=len(n)
    b=len(n1)
    if a>b:
        print(n)
    elif b>a:
        print(n1)
    else:
        print(n)
        print(n1)
function_name()
        
    
    