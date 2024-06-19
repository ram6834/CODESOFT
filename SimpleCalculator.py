def Calculator() :
    print()

    print("List of Operations - ")

    print()

    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modular Division")

    print()

   
    user_choice=input("choose operation (1/2/3/4/5) : ")   

    if user_choice not in ['1','2','3','4','5'] :
        print("Invalid operation. Please try again!!")
        return

    try:
        a= int(input("enter first number : "))
        b= int(input("enter second number : "))
    except ValueError :
        print("Invalid input. Enter numeric values")
        return
        

    if user_choice=='1':
        print(f"The addition between {a} and {b} is {a+b}")

    if user_choice=='2':
        print(f"The Subtraction between {a} and {b} is {a-b}")

    if user_choice=='3':
        print(f"The Multiplication between {a} and {b} is {a*b}")

    if user_choice=='4':
        try:
            c=a/b
            print(f"The Division between {a} and {b} is {c}")
        except ZeroDivisionError:
            print("Invalid input. The Denominator should not be zero")

    if user_choice=='5':
        print(f"The Modular Division between {a} and {b} is {a%b}")  

Calculator()