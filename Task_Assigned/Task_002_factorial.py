import math

n= 5
factorial = 1

result = math.factorial(n)
print(result, "\n")

for i in range(1,n+1):
    factorial = factorial * i


print(factorial , "\n")

while n > 0:
    factorial *= n
