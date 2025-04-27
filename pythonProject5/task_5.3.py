def rarely_word(word):
    if not word.isalpha():
        print("Ошибка: введены не буквенные символы!")
        return

    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

vvod = input("Введите слово: ")
rarely_word(vvod)

