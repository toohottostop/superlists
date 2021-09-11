import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def _check_rows_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_get_title(self):
        self.browser.get('localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do lists', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertIn(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self._check_rows_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make peacock feather bait')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self._check_rows_in_list_table('1: Buy peacock feathers')
        self._check_rows_in_list_table('2: Make peacock feather bait')

        self.fail('Stop testing!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
