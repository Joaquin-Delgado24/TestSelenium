import unittest
import time
#from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.common.by import By
from datetime import datetime
import json
import logging

class RequestTestCase(unittest.TestCase):

    def setUp(self):
        self.browser1 = webdriver.Firefox()
        self.browser2 = webdriver.Firefox()
        self.addCleanup(self.browser1.quit)
        self.addCleanup(self.browser2.quit)

    def test_get_request(self):
        timenow = datetime.now().strftime("%d-%m-%y-%H%M%S")

        # Realizar carga de pagina
        self.browser1.get('https://compuplaza.net.pe')
        time.sleep(5)
        self.browser2.get('https://compuplaza.net.pe')
        time.sleep(5)
        # Tomar screenshots
        self.browser1.save_screenshot('C:/Users/User/Documents/GitHub/TestSelenium/Screenshots/CS-' + timenow + '-Session1.png')
        self.browser2.save_screenshot('C:/Users/User/Documents/GitHub/TestSelenium/Screenshots/CS-' + timenow + '-Session2.png')   
        

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
