import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NovaReceitaTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "https://tryit.azurewebsites.net/novareceita/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_criar_nova_receita(self):
        self.driver.get(self.SITE_LINK)

        ingredientes = self.driver.find_element(By.ID, "ingredientes")
        botao1 = self.driver.find_element(By.XPATH, "//div[@class='botao1']/button[@class='btn btn-primary']")
        botao2 = self.driver.find_element(By.XPATH, "//div[@class='botao2']/a[@class='btn btn-secondary']")

        nome_input.send_keys("Minha Nova Receita")
        ingredientes.send_keys("Ingrediente 1\nIngrediente 2\nIngrediente 3")

        botao1.click()
        self.assertEqual(self.driver.current_url, "https://tryit.azurewebsites.net/recomendacoes/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

class CadastroTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "https://tryit.azurewebsites.net/cadastrar_usuario/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_cadastro(self):
        self.driver.get(self.SITE_LINK)

        nome_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "nome")))
        sobrenome_input = self.driver.find_element(By.ID, "sobrenome")
        username_input = self.driver.find_element(By.ID, "username")
        senha_input = self.driver.find_element(By.ID, "senha")
        submit = self.driver.find_element(By.ID, "criar-conta-button")
        cancelar_button = self.driver.find_element(By.ID, "cancelar-button")

        username_input.send_keys("marimbcorreia")
        senha_input.send_keys("123456")

        criar_conta_button.click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://tryit.azurewebsites.net/filtrarreceita/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

class ReceitasFavoritadasTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "https://tryit.azurewebsites.net/favoritados/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_visualizar_receitas(self):
        self.driver.get(self.SITE_LINK)

        h2_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

        titulos_receitas = self.driver.find_elements(By.TAG_NAME, "h2")
        self.assertEqual(len(titulos_receitas), 3)

        titulos_receitas[0].click()
        p_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )

        self.assertTrue("Panqueca Americana" in self.driver.page_source)
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
