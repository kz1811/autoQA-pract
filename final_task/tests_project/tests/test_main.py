from framework.utils.logger import Logger
from framework.browser.browser import Browser
from framework.utils.screenshooter import Screenshooter
from tests_project.tests.base import SqlPrepare
from tests_project.files.test_data import *
from tests_project.steps.steps import Steps
from tests_project.pages.test_page import TestPage
from tests_project.pages.main_page import MainPage
from tests_project.pages.project_page import ProjectPage
from tests_project.api.reporting_test_portal_api import ReportingTestPortalApi


class TestFinalTask(SqlPrepare):

    def test_case(self):
        Logger().info('Getting the token')
        token = ReportingTestPortalApi().get_token()
        assert token is not None, "token wasn't generated"

        # 2

        main_page = MainPage()
        assert main_page.is_opened(), "Main Page was not opened"
        Logger().info('Setting the token')
        Browser().set_cookie('token', token)

        Logger().info('Refreshing the page')
        main_page.refresh_page()

        Logger().info('Checking is right number in the footer')
        assert main_page.is_right_number_in_the_footer(), "Number in the footer wasn't correct"

        Logger().info('Clicking nexage button')
        main_page.click_project_link()

        nexage_page = ProjectPage(PROJECT_NAME)
        Logger().info('Checking is Nexage Page is opened')
        assert nexage_page.is_opened(), "Nexage page wasn't opened"

        # 3

        Logger().info('Getting tests by project name with database')
        tests = Steps().get_tests_by_project_name(builder=self.builder, project_name=PROJECT_NAME)

        Logger().info('Checking are tests from database and tests from UI Nexage Page the same')
        assert nexage_page.is_tests_same(tests), "tests are not the same"

        Logger().info('Checking are tests sorted by date and time')
        assert Steps().is_tests_sorted_by_datetime(tests), "tests don't sorted by name"

        # 4

        Logger().info('Go to the previous page')
        Browser().go_to_the_previous_page()
        main_page = MainPage()
        assert main_page.is_opened(), "Main page wasn't opened"

        Logger().info('Creating new project')
        main_page.click_add_button()
        project_name = main_page.input_and_save_project_data()

        Logger().info('Checking is project successfully added')
        assert main_page.is_success_alert_message_presented(project_name), "Project was not added"

        Logger().info('Closing add project window with js-script')
        main_page.close_add_project_window()

        Logger().info('Checking is add project window closed')
        assert main_page.is_add_project_window_closed(), "Add Project window was not closed"
        main_page.refresh_page()

        Logger().info(f'Checking is new project with name "{project_name}" added')
        assert main_page.is_project_on_page(name=project_name), f'Project "{project_name}" is not in the page'

        # 5

        Logger().info('Go to new page')
        main_page.click_project_link(project_name)
        project_page = ProjectPage(project_name)
        assert project_page.is_opened(), "Project Page was not opened"

        Logger().info('Adding new test with logs and screenshot')
        screenshot_path = Screenshooter().take_screenshot()
        test_model = self.builder.add_test(screenshot=screenshot_path, logs=LOGS_PATH, project_name=project_name)

        Logger().info('Checking is test presented on page')
        assert project_page.is_test_on_page(test=test_model), "Test is not on page"

        # 6

        Logger().info('Go to the test page')
        project_page.click_to_test_link(test=test_model)
        test_page = TestPage(test_model.test_name)

        Logger().info('Checking is test page opened')
        assert test_page.is_opened(), "Test Page was not opened"

        Logger().info('Checking is test data valid')
        assert test_page.is_fields_of_test_valid(self.builder, test_model), "test data aren't correct"

        Logger().info('Checking are upload and local screenshot copies the same')
        assert test_page.is_test_screenshot_valid(screenshot_path=screenshot_path), "Upload image and image on server " \
                                                                                    "are not the same "
