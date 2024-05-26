from course_work_4.src.hh_api import HeadHunterAPI

hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies('python')

for i, vacan in enumerate(hh_vacancies):
    print(i, repr(vacan), sep='\n')

