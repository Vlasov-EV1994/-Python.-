# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# Можно убрать проверки и всё прочее и сделать в 3-4 строки, но лучше с проверками
# Ввод данных.
num = input('Введите трёхзначное число: ')
# Проверка на то что введено число, а не символ
if num.isdigit():
    # Проверка на то что число является трёхзначным.
    if len(num) == 3:
        # Преобразование числа в список раздельных чисел.
        a = [int(i) for i in num]
        # Сумма всех чисел в списке.
        b = sum(a)
        # Произведение
        c = a[0] * a[1] * a[2] # Я не смог придумать что то получше чем это, но с учетом что есть проверки вариант нормальный
        # Вывод результата.
        print('Сумма =', b,
              'Произведение =', c)
    else:
        print('Число не соответствует!')
else:
    print('Не число!')



