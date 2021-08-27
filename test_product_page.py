from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
import pytest
import time

@pytest.mark.register_user
class TestUserAddToCartFromProductPage(object):
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/"
		self.reg_page = LoginPage(browser, link)
		self.reg_page.open()
		self.reg_page.go_to_login_page()
		self.reg_page.register_new_user(str(time.time()) + "@fakemail.org", "1234567!P")
		self.reg_page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_cart(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=NewYear2019"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_add_to_basket()
		#page.solve_quiz_and_get_code()
		page.should_be_add_correct_product()
		page.should_be_correct_sum()

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_cart(browser, link):
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_promo_url("promo=newYear2019")
	page.should_be_add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_add_correct_product()
	page.should_be_correct_sum()

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_basket()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

def test_message_dissapeared_after_adding_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_basket()
	page.should_not_be_success_message2()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_cart_page()
	cart_page = CartPage(browser=browser, url=browser.current_url)
	cart_page.should_not_be_product_in_cart()
	cart_page.should_be_empty_cart()
