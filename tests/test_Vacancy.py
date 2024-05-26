from course_work_4.src.Vacancy import Vacancy


def test_vacancy_equal_data():
    '''
    тест на проверку равентсва зарплат
    '''
    assert (Vacancy('test', 'test', None, None, 'test') ==
            Vacancy('test1', 'test1', None, None, 'test'))

    assert (Vacancy('test', 'test', 1000, None, 'test') !=
            Vacancy('test1', 'test1', None, None, 'test'))

    assert (Vacancy('test', 'test', None, None, 'test') !=
            Vacancy('test1', 'test1', None, 4000, 'test'))


def test_vacancy_lt_data():
    '''
    тест на проверку неравентсва зарплат self < other
    '''
    assert (Vacancy('test', 'test', None, None, 'test') <
           Vacancy('test1', 'test1', None, None, 'test')) is False

    assert (Vacancy('test', 'test', None, None, 'test') <
            Vacancy('test1', 'test1', 1000, None, 'test'))

    assert (Vacancy('test', 'test', 5, None, 'test') <
            Vacancy('test1', 'test1', 1000, None, 'test'))

    assert (Vacancy('test', 'test', None, None, 'test') <
            Vacancy('test1', 'test1', None, 60, 'test'))

    assert (Vacancy('test', 'test', None, 5, 'test') <
            Vacancy('test1', 'test1', None, 10, 'test'))

    assert (Vacancy('test', 'test', 1000, 2000, 'test') <
            Vacancy('test1', 'test1', 1000, 3000, 'test'))

    assert (Vacancy('test', 'test', 1000, 2000, 'test') <
            Vacancy('test1', 'test1', None, 3000, 'test')) is False


def test_vacancy_gt_data():
    '''
    тест на проверку неравентсва зарплат self > other
    '''
    assert (Vacancy('test', 'test', None, None, 'test') >
           Vacancy('test1', 'test1', None, None, 'test')) is False

    assert (Vacancy('test', 'test', 5, None, 'test') >
            Vacancy('test1', 'test1', None, None, 'test'))

    assert (Vacancy('test', 'test', 10, None, 'test') >
            Vacancy('test1', 'test1', 1, None, 'test'))

    assert (Vacancy('test', 'test', None, 60, 'test') >
            Vacancy('test1', 'test1', None, None, 'test'))

    assert (Vacancy('test', 'test', None, 10, 'test') >
            Vacancy('test1', 'test1', None, 5, 'test'))

    assert (Vacancy('test', 'test', 1000, 3000, 'test') >
            Vacancy('test1', 'test1', 1000, 2000, 'test'))

