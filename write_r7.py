
print("\t\t\tКОНСОЛЬ ДОБАВЛЕНИЯ РЕЗУЛЬТАТОВ: ")
name = input("Введите имя: ")
score = int(input('Введите кол-во очков: '))


def write_txt_result(name, score):
    lb_txt_file = open('lb.txt', 'a', encoding='utf-8')
    written_string = str(score) + ' - ' + name
    lb_txt_file.write(written_string)
    lb_txt_file.close()

#write_txt_result(name, score)
input('Выход')
