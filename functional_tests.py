import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_get_title(self):
        self.browser.get('localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Stop testing!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
