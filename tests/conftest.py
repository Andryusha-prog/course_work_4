import pytest

from course_work_4.src.Vacancy import Vacancy


@pytest.fixture
def vacancy_sal_none_none():
    Vacancy('test', 'test', None, None, 'test')


@pytest.fixture()
def vacancy_sal_val_none():
    Vacancy('test', 'test', 1000, None, 'test')
