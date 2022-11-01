import pytest
from tests_project.files.test_data import *
from framework.utils.random_util import get_random_word
from tests_project.api.json_placeholder_api import JsonPlaceholderApi
from framework.constants.http_status_codes import OK, CREATED, NOT_FOUND
from tests_project.steps.steps import *


@pytest.mark.API
class TestApi:

    def test_case_1(self):
        answer = JsonPlaceholderApi().get_all_posts(expected_code=OK)

        assert is_answer_in_json_format(answer), 'answer is not json'
        assert are_posts_sorted_by_id(answer), "posts aren't sorted"

    @pytest.mark.parametrize("post_id", [99])
    def test_case_2(self, post_id):
        answer = JsonPlaceholderApi().get_post_by_id(post_id=post_id, expected_code=OK)

        assert answer.json() == POST_99_DATA, 'received post info is not correct'

    @pytest.mark.parametrize("post_id", [150])
    def test_case_3(self, post_id):
        answer = JsonPlaceholderApi().get_post_by_id(post_id, expected_code=NOT_FOUND)

        assert answer.json() == {}, 'json from response is not empty'

    def test_case_4(self):
        json_file = {
            'title': get_random_word(),
            'body': get_random_word(),
            'userId': 1,
        }
        answer = JsonPlaceholderApi().create_post(json_file, expected_code=CREATED)

        assert is_post_created_right(answer, json_file), "Response data is wrong"

    def test_case_5(self):
        answer = JsonPlaceholderApi().get_all_users_data(expected_code=OK)

        assert is_answer_in_json_format(answer), 'answer is not json'

        assert answer.json()[4] == FIFTH_USER_DATA, 'answer is not correct'

    @pytest.mark.parametrize("user_id", [5])
    def test_case_6(self, user_id):
        answer = JsonPlaceholderApi().get_user_data_by_id(user_id, expected_code=OK)

        assert answer.json() == FIFTH_USER_DATA, 'answer is not correct'
