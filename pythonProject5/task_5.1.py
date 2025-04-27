N = int(input("Введите количество слов: "))
words = []

for x in range(N):
    vvod = input("Введите слово:")
    words.append(vvod)
rez = ' '.join(words)
print(rez)

