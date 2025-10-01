try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("what kind of operation you want to perform . press + for addition \n press - for substraction \n press / for division \n press * for multiplication")

    o=input("enter the operations : ")
    match o:
        case "+":
            print(f"the result is : {a+b}")
        case "-":
            print(f"the result is : {a-b}")
        case "/":
            print(f"the result is : {a/b}")
        case "*":
            print(f"the result is : {a*b}")
        case default:
            print("enter a valid operation")

except Exception as e:
    print("enter a valid value for a and b")