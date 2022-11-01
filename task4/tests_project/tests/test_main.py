import time
import pytest
from tests_project.pages.auth_pages.login_page import LoginPage
from tests_project.pages.auth_pages.pass_page import PasswPage
from tests_project.pages.menu_column_form import MenuForm
from tests_project.api.vk_api_wrapper import VkApiWrapper
from tests_project.pages.profile_page import ProfilePage
from tests_project.files import test_data
from framework.utils.logger import Logger


class TestVk:
    def test_vk_post_and_comment_functional(self):

        Logger().info('Переход на страницу ввода логина')
        login_page = LoginPage()
        assert login_page.is_opened()

        Logger().info('Ввод логина и подтверждение')
        login_page.send_login()

        Logger().info('Переход на страницу ввода пароля')
        passw_page = PasswPage()
        assert passw_page.is_opened(), "PassPage was not opened"

        Logger().info('Ввод пароля и подтверждение')
        passw_page.send_password()

        Logger().info('Переход на страницу новостей после авторизации: взаимодействие с меню')
        menu_form = MenuForm()
        assert menu_form.is_opened(), "MenuForm was not opened"

        Logger().info('Переход на страницу профиля')
        menu_form.click_to_my_page_item()

        profile_page = ProfilePage()
        assert profile_page.is_opened(), "ProfilePage was not opened"

        Logger().info('API-запрос на создание записи на стене со случайно сгенерированным текстом')
        api_client = VkApiWrapper()
        is_created, post_id, message = api_client.create_text_post()

        Logger().info('Проверка, что на стене появилась запись со случайно сгенерированным тестом от тестового '
                      'пользователя')
        assert profile_page.is_post_on_page(post=post_id, author=test_data.OWNER_ID,
                                            message=message), "Post not found"

        Logger().info('API-запрос нна редактирование записи на стене: замена текста и загрузка картинки')
        message, item_id = api_client.edit_post(post_id=post_id, type_attach_item='photo', attach_item_id=api_client.upload_photo())

        Logger().info('Проверка, что текст записи на стене изменился и картинка соответствует загруженной')
        assert profile_page.is_post_changed(post=post_id, author=test_data.OWNER_ID, message=message, image_id=item_id), \
            "Photo does not match uploaded or text of message has not changed"

        Logger().info('API-запрос на добавление комментария к записи')
        message = api_client.add_comment(post_id)

        Logger().info('Проверка, что добавился комментарий со случайно сгенерированым текстом от тестового пользователя')
        assert profile_page.is_comment_added(author=test_data.OWNER_ID, message=message, post_id=post_id), "Comment is not added"

        Logger().info('Отметка "Мне нравится" под записью на стене')
        profile_page.like_the_post(post_id)

        Logger().info('API-запрос, проверяющий, поставил ли тестовый пользователь отметку "Мне нравится"')
        assert api_client.is_post_liked('post', post_id)

        Logger().info('API-запрос на удаление поста')
        api_client.delete_post(post_id=post_id)

        Logger().info('Проверка, что пост с указанными данными от тестового пользователя был удален')
        assert profile_page.is_post_deleted(post_id=post_id), "post was not deleted"
