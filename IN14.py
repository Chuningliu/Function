# 14. Write a Python function to check whether a string is a pangram or not.
#  Pangrams are words or sentences containing every letter of the alphabet at least once.

def pangram(name,alphabet=string.ascii_lowercase):
    i=name
    a=[]
    a.append(name)
    if name[i] in name:
        print("It is a pangram")
    else:
        print("It is not a Pangram")
        i+=1
pangram(" The quick brown fox jumps over the lazy dog")

# def ispangram(str1, ):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
 
# print ( ispangram()) 
