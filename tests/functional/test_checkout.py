from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_finalizar_compra_sucesso(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.carregar()
    login_page.fazer_login("standard_user", "secret_sauce")
    products_page.adicionar_backpack_ao_carrinho()

    products_page.clicar_icone_carrinho()
    cart_page.clicar_checkout()

    checkout_page.preencher_informacoes("Ana", "Gomes", "29100-000")
    checkout_page.clicar_continue()
    checkout_page.clicar_finish()

    mensagem_sucesso = checkout_page.capturar_mensagem_sucesso()

    assert "Thank you for your order!" in mensagem_sucesso
    assert "checkout-complete.html" in driver.current_url