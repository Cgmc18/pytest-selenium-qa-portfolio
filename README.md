# Automação de Testes com Pytest e Selenium

![Licença](https://img.shields.io/github/license/Cgmc18/pytest-selenium-qa-portfolio)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Framework](https://img.shields.io/badge/framework-Pytest-red)
![Automação](https://img.shields.io/badge/automação-Selenium-green)

## 📖 Sobre o Projeto

Este repositório demonstra a construção de uma suíte de testes de automação web com foco em código limpo e boas práticas de qualidade, testando a aplicação `saucedemo.com`.

O projeto aplica os seguintes conceitos e tecnologias:
* **Framework:** Pytest, usando `fixtures` para preparar o ambiente de cada teste (abrindo o navegador) e limpá-lo no final.
* **Padrão de Design:** Page Object Model (POM) para garantir a reutilização e manutenção do código.
* **Tecnologias:** Python e Selenium WebDriver para a automação das interações no navegador.
* **Estrutura:** Organização de testes em escopos `Funcional` e `End-to-End` (E2E).

---

## 🚀 Como Rodar Localmente

Siga os passos abaixo para executar os testes na sua máquina.

### 1. Preparando o Ambiente
Primeiro, clone o projeto e entre na pasta:
```bash
git clone [https://github.com/Cgmc18/pytest-selenium-qa-portfolio.git](https://github.com/Cgmc18/pytest-selenium-qa-portfolio.git)
cd pytest-selenium-qa-portfolio
```
Depois, crie e ative um ambiente virtual:
```bash
# Cria o ambiente
python -m venv venv

# Ativa no Windows
.\venv\Scripts\activate

# Ativa no Mac/Linux
source venv/bin/activate
```

### 2. Instalando as Dependências
Com o ambiente ativo, instale tudo o que o projeto precisa:
```bash
pip install -r requirements.txt
```

### 3. Executando os Testes
Agora é só rodar o `pytest`!

```bash
# Para rodar todos os testes
pytest

# Para rodar apenas os testes funcionais
pytest tests/functional/

# Para rodar apenas os testes de jornada completa (E2E)
pytest tests/e2e/

# Dica: adicione -v para ver mais detalhes da execução
pytest -v
```

---

## 👨‍💻 Autor

Feito com ❤️ por **Carol Gomes**.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anagmc/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Cgmc18)

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.