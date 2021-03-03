from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestQiywx:
	def setup(self):
		option = Options()
		option.debugger_address = "127.0.0.1:9222"
		self.driver = webdriver.Chrome()

	def teardown(self):
		pass

	def test_qiywx(self):
		self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
		# print(self.driver.get_cookies())
		cookies = [
			{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
			 'value': '1688850166224948'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
			 'value': 'n1AEJoIoFvjBwE2vT7VRQHnK28PnyJvIKn_WRlGUgKoJzsMh0ea72ZvD_Y0ynNMXl4ZrJdhw28yU0yiHRrv0l-Wa1e6ERwh6nGPFE_ms4pfW9ZKT4pxcL3Td-C-Ov_M3ODcLzPvKLFZ599uAOBDbzDw1WxrVbXIBz0tW_Yupk8Fytw3zdcZPQWLfYkgrQoBiYpGKOIHJhfRFzBlxryYYyiw1N_Ykqlsxi002EgqlMWeKHl-T-XpL8FDxq6vHxNe_fayK69d0GP4vVGn7HNMK-A'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
			 'value': '1688850166224948'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
			 'value': '1970325068436233'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
			 'value': 'd9fYLqX9YcMzcSQv-Ct0GmKIYwlqcirTszfBjqM0sz4zWYpugP2nkSdaS5reJy-K'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
			 'value': 'a450745'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
			 'value': '1'},
			{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
			 'secure': False, 'value': '6893765232'},
			{'domain': '.work.weixin.qq.com', 'expiry': 1646286214, 'httpOnly': False,
			 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614750214'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
			 'value': 'direct'},
			{'domain': 'work.weixin.qq.com', 'expiry': 1614781634, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
			 'secure': False, 'value': '8rcmlis'},
			{'domain': '.qq.com', 'expiry': 1614837145, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
			 'value': 'GA1.2.1418273197.1614750215'},
			{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
			 'value': '10578281543078949'},
			{'domain': '.qq.com', 'expiry': 1677822745, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
			 'value': 'GA1.2.1222403110.1614750215'},
			{'domain': '.work.weixin.qq.com', 'expiry': 1646286098, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
			 'path': '/', 'secure': False, 'value': '0'},
			{'domain': '.work.weixin.qq.com', 'expiry': 1617343057, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
			 'path': '/', 'secure': False, 'value': 'zh'},
			{'domain': '.qq.com', 'expiry': 1929951659, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
			 'secure': False, 'value': '0_669334669f022'}]
		for cookie in cookies:
			self.driver.add_cookie(cookie)
		self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
