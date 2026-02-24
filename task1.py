user_input = input("Введите числа через пробел: ")
elements = user_input.split()
power = int(input("Введите степень: "))
result = []
for el in elements:
    if el.lstrip('-').isdigit():
        num = int(el)
        result.append(num ** power)
    else:
        result.append(el * power)
print("Вывод:", end=" ")
for item in result:
    print(item, end=" ")