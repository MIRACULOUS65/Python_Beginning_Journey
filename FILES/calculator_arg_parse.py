import argparse

# reason to use argparse we can take input from command line

def main():
    parser = argparse.ArgumentParser(description="simple calculator")
    
    parser.add_argument("num1", type=float, help="first number")
    parser.add_argument("num2", type=float, help="second number")
    parser.add_argument("operation", choices=["add","sub","mul","div"], help="operation to perform")
    
    args = parser.parse_args()
    
    # Perform the calculation based on the operation
    if args.operation == "add":
        result = args.num1 + args.num2
        print(f"{args.num1} + {args.num2} = {result}")
    elif args.operation == "sub":
        result = args.num1 - args.num2
        print(f"{args.num1} - {args.num2} = {result}")
    elif args.operation == "mul":
        result = args.num1 * args.num2
        print(f"{args.num1} * {args.num2} = {result}")
    elif args.operation == "div":
        if args.num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = args.num1 / args.num2
            print(f"{args.num1} / {args.num2} = {result}")

if __name__ == "__main__":
    main()
