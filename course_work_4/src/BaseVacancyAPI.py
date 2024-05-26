from abc import ABC, abstractmethod


class BaseVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search: str) -> list[dict]:
        pass
