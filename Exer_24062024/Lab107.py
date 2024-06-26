# recursion


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("enter the value you want to print")
n = int(input())

print(factorial(n))
