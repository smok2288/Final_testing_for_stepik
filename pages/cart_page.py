from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
	def should_not_be_product_in_cart(self):
		assert self.is_not_element_present(*CartPageLocators.CART_TOTALS), "Product in cart, but should not be"

	def should_be_empty_cart(self):
		assert self.get_text(*CartPageLocators.CART_EMPTY_TXT).find("is empty") > 0, "Cart is not empty"
