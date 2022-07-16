# Local scope:

# a = 10
# def function():
#   print("Hello")
#   b = 20
# function()
# print(a)
# print(b)

# Global scope

# msg = "Global Variable"
# def function():
#   # local scope of function
#   msg ="Local Variable"
#   print(msg)
# function()
# print(msg)

# Enclosing scope:
# def vehicle():
#   fun ="Start"
#   def car():
#     model= "Toyato"
#     print(fun)
#     print(model)
#   car()
# vehicle()

# Built-in scope:
# a = 5.5
# int(a)
# print(a)
# print(type(a))

# Global Keyword:
# a = 100
# def method():
#   a = 50
#   print(a)
# method()
# print(a)


# a = 100
# def method():
#   global a
#   a = 50
#   print(a)
# method()
# print(a)

# Non-local keyword:
# a = "global variable"
# def method():
#         a = "nonlocal variable"
#         def function():
#                 a = "local variable"
#                 print(a)
#         function()
#         print(a)
# method()
# print(a)

# a = "global variable"
# def method():
#         a = "nonlocal variable"
#         def function():
#                 nonlocal a
#                 a = "local variable"
#                 print(a)
#         function()
#         print(a)
# method()
# print(a)
