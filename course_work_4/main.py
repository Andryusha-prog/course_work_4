import os.path

from course_work_4.src.hh_api import HeadHunterAPI
from course_work_4.src.json_con import ConnectorJSON

hh_api = HeadHunterAPI()
path = os.path.join('data', 'vacancies.json')
conn_js = ConnectorJSON(path)

#Приветственное сообщение при запуске программы
welcome_message = '''
Добро пожаловать в программу отображения вакансий сайта HH.ru.
Данная программа вможет выполнять следующие действия (введите цифру для выбора):
0 - Выход из программы
1 - Формирование Файла с данными вакансии сайта HH.ru по ключевому слову
2 - Вывод первых N вакансий с лучшей предложенной зарплатой
'''

while True:
    print(welcome_message)
    user_input = input()

    if user_input.isdigit():
        user_input_digit = int(user_input)
        if int(user_input_digit) == 0:
            break
        elif int(user_input_digit) == 1:
            user_key = input('input key word: ')
            hh_vacancies = hh_api.get_vacancies(user_key) # функция запроса данных вакансии от HH.ru
            for vacancy in hh_vacancies:
                conn_js.add_vacancy_to_file(vacancy) #функция добавления вакансии в файл

        elif int(user_input_digit) == 2:
            vacancies = conn_js.get_vacancies_from_file() #функция формирования списка вакансий из файла
            if len(vacancies) == 0:
                print('Файл пустой! Сначала необходимо сформировать файл!')
                continue
            else:
                user_num = int(input('Введите количество топ вакансий:'))
                for vac in sorted(vacancies, key=lambda x: x.sal_from, reverse=True)[:user_num]:
                    print(vac)
    else:
        continue
