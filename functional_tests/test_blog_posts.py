from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import unittest
import time

from .base import FunctionalTest


class BlogPostTests(FunctionalTest):

    def test_can_view_blog_post_information(self):

        # New user Akane visits learnlikeababy.com
        self.browser.get(self.live_server_url)

        # Sees Learn Like A Baby in the browser title of the page
        self.wait_for(lambda:
            self.assertIn('Learn Like A Baby', self.browser.title)
        )
        try:
            self.browser.find_element(By.LINK_TEXT, 'Blog Posts').click()
        except NoSuchElementException:
            self.browser.find_element(By.CLASS_NAME, 'navbar-toggler-icon').click()
            self.wait_for(lambda:
                self.browser.find_element(By.LINK_TEXT, 'Blog Posts').click()
                )
            
        self.wait_for(lambda:
            self.assertIn('Blog Posts', self.browser.title)    
        )

    def test_user_can_create_update_and_delete_a_blog_post(self):
        # New user tries to create, update and delete blog posts
        self.browser.get(self.live_server_url)