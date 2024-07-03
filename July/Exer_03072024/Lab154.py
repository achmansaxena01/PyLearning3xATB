try:
    # code
    a = int(input("Enter the num 1"))
    b = int(input("Enter the num 2"))
    c = a / b
    print("Result Div is ", c)
except Exception as e:
    print(e)
    print("Please enter integer!")

# Errors are something , difficult to recover.


# Exceptions (Error) -> can be handled
