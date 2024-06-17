import math

n = 5
factorial = 1

result = math.factorial(n)
print("result using math is : ", result)

for i in range(1, n + 1):
    factorial = factorial * i

print("result using factorial in range is : ", factorial)
factorial1 = 1
while n > 0:
    factorial1 *= n
    n = n - 1

print("result using while loop is : ", factorial1)
