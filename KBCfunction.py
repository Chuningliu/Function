# 5050 LIFELINE



def function():
    question_list = ["How many continents are there?",
                 "What is the capital of India?",
                 "NG mei kaun se course padhaya jaata hai?"]

    options_list = [["Four", "Nine", "Seven", "Eight"],
                ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
                ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
    solution_list = [3, 4, 1]
    lifeline5050=[["nine","seven"],["Chennai","Delhi"],["Software Engineering","Tourism"]]
    lifeans=[2,2,1]
    i=0
    j=0
    while i<len(question_list[i]) and j<len(options_list):
        print(j+1,question_list[i])
        k=0
        while k<(len(options_list)+1):
            print(k+1,options_list[j][k])
            k+=1
        lifeline=(input("Want 5050 lifeline?Enter Yes or No:"))
        if lifeline=="Yes":
            count=0
            if count==0:
                l=0
                while l<len(lifeline5050[i]):
                    print(l+1,lifeline5050[i][l])
                    l+=1
                count+=1
                sol1=int(input("Enter your answer:"))
                if sol1==lifeans[i]:
                    print("Congrates!Your answer is right!")
                else:
                    print("Your answer is wrong! ")
                    break
            else:
                print("Your lifeline has been used.")
                sol=int(input("Enter the answer"))
                if sol==solution[i]:
                    print("Congratulations!! Your answer is right")
                else:
                    print("Better luck next time")
                break
        elif lifeline=="No":
            sol=int(input("Enter the answer:"))
            if sol==solution_list[i]:
                print("Congratulation! Your answer is right")
            else:
                print("Better luck next time")
                break
    print()
    i+=1
    j+=1
function()