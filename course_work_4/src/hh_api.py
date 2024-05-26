import requests

from course_work_4.src.BaseVacancyAPI import BaseVacancyAPI
from course_work_4.src.Vacancy import Vacancy


class HeadHunterAPI(BaseVacancyAPI):
    def get_vacancies(self, search: str) -> list[Vacancy]:
        url = 'https://api.hh.ru/vacancies'

        params = {
            'text': search,
            'per_page': 100,
            'only_with_salary': True
        }

        response = requests.get(url, params=params, timeout=100)

        if not response.ok:
            raise ConnectionError
        else:
            return [
                self.parse_vacancy(item) for item in response.json()['items'] if item['salary']['currency'] == 'RUR'
            ]

    @staticmethod
    def parse_vacancy(data: dict) -> Vacancy:
        return Vacancy(
            name=data['name'],
            url=data['alternate_url'],
            sal_from=data['salary']['from'],
            sal_to=data['salary']['to'],
            requirement=data['snippet']['requirement']
        )
