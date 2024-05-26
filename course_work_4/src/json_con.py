import json
import os
from course_work_4.src.Vacancy import Vacancy
from course_work_4.src.file_connector import FileConnector


class ConnectorJSON(FileConnector):

    def __init__(self, path_json: os.path):
        """
        При инициализации указывается путь к файлу с вакансиями
        """
        self.path_json = path_json

    def add_vacancy_to_file(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies_from_file()
        if vacancy not in vacancies:
            vacancies.append(vacancy)

        vacancies_dict = self.parse_list_to_dict(vacancies)
        self.save_func(vacancies_dict)

    def get_vacancies_from_file(self) -> list[Vacancy]:
        """
        На первом шаге проводится проверка того, что файл существует и он не пустой, иначе возвращается пустой список
        """
        if not os.path.exists(self.path_json) or os.stat(self.path_json).st_size == 0:
            return []
        else:
            with open(self.path_json, 'r') as file:
                return self.parse_dict_to_class(json.load(file))

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies_from_file()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            vacancies_dict = self.parse_list_to_dict(vacancies)
            self.save_func(vacancies_dict)

    @staticmethod
    def parse_dict_to_class(inp_data: list[dict]) -> list[Vacancy]:
        """
        Функция преобразует список словарей в список классов вакансии, что необходимо при чтении из файла
        """
        vacancies = []
        for js_f in inp_data:
            vac = Vacancy(js_f['name'], js_f['url'], js_f['salary_from'], js_f['salary_to'],
                          js_f['requirement'])
            vacancies.append(vac)
        return vacancies

    @staticmethod
    def parse_list_to_dict(vacancies: list[Vacancy]) -> list[dict]:
        """
        функция выполняет преобразование из списка экземляров класса вакансии в список словарей для сохранения в файл
        """
        vacancy_list = []
        for vac in vacancies:
            dict_vacancy = {
                'name': vac.name,
                'url': vac.url,
                'salary_from': vac.sal_from,
                'salary_to': vac.sal_to,
                'requirement': vac.requirement
            }
            vacancy_list.append(dict_vacancy)
        return vacancy_list

    def save_func(self, vacancies: list[dict]) -> None:
        """
        Функция для сохранения подготовленного списка словарей в файл вакансии
        """
        with open(self.path_json, 'w') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=2)
