# работает для всех 1e-n, где 1 < n < 324, а grade = n + 1
number = float(input('Введите число в экспоненциальном виде: '))
num_str = str(number)
grade_str = ''
point = False
for char in num_str:
    if point:
        grade_str += char
    if char == 'e':
        point = True
grade = abs(int(grade_str)) + 1
print(grade)
i = 0
while abs(number) < 1:
    i += 1
    number = round(number, grade - i)
    number *= 10
    print('Мантисса: ', int(number))
