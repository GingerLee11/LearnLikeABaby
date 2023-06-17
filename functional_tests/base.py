from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

MAX_WAIT = 10
User = get_user_model()

def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    @wait
    def wait_for(self, fn):
        return fn()
    
    def create_and_authenticate_user(self, first_name='Test', last_name='User', email='test@example.com', password='Somanythings!'):

        # Create the user
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)

        # Visit the login page
        self.browser.get(self.live_server_url + '/login/')

        # Fill in the login form
        email_input = self.browser.find_element(By.ID, 'id_email')
        email_input.send_keys(email)
        password_input = self.browser.find_element(By.ID, 'id_password')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        # Wait for the login process to complete
        self.wait_for(lambda: self.assertEqual(self.browser.current_url, self.live_server_url + '/'))

        return user
    
    @wait
    def fill_out_form(self, form_attributes):
        for attribute_id, text in form_attributes.items():
            element = self.browser.find_element(By.ID, attribute_id)
            if text == None:
                self.wait_for(lambda:
                    element.click()
                )
            else:
                self.wait_for(lambda:
                    element.send_keys(text)
                )
        element.submit()

    