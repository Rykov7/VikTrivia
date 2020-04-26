def leader_text():
    print('\t\t\tДОСКА ЛИДЕРОВ')
    print("СЧЁТ\tИМЯ")
    print('--------------------------')
    try:
        f = open('lb.txt', 'r', encoding='utf-8')
        board = f.readlines()
        board.sort(reverse=True)

        for i in board:
            print(i, end='')

        f.close()
    except:
        input("\n\n\nНепредвиденная ошибка или файл отсутствует.")
    else:
        print('--------------------------')

leader_text()
input('Нажмите ENTER для выхода (reader)')
