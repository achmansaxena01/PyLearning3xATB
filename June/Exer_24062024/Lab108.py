def sum_of_digits(r):
    if r < 10:
        return r
    else:
        return r % 10 + sum_of_digits(r // 10)


n = 123456
sum1 = sum_of_digits(n)
print(sum1)
