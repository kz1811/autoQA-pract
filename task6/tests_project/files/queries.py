GET_DATA_FROM_TABLE_QUERY = """SELECT * 
                               FROM {}
                               WHERE mod(id, 11)=0 limit {};"""

INSERT_DATA_INTO_TESTS_TABLE_QUERY = """INSERT 
                                        INTO {} (name, project, result) 
                                        VALUES ('{}', '{}', '{}'); """

UPDATE_TESTS_TABLE_QUERY = """UPDATE {} SET result = '{}' 
                              WHERE id={}; """
