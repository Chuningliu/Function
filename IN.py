# 1. Write a Python function to find the Max of three numbers.
def threemax():
    a=[14,19,23]
    i=0
    while i<len(a):
        b=max(a)
        i+=1
    print(b)
threemax()