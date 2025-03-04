mesto = int(input("Введите номер места: "))

if mesto < 1 or mesto > 54:
    print("Неверный номер места. В плацкартном вагоне всего 54 места.")
else:

    if mesto in range(1, 37):  # Нижние места
        if mesto % 6 in [1, 2, 3, 4]:
            print("Нижнее купе")
        else:
            print("Нижнее боковое")
    else:                           # Верхние места
        if mesto % 6 in [1, 2]:
            print("Верхнее купе")
        else:
            print("Верхнее боковое")
