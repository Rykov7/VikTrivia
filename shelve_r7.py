import shelve

print("\t\t\tКОНСОЛЬ ДОБАВЛЕНИЯ РЕЗУЛЬТАТОВ: ")
name = input("Введите имя: ")
score = int(input('Введите кол-во очков: '))

lb_dat = shelve.open('lb')
lb_dat[name] = score
lb_dat.close()

input('Выход')