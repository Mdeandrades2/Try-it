import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NovaReceitaTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK ="https://tastyflavorfusion.azurewebsites.net/novareceita/" 
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_criar_nova_receita(self):
        
        self.driver.get(self.SITE_LINK)

        ingredientes = self.driver.find_element(By.ID, "ingredientes")
        botao1 = self.driver.find_element(By.XPATH, "//div[@class='botao1']/button[@class='btn btn-primary']")
        botao2 = self.driver.find_element(By.XPATH, "//div[@class='botao2']/a[@class='btn btn-secondary']")

        # Preencha os campos com informações de teste
        nome_input.send_keys("Minha Nova Receita")
        ingredientes.send_keys("Ingrediente 1\nIngrediente 2\nIngrediente 3")

        # Clique no botão "Criar Receita"
        botao1.click()

        # Verifique se você foi redirecionado para a página correta após a criação da receita
        self.assertEqual(self.driver.current_url, "https://tastyflavorfusion.azurewebsites.net/recomendacoes/" )  
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

    

class CadastroTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "https://tastyflavorfusion.azurewebsites.net/cadastrar_usuario/"
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

        # Clique no botão "Criar Conta"
        criar_conta_button.click()

        time.sleep(5)  # Aguarde algum tempo para ver a página após o clique

        # Verifique se você foi redirecionado para a página correta após o cadastro
        self.assertEqual(self.driver.current_url, "https://tastyflavorfusion.azurewebsites.net/filter-recipe/") 


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


class ReceitasFavoritadasTest(unittest.TestCase):


    def setUp(self):
        self.SITE_LINK = "https://tastyflavorfusion.azurewebsites.net/favoritados/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_visualizar_receitas(self):
        self.driver.get(self.SITE_LINK)

        # Aguarde até 5 segundos até que o elemento com a tag "h2" esteja presente
        h2_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

        # Verifique se a página contém os títulos das receitas
        titulos_receitas = self.driver.find_elements(By.TAG_NAME, "h2")
        self.assertEqual(len(titulos_receitas), 3)  # Deve haver 3 receitas

        # Clique no primeiro título de receita
        titulos_receitas[0].click()

        # Aguarde até 10 segundos até que o elemento com a tag "p" esteja presente
        p_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )

        # Verifique se a página contém informações sobre a receita
        self.assertTrue("Panqueca Americana" in self.driver.page_source)

        # Navegue de volta à página principal
        self.driver.back()

        # Repita o processo para as outras receitas, se necessário...

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


