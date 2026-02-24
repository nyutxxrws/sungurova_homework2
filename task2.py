dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
kset = set()
for key in dct:
    kset.add(key)
vset = set()
for key in dct:
    value = dct[key]
    vset.add(value)
union = set()
for key in kset:
    union.add(key)
for value in vset:
    union.add(value)
print("Множество ключей: ", kset)
print("Множество значений: ", vset)
print("Объединение множеств: ", union)