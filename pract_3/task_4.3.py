first = str(input("Введите цвет 1: "))
two = str(input("Введите цвет 2: "))

if (first == "красный" and two == "желтый") or (first == "желтый" and two == "красный"):
    print (f"При смешивании цветов: {first} и {two}, мы получим оранжевый цвет")

if (first == "синий" and two == "желтый") or (first == "желтый" and two == "синий"):
    print(f"При смешивании цветов: {first} и {two}, мы получим зеленый цвет")

if (first == "красный" and two == "синий") or (first == "синий" and two == "красный"):
    print(f"При смешивании цветов: {first} и {two}, мы получим фиолетовый цвет")
