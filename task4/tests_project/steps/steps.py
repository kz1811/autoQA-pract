class Steps:

    def dict_number_with_max_value_of_param(self, list_of_dicts, param):
        max_value = 0
        index = None
        for i in range(len(list_of_dicts)):
            if list_of_dicts[i][f'{param}'] > max_value:
                max_value = list_of_dicts[i][f'{param}']
                index = i
        return index
