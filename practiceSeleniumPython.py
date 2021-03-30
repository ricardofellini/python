import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    ## Open our website and verify if the title is correct
    def test_Software_Online(self):
        driver = self.driver
        driver.get("http://sol.ec.eco.br/solerp/")
        self.assertIn("Login do Sistema", driver.title)

    ## Find the user element and send key user
        user = driver.find_element_by_name("usuario")
        user.clear()
        user.send_keys("ricardof")

    ## Find the password element and send key password

        password = driver.find_element_by_name("senha")
        password.clear()
        password.send_keys("")

    ## Find the button submit then click
        botaoLogin = driver.find_element_by_class_name("botaoLogin")
        botaoLogin.submit()

     ## Verify if the page is logged
        self.assertIn("EcoCentauro SOL", driver.title)
if __name__ == '__main__':
        unittest.main()

