import pytest

from course_work_4.src.Vacancy import Vacancy


@pytest.fixture
def vacancy_sal_none_none():
    Vacancy('test', 'test', None, None, 'test')


@pytest.fixture()
def list_vacancy():
    list_vac = []
    vac1 = Vacancy('test_name', 'test_url', 1000, None, 'test_requirement')
    list_vac.append(vac1)
    return list_vac


@pytest.fixture()
def dict_test_list_data():
    return [{
        'name': 'test_name',
        'url': 'test_url',
        'salary_from': 1000,
        'salary_to': None,
        'requirement': 'test_requirement'
    }]


@pytest.fixture()
def dict_data():
    return {
        'name': 'test_name',
        'alternate_url': 'test_url',
        'salary': {
            'from': 1000,
            'to': None
        },
        'snippet': {
            'requirement': 'test_requirement'
        }
    }


@pytest.fixture()
def vac_data():
    return Vacancy('test_name', 'test_url', 1000, None, 'test_requirement')
