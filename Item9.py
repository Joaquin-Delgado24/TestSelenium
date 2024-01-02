import unittest
from anyio import sleep
#from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire.utils import decode
from datetime import datetime
import json
import logging

class RequestTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_get_request(self):
        time = datetime.now().strftime("%d-%m-%y-%H%M%S")

        # Realizar carga de pagina
        response = self.browser.get('https://compuplaza.net.pe')
        self.browser.save_screenshot('C:/Users/User/Documents/GitHub/TestSelenium/Screenshots/IdleSession-' + time + '-0.png')
        # Esperar 50 minutos
        sleep(3000)
        self.browser.save_screenshot('C:/Users/User/Documents/GitHub/TestSelenium/Screenshots/IdleSession-' + time + '-1.png')  
        

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
