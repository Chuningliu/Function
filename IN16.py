# 16. Write a Python function to create and 
# print a list where the values are square of numbers between 1 and 30 (both included).
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
