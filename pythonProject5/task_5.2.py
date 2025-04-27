words = []
while True:
        vvod = input()

        if vvod == 'stop':
            break
        else:
           words.append(vvod)
rez = ' '.join(words)
print(rez)
