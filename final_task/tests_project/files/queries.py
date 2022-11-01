# Queries

GET_TESTS_DATA = """select * from test;"""

GET_PROJECT_DATA_BY_NAME_QUERY = """select * from project """ \
                                 """where name='{}';"""

# GET_TESTS_BY_PROJECT_ID_QUERY = "select * from test " \
#                                 "where project_id={} " \
#                                 "group by name, method_name, status_id, start_time " \
#                                 "order by start_time desc " \
#                                 "limit {};"

GET_TESTS_BY_PROJECT_ID_QUERY = """select name, MAX(start_time) as time from test """ \
                                """where project_id={} """ \
                                """group by name """ \
                                """order by 2 desc """ \
                                """limit {};"""

GET_TEST_DATA_BY_NAME_AND_START_TIME = """select * from test """ \
                                       """where name="{}" and start_time="{}"; """

GET_PROJECT_NAME_BY_ID = """select name from project where id={};"""

CREATE_TEST_QUERY = """insert into test (name, method_name, start_time, project_id, status_id, session_id, env, browser) """ \
                    """values ("{}", "{}", "{}", {}, {}, {}, "{}", "{}");"""

GET_TEST_ID_BY_TEST_DATA = """select id from test """ \
                           """where name="{}" and method_name="{}" and status_id={} and start_time="{}" """ \
                           """and session_id={} and browser="{}" and env="{}";"""

ATTACH_SCREENSHOT = """insert into attachment (content, content_type, test_id) """ \
                    """values (%s, 'image/png', %s);"""

ATTACH_LOG = """insert into log (content, test_id) """ \
             """values (%s, %s);"""