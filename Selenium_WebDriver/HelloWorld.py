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



class HelloWorld(unittest.TestCase):
    #currentDir = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def setUp(cls):
        
        cls.driver = webdriver.Chrome(executable_path=r'chromedriver_win32/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.google.com.ar')

    def visitWikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod # run in only one window
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='hello-world-reports'))
    