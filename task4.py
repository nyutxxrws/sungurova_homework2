s = input("Введите строку: ")
words = s.lower().split()
counter = {}
for w in words:
    if w not in counter:
        counter[w] = words.count(w)
for w in counter:
    print(w + ":", counter[w])