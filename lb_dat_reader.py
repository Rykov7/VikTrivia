def leader():
    import shelve
    print('\t\t\tДОСКА ЛИДЕРОВ')
    print("МЕСТО\tСЧЁТ\tИМЯ")
    print('--------------------------')
    counter = 0


    try:
        lb = []
        s = shelve.open('lb')
        for i in s:
            lb.append((s[i], i))
            lb.sort(reverse=True)
            lb = lb[:10]
        for i in lb:
            counter += 1
            print(f'   {counter}\t {i[0]}\t{i[1]}')
    except:
        input("\n\n\nНепредвиденная ошибка или файл отсутствует.")
    else:
        print('--------------------------')

    s.close()