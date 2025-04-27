import random

def math_game():
    trueAnsw = 0
    falseAnsw = 0

    while trueAnsw < 3 and falseAnsw < 3:

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        answer = input(f"{num1} + {num2} = ")

        if answer.isdigit() and int(answer) == num1 + num2:
            trueAnsw += 1
            print("Правильно!")
        else:
            falseAnsw += 1
            print("Ответ неверный.")
    if trueAnsw == 3:
        print(f"Игра окончена. Вы победили:) Правильных ответов: {trueAnsw}")
    else:
        print(f"Игра окончена. Вы проиграли:( Правильных ответов: {trueAnsw}")

math_game()

