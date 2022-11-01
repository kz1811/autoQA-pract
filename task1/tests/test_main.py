import pytest
from tests.pages.home_page import HomePage
from tests.pages.game_page import GamePage
from framework.utils.logger import Logger


class TestTask1:

    @pytest.mark.UI
    def test_case_cards(self):
        Logger.info('Открытие Home Page')
        home_page = HomePage()
        assert home_page.is_opened(), 'Home Page was not opened'

        Logger.info('Открытие Game Page')
        home_page.click_here_link()
        game_page = GamePage()
        assert game_page.first_card.is_opened(), 'First Card was not opened'

        Logger.info('Заполнение формы 1, принятие условий и переход на форму 2')
        game_page.first_card.fill_and_submit_the_card()
        assert game_page.second_card.is_opened(), 'Second Card was not opened'

        Logger.info('Загрузка изображения, выбор 3 пунктов и переход на форму 3')
        game_page.second_card.download_and_upload_image()
        game_page.second_card.pick_three_interests()
        game_page.second_card.click_next_button()
        assert game_page.third_card.is_opened(), "Third Card was not opened"

    @pytest.mark.UI
    def test_case_2(self):
        Logger.info('Открытие Home Page')
        home_page = HomePage()
        assert home_page.is_opened(), 'Home Page was not opened'

        Logger.info('Открытие Game Page')
        home_page.click_here_link()
        game_page = GamePage()
        assert game_page.is_opened(), 'Game Page was not opened'

        Logger.info('Сворачивание Help Form')
        assert game_page.hide_help_form(), 'help form was not hiding'

    @pytest.mark.UI
    def test_case_3(self):
        Logger.info('Открытие Home Page')
        home_page = HomePage()
        assert home_page.is_opened(), 'Home Page was not opened'

        Logger.info('Открытие Game Page')
        home_page.click_here_link()
        game_page = GamePage()
        assert game_page.is_opened(), 'Game Page was not opened'

        Logger.info('Принятие cookies')
        assert game_page.accept_cookies(), 'Cookies was not accepted or the header is not absent'

    @pytest.mark.UI
    def test_case_4(self):
        Logger.info('Открытие Home Page')
        home_page = HomePage()
        assert home_page.is_opened(), 'Home Page was not opened'

        Logger.info('Открытие Game Page')
        home_page.click_here_link()
        game_page = GamePage()
        assert game_page.is_opened(), 'Game Page was not opened'

        Logger.info('Проверка, начинает ли таймер отсчет с 0')
        assert game_page.get_timer() == '00:00:00', 'Timer starts not from zero'
