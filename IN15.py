# 15. Write a Python program that accepts a hyphen-separated sequence of words as input 
# and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white

def sequence(name):
    
        name.sort()
        print(name)
sequence("green""-red""-yellow""-black""-white")