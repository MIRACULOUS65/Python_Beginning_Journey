a = int(input("Please enter a number: "))  # Ensure input is converted to int

match a:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case _:
        print("You entered something else.")
print("This is the end of the program.")