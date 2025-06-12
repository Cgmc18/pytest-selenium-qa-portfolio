from selenium.webdriver.common.by import By

class LoginPage:
    # O construtor da classe. É chamado quando criamos um objeto LoginPage.
    # Ele recebe o 'driver' (o navegador) como argumento.
    def __init__(self, driver):
        self.driver = driver

        self.URL = "https://www.saucedemo.com/"
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")
        self.ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def carregar(self):
        self.driver.get(self.URL)

    def fazer_login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def capturar_mensagem_erro(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text