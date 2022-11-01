from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.form import Form
from framework.elements.text import Text
from framework.elements.link import Link
from framework.elements.button import Button
from tests_project.files import test_data
from tests_project.api.vk_api_wrapper import VkApiWrapper
from framework.utils import compare_images


class ProfilePage(BasePage):

    WALL_MODULE_LOCATOR = (By.ID, "profile_wall")
    POST_LOCATOR = "post{}_{}"
    POST_AUTHOR_LOCATOR = "//div[@id='post{}_{}']//h5[@class='post_author']/a[contains(@href, '{}')]"
    POST_TEXT_LOCATOR = "//div[@data-post-id='{}_{}']//div[contains(@class, 'wall_post_text')]"
    SHOW_COMMENTS_LOCATOR = '''//a[contains(@onclick, "wall.showNextReplies(this, '{}_{}")]'''
    COMMENT_AUTHOR_LOCATOR = "//div[@id='replies{}_{}']//a[@data-from-id='{}']"
    COMMENT_TEXT_LOCATOR = "//div[@id='replies{}_{}']//div[text()='{}']"
    REACTION_BUTTON_LOCATOR = "//div[@data-reaction-target-object='wall{}_{}']"

    def __init__(self, page_name='Profile'):
        self.locator = self.WALL_MODULE_LOCATOR[1]
        self.page_name = page_name
        self.search_condition = self.WALL_MODULE_LOCATOR[0]

    def is_post_on_page(self, post, author, message):

        post_locator = (By.ID, self.POST_LOCATOR.format(author, post))
        post_form = Form(post_locator[0], post_locator[1], 'post')
        post_form.wait_for_is_present()

        post_author_locator = (By.XPATH, self.POST_AUTHOR_LOCATOR.format(author, post, author))
        post_author = Link(post_author_locator[0], post_author_locator[1], 'post author')
        post_author.wait_for_is_present()

        post_text_locator = (By.XPATH, self.POST_TEXT_LOCATOR.format(author, post))
        post_text = Text(post_text_locator[0], post_text_locator[1], 'post')

        return post_form.is_exist() and post_author.is_exist() and (post_text.get_text() == message)

    def is_post_changed(self, post, author, message, image_id):

        post_text_locator = (By.XPATH, self.POST_TEXT_LOCATOR.format(author, post))
        post_text = Text(post_text_locator[0], post_text_locator[1], 'post')

        photo_path = VkApiWrapper().download_photo(image_id=image_id)

        is_images_equal = compare_images.compare_images(test_data.IMAGE_PATH, photo_path)

        return post_text.get_text() == message and is_images_equal

    def is_comment_added(self, post_id, author, message):

        show_comments_locator = (By.XPATH, self.SHOW_COMMENTS_LOCATOR.format(author, post_id))
        show_messages = Link(show_comments_locator[0], show_comments_locator[1], 'show next replies')
        show_messages.click()

        comment_author_locator = (By.XPATH, self.COMMENT_AUTHOR_LOCATOR.format(author, post_id, author))
        commenter_link = Link(comment_author_locator[0], comment_author_locator[1], 'author of the comment')
        commenter_link.wait_for_is_present()

        comment_text_locator = (By.XPATH, self.COMMENT_TEXT_LOCATOR.format(author, post_id, message))
        comment_text = Text(comment_text_locator[0], comment_text_locator[1], 'comment')
        comment_text.wait_for_is_present()

        return commenter_link.is_exist() and comment_text.is_exist()

    def like_the_post(self, post_id, author=test_data.OWNER_ID):

        reaction_button_locator = (By.XPATH, self.REACTION_BUTTON_LOCATOR.format(author, post_id))
        like_button = Button(reaction_button_locator[0], reaction_button_locator[1], "like")
        like_button.click()

    def is_post_deleted(self, post_id):

        post_locator = (By.ID, self.POST_LOCATOR.format(test_data.OWNER_ID, post_id))
        post_form = Form(post_locator[0], post_locator[1], "post")

        post_form.wait_for_invisibility()

        return not post_form.is_displayed()

