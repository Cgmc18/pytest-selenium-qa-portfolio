from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    def clicar_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()