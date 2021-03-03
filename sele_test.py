import selenium
import pytest

from selenium import webdriver


class Test_Horgwarts():
	def setup(self):
		self.driver = webdriver.Chrome()
		pass

	def teardown(self):
		self.driver.quit()
		pass

	def test_horgwarts(self):
		self.driver.get("http://www.testerhome.com")
		self.driver.find_element_by_link_text("社团")
		pass
