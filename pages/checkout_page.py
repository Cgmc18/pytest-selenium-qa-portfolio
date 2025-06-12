from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.FIRST_NAME_INPUT = (By.ID, "first-name")
        self.LAST_NAME_INPUT = (By.ID, "last-name")
        self.POSTAL_CODE_INPUT = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")
        self.FINISH_BUTTON = (By.ID, "finish")
        self.COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def preencher_informacoes(self, nome, sobrenome, cep):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(nome)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(sobrenome)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(cep)

    def clicar_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def clicar_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def capturar_mensagem_sucesso(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text