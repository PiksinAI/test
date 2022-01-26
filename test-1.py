# работает для всех 1e-n, где 1 < n < 324, а grade = n + 1
number = 1e-155
grade = 156
i = 0
while abs(number) < 1:
    i += 1
    number = round(number, grade - i)
    number *= 10
    print(number)
