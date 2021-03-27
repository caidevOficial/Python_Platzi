# Copyright (C) 2021 <FacuFalcone - CaidevOficial>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import os
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    currentDir = os.path.dirname(os.path.realpath(__file__)) + "\chromedriver.exe"
    #rel_path = "C:\Users\Facu\Desktop\GitHub\Python_Platzi\Selenium_WebDriver\chromedriver_win32\chromedriver.exe"
    
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\Facu\Desktop\GitHub\Python_Platzi\Selenium_WebDriver\chromedriver_win32\chromedriver.exe')
        driver = self.driver
        driver.get('https://caidevoficial.github.io/Curriculum/')
        driver.maximize_window()
        #driver.implicitly_wait(20) #Wait until close

    def test_search_textField(self):
        search_field = self.driver.find_element_by_id("myPhoto")

    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element_by_name("q")
    
    def test_search_test_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("shadow")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("container")

    def test_xPath(self):
        img_path = self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/img")

    # def test_count_of_promo_banner_images(self):
    #     banner_list = self.driver.find_element_by_class_name("promos")
    #     banners = banner_list.find_element_by_tag_name('img')
    #     self.assertEqual(3,len(banners))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports', report_name='search-reports'))
