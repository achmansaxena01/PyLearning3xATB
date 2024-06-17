# *args - any number of arguments
# print("Pramod", "Amit", "SB")


def sum_three(a=1, b=1, c=1):
    return a + b + c


r1 = sum_three()
r2 = sum_three(a: 1,b: 2)
r3 = sum_three(a:1, b: 2, c: 3)
r4 = sum_three(a=10, b=67, c=45)
r5 = sum_three(a, b, c)
r6 = sum_three(a=10.9, b=67.89, c=45.998)
