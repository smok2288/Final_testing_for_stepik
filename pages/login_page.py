from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		# проверка на корректный url адрес
		assert self.url.find("login") > 0, "URL is not corrected"

	def should_be_login_form(self):
		# проверка, что есть форма логина
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		# проверка, что есть форма регистрации на странице
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

	def register_new_user(self, email, password):
		self.go_to_login_page()
		assert self.send_keys_element(*LoginPageLocators.REG_EMAIL, email), "Reg email is not exist"
		assert self.send_keys_element(*LoginPageLocators.REG_PASSWORD, password), "Reg password is not exist"
		assert self.send_keys_element(*LoginPageLocators.REG_CPASSWORD, password), "Reg confirm password is not exist"
		assert self.click_element(*LoginPageLocators.REGISTER_BTN), "Reg btn is not exist"
