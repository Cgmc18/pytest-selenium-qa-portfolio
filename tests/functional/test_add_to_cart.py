from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_adicionar_produto_carrinho(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.carregar()
    login_page.fazer_login("standard_user", "secret_sauce")

    products_page.adicionar_backpack_ao_carrinho()
    texto_icone_carrinho = products_page.capturar_icone_carrinho()

    assert texto_icone_carrinho == "1", "O número no ícone do carrinho não é '1' após adicionar o produto."