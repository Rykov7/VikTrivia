

person = ['Petr', '17', 'Moskva'] # ['Vasya', '1', '1960'], ['Petya', '14', '1998']]


k = 0 # Длина пароля
counter = 0 # 16-ричный счетчик
base = len(person)
words = []

while k < 4:
    password = ''

    i = counter
    while i > 0:
        r = i % base
        password = person[r] + password
        i = i // base
        list_length.append

    password =  person[0] * (k - len(password)) + password

    print(f'{counter}\t{password}')

    counter += 1
    if password == person[-1] * k:
        k += 1
        counter = 0
input()