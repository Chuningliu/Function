# 13. Write a Python function that prints out the first n rows of Pascal triangle.


def pascal(n):
   a=[1]
   b=[0]
   i=0
   while i<n:
      print(a)
      a=[l+r for l,r in zip(a+b,b+a)]
      i+=1
   return n>=1
pascal(6)
