print("->   To implement swich-case like characteristics very similar to if-else functionality, we use match case in python.")
print("->   A match statement will compare a given variable's value to different shapes also referred to as the pattern. The main idea is to keep on comparing the variable ")


x = int(input("input the value of x: "))
match x:
    case 2:
        print("The value of x is true")
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and the case is 4")
    case 15 if x % 3 == 0:
        print("value of x is 15 and 15 % 3 == 0")
    case 0:
        a = float(input("Enter first Number: "))
        b = float(input("Enter second Number: "))
        operation = input("What mathematical operation do you want perform. Enter any from (/, *, -, +): ")
        if operation == "/" :
            print(a/b)
        if operation == "*" :
            print(a*b)
        if operation == "-" :
            print(a-b)
        if operation == "+" :
            print(a+b)
    case _ if x / 3 == 9:
        print("value of x is 27")
    case _ if x - 10 > 15:
        print(" value of x is greter than 25")
    case _:
        print(x)