from course_work_4.src.hh_api import HeadHunterAPI


def test_parser(dict_data, vac_data):
    assert HeadHunterAPI.parse_vacancy(dict_data) == vac_data
