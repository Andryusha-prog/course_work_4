from abc import ABC, abstractmethod


class FileConnector(ABC):

    @abstractmethod
    def add_vacancy_to_file(self, vacancy):
        """
        Функция добавления вакансии в файл
        """
        pass

    @abstractmethod
    def get_vacancies_from_file(self):
        """
         Функция возвращает список вакансий из файла
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Функция удаляет указанную вакансию из  файла
        """
        pass
