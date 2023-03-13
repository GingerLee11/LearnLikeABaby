from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

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

        # Sees the title of the home page
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Learn Like A Baby', header_text)

        # Sees the text explaining the name of the blog
        body = self.browser.find_element(By.TAG_NAME, 'body').text
        
        ## This might change if the blog is updated, 
        # but at least I can test to make sure the content doesn't disappear
        self.assertIn('A blog about learning. Why like a baby?', body)
        self.assertIn("You can't fill a cup that is already full.", body)

        # Akane sees all the different links for learning 
        ## This list might change, but I still need to test all of the current links
        learning_links = self.browser.find_elements(By.CLASS_NAME, 'list-group-item list-group-item-action')
        for link in learning_links:
            print(link.text)

        self.fail('Finish the test!')

