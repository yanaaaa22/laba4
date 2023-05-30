def happy():
    ticket = input('Введите номер билета: ')
    x = 0
    y = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            x = x + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket))+1]:
            y = y + int(i)
        if x == y:
            print('Билет счастливый')
        else:
            print('Билет не счастливый')
    else:
        print('Такого билета нет')
happy()