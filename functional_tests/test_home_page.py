from selenium import webdriver

import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_home_page_information(self):
        # New user Akane visits learnlikeababy.com
        self.browser.get('http://localhost:8000/')

        # Sees Learn Like A Baby in the title of the page
        self.assertIn('Learn Like A Baby', self.browser.title)
        time.sleep(4)
        


if __name__ == '__main__':  
    unittest.main()
