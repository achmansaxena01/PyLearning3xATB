# try , except and finally
try:
    # code
    a = int(input("Enter the num 1 \n"))
    b = int(input("Enter the num 2 \n"))
    c = a / b
except ValueError as ve:
    print(ve)
    print("Please enter integer!")
except ZeroDivisionError as zde:
    print(zde)
    print("Cannot divide by 0 !")
else:
    print("executing else")
    print("Result Div is ", c)
finally:
    print("I will be executed anyhow !!")

