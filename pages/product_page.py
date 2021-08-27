from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def should_be_promo_url(self, promotxt):
		# проверка на наличие promotxt в url адреса
		parIdx = self.url.find("?")
		assert parIdx > 0 and self.url.find(promotxt) > parIdx, "URL is not corrected"

	def should_be_add_to_basket(self):
		# проверка, что товар добавляется в корзину
		assert self.click_element(*ProductPageLocators.ADD_BTN), "Product don't add to basket"

	def should_be_add_correct_product(self):
		# проверка, что нужный товар добавлен в корзину
		assert self.get_text(*ProductPageLocators.PRODUCT_NAME).strip() == self.get_text(*ProductPageLocators.ADD_PRODUCT_NAME).strip(), "Product is not corrected"

	def should_be_correct_sum(self):
		# проверка, что сумма пересчиталась корректно
		assert self.get_num(*ProductPageLocators.SUM_BASKET) == self.get_num(*ProductPageLocators.PRODUCT_PRICE), "Sum is not corrected"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def should_not_be_success_message2(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should not be"
