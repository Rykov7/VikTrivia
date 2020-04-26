#!/usr/bin/env python3
# Викторина
# Читает сплошной текстовый файл

import sys
import shelve
from lb_dat_reader import leader


def open_file(file_name, mode):
    # 1. Пробуем открыть файл.
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Невозможно открыть файл', the_file, 'Завершение программы\n', e)
        input('\n\nНажмите Enter для выхода')
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    # 2. Функция перевода строки.
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    # 3. Переход к следующему блоку вопросов.
    question = next_line(the_file)
    answers = []
    for v in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    # 3.1. Если мы на строке "Правильного ответа" (да), то верный ответ - это первый символ данной строки.
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    nominal = next_line(the_file)
    return question, answers, correct, explanation, nominal


def welcome(title):
    # 4. Блок приветствия. Забирает первую строку базы данных с заголовком.
    print('\t\tДобро пожаловать в VikTrivia by @Rykov7\n')
    print('\t\tТема викторины: ' +  title + '\n')


def yes_no(yes_no_question):
    answer = input(yes_no_question)
    while answer.upper() != 'Y':
        answer = input(yes_no_question)


def feedback(max_num, user_num, user_name):
    if max_num == user_num:
        print('Ты - ГУРУ истории США! Поздравляю, ' + user_name + '! Ты ответил на все вопросы верно!')
    elif user_num > 1500:
        print('Ты - ЗНАТОК истории США! Молодец, ' + user_name + '! Ты ответил почти на все вопросы верно!')
    elif user_num > 600:
        print('Ты - СОУ-СОУ... что-то ты, ' + user_name + ', знаешь об истории США и это уже неплохо.')
    else:
        print('Ты - НЕ ЗНАТОК истории США, ' + user_name + '. Но, надеюсь, ты узнал что-то новое из викторины!')

def main():
    # 5. Основной блок.
    usa_file = open_file('usa.t', 'r')
    title = next_line(usa_file)
    welcome(title)
    name = input('\nКак вас зовут?: ')
    full_score = 0
    question_counter = 0
    score = 0
    # 5.1 Вызываем первый блок:
    question, answers, correct, explanation, nominal = next_block(usa_file)

    while question:
        print(question)
        full_score += int(nominal)
        question_counter += 1
        for v in range(4):
            print('\t', v+1, '-', answers[v])
        answer = input("Каков ваш ответ?: ")
        if answer == correct:
            print('\nВерно!', end=' ')
            score += int(nominal)
        else:
            print('\nНеправильно...', end=' ')
        print(explanation)
        print('ОЧКОВ:', score, '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n')
        input('<ENTER> ДАЛЕЕ >>>\n\n\n')
        question, answers, correct, explanation, nominal = next_block(usa_file)

    usa_file.close()
	
    print(f'Это был последний из {question_counter} вопросов.')
    feedback(full_score, score, name)
    print(f'Твой окончательный счёт: {score} / {full_score}\n' )

    lb_dat = shelve.open('lb')
    lb_dat[name] = score
    lb_dat.close()



main()
leader()
yes_no('Хотите выйти? (Y/N): ')
input('\n\nНажмите Enter для выхода.')