# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]

def list1(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]not in b:
            b.append(a[i])
        i+=1
    print(b)
list1([1,2,3,3,3,3,4,5])