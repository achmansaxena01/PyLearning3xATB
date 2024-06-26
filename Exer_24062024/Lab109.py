def sum_of_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit = sum_digit + n % 10
        n = n // 10
    return sum_digit


print(sum_of_digit(12345))
