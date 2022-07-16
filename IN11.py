# 11. Write a Python function to check whether a number is perfect or not. 


# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))
 
def perfect(n):
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print("It is the perfect number")
    else:
        print("It is not a perfect number")
perfect(6)
            

# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if i%2==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(c)
# print(b)
    
        
    

        


