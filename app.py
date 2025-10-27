from calculator import add

if __name__ == "__main__":
    print("Welcome to Calculator App")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"The sum is: {add(x, y)}")

