l1 = input("Введите первый список: ")
el1 = l1.split()
list1 = []
for num in el1:
    list1.append(int(num))
l2 = input("Введите второй список: ")
el2 = l2.split()
list2 = []
for num in el2:
    list2.append(int(num))
s1 = set(list1)
s2 = set(list2)
common = s1 & s2
print("Общие элементы:", end=" ")
for item in common:
    print(item, end=" ")