import os.path

from course_work_4.src.Vacancy import Vacancy
from course_work_4.src.hh_api import HeadHunterAPI
from course_work_4.src.json_con import ConnectorJSON

hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies('python')

path = os.path.join('data', 'vacancies.json')

conn_js = ConnectorJSON(path)

#for i, vacan in enumerate(hh_vacancies):
#    print(i, repr(vacan), sep='\n')

vac1 = Vacancy('name', 'url', 10, 20, 'test_text')

vac2 = Vacancy('name2', 'url2', 20, 30, 'test_text')
vac3 = Vacancy('name3', 'url3', 30, 40, 'test_text')
conn_js.add_vacancy_to_file(vac1)
conn_js.add_vacancy_to_file(vac2)
conn_js.add_vacancy_to_file(vac3)

print(conn_js.get_vacancies_from_file())

conn_js.delete_vacancy(vac1)
conn_js.delete_vacancy(vac3)

print(conn_js.get_vacancies_from_file())
