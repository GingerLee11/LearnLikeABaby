from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import unittest
import time

from .base import FunctionalTest


class BlogPostTests(FunctionalTest):

    def test_can_register_and_then_login(self):

        # New user visits learnlikeababy.com
        self.browser.get(self.live_server_url)

        # Sees Learn Like A Baby in the browser title of the page
        self.wait_for(lambda:
            self.assertIn('Learn Like A Baby', self.browser.title)
        )
        # User sees the Login button at the top right of the page and clicks on it
        self.browser.find_element(By.LINK_TEXT, 'Login').click()

        # This taskes them to the login page
        self.wait_for(lambda:
            self.assertIn('Login', self.browser.title)
        )
        # The new user does not yet have an account, 
        # so they click on the register link
        # Something like: (Don't have an account, register here)
        self.browser.find_element(By.LINK_TEXT, 'Register').click()

        # This taskes them to the register page
        self.wait_for(lambda:
            self.assertIn('Register', self.browser.title)
        )

        # They fill in their registration information
        form_attributes = {
            'id_email': 'test@exmple.com',
            'id_password1': 'noonecanguessthis!',
            'id_password2': 'noonecanguessthis!',
        }

        self.fill_out_form(form_attributes)

        self.wait_for(lambda: self.assertIn('Login', self.browser.title))

        form_attributes = {
            'id_email': 'test@exmple.com',
            'id_password': 'noonecanguessthis!',
        }

        self.fill_out_form(form_attributes)

        self.wait_for(lambda: self.assertIn('Learn Like A Baby', self.browser.title))



        self.fail('Finish the test!')
