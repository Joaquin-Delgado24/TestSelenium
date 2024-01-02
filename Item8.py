import unittest
from anyio import sleep
#from selenium import webdriver
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.common.by import By
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
        # Logout
        self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[3]/div/a/svg').click()
        sleep(5)
        # Retroceder
        self.browser.back()
        sleep(5)
        # Tomar screenshot
        self.browser.save_screenshot('C:/Users/User/Documents/GitHub/TestSelenium/Screenshots/BackBrowsing-' + time + '.png')  

            

def checkHeader(headers, toCheck):
    if(headers.get(toCheck)):
        value = headers.get(toCheck)
        return '[!] Header found: [' + toCheck + ']: ' + value
    else:
        return 'Header not Found: ' + toCheck
        

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
