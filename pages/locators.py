from selenium.webdriver.common.by import By

class MainPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
	LOGIN_FORM		= (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM	= (By.CSS_SELECTOR, "#register_form")
	REG_EMAIL		= (By.CSS_SELECTOR, "#id_registration-email")
	REG_PASSWORD	= (By.CSS_SELECTOR, "#id_registration-password1")
	REG_CPASSWORD	= (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BTN	= (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators(object):
	ADD_BTN				= (By.CSS_SELECTOR, "button.btn-add-to-basket")
	PRODUCT_NAME		= (By.CSS_SELECTOR, ".product_main h1")
	ADD_PRODUCT_NAME	= (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
	PRODUCT_PRICE		= (By.CSS_SELECTOR, ".product_main p")
	SUM_BASKET			= (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
	SUCCESS_MESSAGE		= (By.XPATH, "//*[@id='messages']/div[1]/div/strong")

class BasePageLocators(object):
	LOGIN_LINK			= (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID	= (By.CSS_SELECTOR, "#login_link_inc")
	CART_LINK			= (By.CSS_SELECTOR, ".btn-default[href*='basket']")
	CART_LINK_INVALID	= (By.CSS_SELECTOR, "#basket_unlink")
	USER_ICON			= (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
	CART_EMPTY_TXT	= (By.CSS_SELECTOR, "#content_inner p")
	CART_TOTALS		= (By.CSS_SELECTOR, "#basket_totals")
