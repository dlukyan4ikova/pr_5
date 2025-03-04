password1 = input("Введите пароль: ")

if len(password1) < 6:
    print("Пароль ненадежный. Придумайте новый пароль.")
else:
    password2 = input("Повторите пароль: ")
    if password1 == password2:
        print("Пароль принят.")
    else:
        print("Пароль не принят.")