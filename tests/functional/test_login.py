from pages.login_page import LoginPage

def test_login_sucesso(driver):

    login_page = LoginPage(driver)
    
    login_page.carregar()
    login_page.fazer_login("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url, "Login falhou ou não redirecionou para a página de produtos."

def test_login_falha(driver):

    login_page = LoginPage(driver)

    login_page.carregar()
    login_page.fazer_login("locked_out_user", "secret_sauce")
    mensagem_erro = login_page.capturar_mensagem_erro()
    
    assert "Sorry, this user has been locked out" in mensagem_erro, "A mensagem de erro para usuário bloqueado não apareceu."