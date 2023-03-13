from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import unittest
import time

from .base import FunctionalTest


class BlogPostTests(FunctionalTest):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_home_page_information(self):
        # New user Akane visits learnlikeababy.com
        self.browser.get('http://localhost:8000/')

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

        