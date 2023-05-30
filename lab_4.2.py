def hundred():
    try:
        x = int(input('Введите число'))
        k = 100 / x
    except ZeroDivisionError:
        print('На ноль нельзя делить')
    except ValueError:
        print('Вы ввели не число')
    else:
        print('100 / ' , x , '=' , k)
hundred()




