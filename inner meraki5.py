# Define a function which takes one parameter(positive integer). 
# This function returns the sum of all multiples of 3 and 5 (not 
# neccessary common multiples) in the range 1 to the integer passed as the parameter.

# def function_name():
#     n=10
#     i=1
#     while i<=n:
#         if i%3==0:
#             print(i,"divisible by 3")
#         elif i%5==0:
#             print(i,"divisible by 5")
#         i+=1
# function_name()
def function_name(n):
    i=1
    while i<=n:
        if i%3==0:
            print(i,"divisible by 3")
        elif i%5==0:
            print(i,"divisible by 5")
        i+=1
# n=int(input("Enter numbers:-"))
function_name(14)