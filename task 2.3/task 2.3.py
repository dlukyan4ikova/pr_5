def tip_mesta(mesto):
    if mesto < 1 or mesto > 54:
        return "Такого места нет. Введите номер места от 1 до 54."

    if mesto in range(1, 37):  # Нижние места
        if mesto % 6 in [1, 2, 3, 4]:
            return "Нижнее купе"
        else:
            return "Нижнее боковое"
    else:  # Верхние места
        if mesto % 6 in [1, 2]:
            return "Верхнее купе"
        else:
            return "Верхнее боковое"
mesto = int(input("Введите номер места: "))
mesto = tip_mesta(mesto)
print(mesto)