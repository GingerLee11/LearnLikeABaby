from django.contrib.staticfiles.testing import StaticLiveServerTestCase


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

MAX_WAIT = 10

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

    