from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math
import re

class BasePage(object):

	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def click_element(self, how, what):
		try:
			self.browser.find_element(how, what).click()
		except NoSuchElementException:
			return False
		return True

	def get_text(self, how, what):
		try:
			return self.browser.find_element(how, what).text
		except NoSuchElementException:
			return None

	def get_num(self, how, what):
		try:
			numtxt = self.browser.find_element(how, what).text.replace(',', '.')
			return float(re.findall(r'\d+.\d+', numtxt)[0])
		except NoSuchElementException:
			return None

	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()

	def go_to_cart_page(self):
		link = self.browser.find_element(*BasePageLocators.CART_LINK)
		link.click() 

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True

	def is_not_element_present(self, how, what, timeout = 4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False

	def is_disappeared(self, how, what, timeout = 4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True

	def open(self):
		self.browser.get(self.url)

	def send_keys_element(self, how, what, key):
		try:
			self.browser.find_element(how, what).send_keys(key)
		except NoSuchElementException:
			return False
		return True

	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			print("Your code: {}".format(alert.text))
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")