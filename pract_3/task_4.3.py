first = str(input("Введите цвет1: "))
two = str(input("Введите цвет2: "))

if (first == "красный" and two == "желтый") or (first == "желтый" and two == "красный"):
    print (f"При смешивании цветов: {first} и {two}, мы получаем оранжевый цвет")

if (first == "синий" and two == "желтый") or (first == "желтый" and two == "синий"):
    print(f"При смешивании цветов: {first} и {two}, мы получаем зеленый цвет")

if (first == "красный" and two == "синий") or (first == "синий" and two == "красный"):
    print(f"При смешивании цветов: {first} и {two}, мы получаем фиолетовый цвет")
