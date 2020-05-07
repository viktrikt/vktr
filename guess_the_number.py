# Игра в угадывание чисел.
import random
secretNumber = random.randint(1, 20)
print('Мною задумано число в интервале от 1 до 20. Попробуйте его угадать.')

#Предоставить игроку 6 попыток для угадывания число.
for quessesTaken in range(1, 7):
    print('Ваш вариант:')
    quess = int(input())

    if quess < secretNumber:
        print('Предложенное число меньше задуманного.')
    elif quess > secretNumber:
        print('Предложенное число больше задуманного.')
    else:
        break #Соответствует правильному ответу!

if quess == secretNumber:
    print('Верно! Количество попыток: ' + str(quessesTaken))
else:
    print('Нет. Было задумано число ' + str(secretNumber))
