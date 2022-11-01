from requests.exceptions import JSONDecodeError


def are_posts_sorted_by_id(response):

    ids_list = []
    [ids_list.append(i['id']) for i in response.json()]

    return ids_list.sort() is None


def is_answer_in_json_format(response):
    try:
        response.json()
    except JSONDecodeError:
        return False
    return True


def is_post_created_right(response, post_data):
    post_data['id'] = 101
    return post_data == response.json()
