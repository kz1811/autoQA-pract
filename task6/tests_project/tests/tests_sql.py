import sys
import pytest
from tests_project.steps.steps import Steps
from framework.utils.config_parser import ConfigParser
from tests_project.tests.base import SqlPrepare


class TestSqlFillingTheTable(SqlPrepare):

    @pytest.mark.parametrize('value', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_one_is_one(self, value, post_condition_query, query_type=None, test_id=None):
        result = (1 == 1)

        post_condition_query(Steps().get_ending_query(test_id=test_id,
                                                      name=sys._getframe().f_code.co_name,
                                                      result=result,
                                                      query_type=query_type))

        assert result, "one is not one"

    @pytest.mark.parametrize('value', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_two_is_two(self, value, post_condition_query, query_type=None, test_id=None):
        result = (2 == 2)

        post_condition_query(Steps().get_ending_query(test_id=test_id,
                                                      name=sys._getframe().f_code.co_name,
                                                      result=result,
                                                      query_type=query_type))

        assert result, "two is not two"

    @pytest.mark.parametrize('value', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_three_is_three(self, value, post_condition_query, query_type=None, test_id=None):
        result = (3 == 3)

        post_condition_query(Steps().get_ending_query(test_id=test_id,
                                                      name=sys._getframe().f_code.co_name,
                                                      result=result,
                                                      query_type=query_type))

        assert result, "three is not three"

    @pytest.mark.parametrize('value', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_four_is_four(self, value, post_condition_query, query_type=None, test_id=None):
        result = (4 == 4)

        post_condition_query(Steps().get_ending_query(test_id=test_id,
                                                      name=sys._getframe().f_code.co_name,
                                                      result=result,
                                                      query_type=query_type))

        assert result, "four is not four"

    functions = {'test_one_is_one': test_one_is_one,
                 'test_two_is_two': test_two_is_two,
                 'test_three_is_three': test_three_is_three,
                 'test_four_is_four': test_four_is_four}


class TestSqlChangingTheData(TestSqlFillingTheTable):

    def test_reload_the_tests(self, post_condition_query):
        for value in range(ConfigParser().get_config()['num_of_test_runs']):
            self.test_one_is_one(value=value, post_condition_query=post_condition_query)
            self.test_two_is_two(value=value, post_condition_query=post_condition_query)
            self.test_three_is_three(value=value, post_condition_query=post_condition_query)
            self.test_four_is_four(value=value, post_condition_query=post_condition_query)

        value = 1
        table_data = Steps().get_data_from_table(self.postgresql)
        Steps().reload_the_tests_from_table(funcs=self.functions, value=value, table_data=table_data,
                                            fixture=post_condition_query)
