import requests
from tests_project.files import test_data
from framework.api.client_api import ClientApi
from framework.utils import random_util
from tests_project.files import test_data
from tests_project.steps.steps import Steps


class VkApiWrapper:

    access_token = test_data.ACCESS_TOKEN

    def create_text_post(self, message=random_util.get_random_word(), owner_id=test_data.OWNER_ID, return_data=1):

        url = f'/method/wall.post?' \
              f'access_token={self.access_token}&' \
              f'owner_id={owner_id}&' \
              f'message={message}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url )
        post_id = answer.json()['response'].get('post_id')

        if post_id is not None:
            if return_data == 0:
                return True
            else:
                return True, post_id, message
        else:
            raise RuntimeError('Post was not created')

    def edit_post(self, post_id, attach_item_id, message=random_util.get_random_word(),
                  owner_id=test_data.OWNER_ID,
                  type_attach_item='photo', ):

        url = f'/method/wall.edit?' \
              f'access_token={self.access_token}&' \
              f'owner_id={owner_id}&' \
              f'post_id={post_id}&' \
              f'message={message}&' \
              f'attachments={type_attach_item}{owner_id}_{attach_item_id}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )

        if answer.json()['response'].get('post_id'):
            return message, attach_item_id
        else:
            raise RuntimeError('Post was not edited')

    def add_comment(self, post_id, message=random_util.get_random_word(), owner_id=test_data.OWNER_ID, ):

        url = f'/method/wall.createComment?' \
              f'access_token={self.access_token}&' \
              f'owner_id={owner_id}&' \
              f'post_id={post_id}&' \
              f'message={message}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )

        return message

    def is_post_liked(self, type_item, item_id, owner_id=test_data.OWNER_ID):

        url = f'/method/likes.isLiked?' \
              f'access_token={self.access_token}&' \
              f'owner_id={owner_id}&' \
              f'type={type_item}&' \
              f'item_id={item_id}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )
        answer = answer.json()['response']

        return answer['liked']

    def delete_post(self, post_id, owner_id=test_data.OWNER_ID):

        url = f'/method/wall.delete?' \
              f'access_token={self.access_token}&' \
              f'owner_id={owner_id}&' \
              f'post_id={post_id}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )
        is_deleted = answer.json()['response']

        return is_deleted

    def get_upload_photo_server_link(self):

        url = f'/method/photos.getWallUploadServer?' \
              f'access_token={self.access_token}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )
        return answer.json()['response']['upload_url']

    def upload_photo(self, photo_path=test_data.IMAGE_PATH):

        img = {'photo': ('image.jpg', open(f'{photo_path}', 'rb'))}
        url = self.get_upload_photo_server_link()

        answer = ClientApi().send_post_request(endpoint=url, files=img).json()

        url = f'/method/photos.saveWallPhoto?' \
              f'access_token={self.access_token}&' \
              f'photo={answer["photo"]}&' \
              f'hash={answer["hash"]}&' \
              f'server={answer["server"]}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )
        photo_id = answer.json()['response'][0]['id']

        return photo_id

    def download_photo(self, image_id, owner_id=test_data.OWNER_ID, download_path=test_data.DOWNLOAD_IMAGE_PATH):

        url = f'/method/photos.getById?' \
              f'access_token={self.access_token}&' \
              f'photos={owner_id}_{image_id}&' \
              f'v={test_data.VERSION_VK_API}'

        answer = ClientApi().send_post_request(endpoint=url, )

        sizes = answer.json()['response'][0]['sizes']

        index = Steps().dict_number_with_max_value_of_param(sizes, 'height')
        url = sizes[index]['url']

        answer = requests.get(url)
        with open(download_path, 'wb') as img:
            img.write(answer.content)

        return download_path
