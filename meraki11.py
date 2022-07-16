# Create a function named Calculator which takes three arguments - number_x, number_y,
# operation. number_x and number_y  we will take two integers and 
# operation parameter defines the type of mathematical operation to be 
# performed on the two integers.

# def calculator():
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3. Multiplication")
#     print("4.Division")
#     Choice=input("Enter your choice:")
#     num1=int(input("Enter number 1:"))
#     num2=int(input("Enter number 2:"))
#     if Choice=="1":
#         print(num1,"+",num2,"=",(num1+num2))
#     elif Choice=="2":
#         print(num1,"-",num2,"=",(num1-num2))
#     elif Choice=="3":
#         print(num1,"*",num2,"=",(num1*num2))
#     elif Choice=="4":
#         if num2==0.0:
#             print("Divide by 0, error")
#         else:
#             print(num1,"/",num2,"=",(num1/num2))
#     else:
#         print("Invalid choice")
# calculator()







# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):

#     return x * y

# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
    
#     else:
#         print("Invalid Input")

