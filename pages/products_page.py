from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

        self.ADD_TO_CART_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.SHOPPING_CART_ICON = (By.CLASS_NAME, "shopping_cart_badge")

    def adicionar_backpack_ao_carrinho(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK_BUTTON).click()

    def capturar_icone_carrinho(self):
        return self.driver.find_element(*self.SHOPPING_CART_ICON).text
    
    def clicar_icone_carrinho(self):
        self.driver.find_element(*self.SHOPPING_CART_ICON).click()