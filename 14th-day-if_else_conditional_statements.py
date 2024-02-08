print("->   Sometimes programmer needs to check the evaluation of certain expression(s) wheather the expression evaluate to True or false, If the expression evaluates to false\n Then the program execution follows a different path then it would have if the expression had evaluated to true")
print("->   Based on this, conditional statements are classified into the following types\nif\nif-else\nif-else-elif\nnested if-else-elif")
print("->   Conditional operators\n>\n<\n>=\n<=\n==")
print("""         print(a>4)-
         print(a<4)
         print(a>=4)
         print(a<=4)
         print(a==4)""")
a=int(input("How many years of experience you have in DEVOPS: "))
print(a>4)
print(a<4)
print(a>=4)
print(a<=4)
print(a==4)
print("""
            if(a>3):
                print("you can work in our org")
            else:
                print("You cannot work in our org")""")
print("### the spaces before the print statement after the if condition is called indendation")

a=int(input("How many years of experience you have in DEVOPS: "))
if(a>3):
    print("you can work in our org")
else:
    print("You cannot work in our org")

print("->    Nested Elif statements")
print("      ----------------------")

laptop = 20000
brand = input("Enter Laptop Brand name: ")
print(brand)
if (brand == "dell"):
    budget = int(input("What is the budget for the laptop: "))
    print("your budget is", budget)
    if(budget > 20000):
            show_models = input("Do you want to see models: ")
            if(show_models == "yes"):
                print("Please bear with me I will give you the list of Dell laptop models")
                print(''' We have folowing models for DELL
                latitude
                inspiron
                alienware''')
            else:
                print("Ok have a good day")
    else:
        print("Please choose different laptop brand for this budget")
else:
    print("you can go with other other laptop brands")

