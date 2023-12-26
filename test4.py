import unittest
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

        # Realizar requests
        #for i in range (1, 18):
        site = 'https://compuplaza.net.pe/'
        response = self.browser.get(site)


        # Leer cookies
        printCookies(site, self.browser.get_cookies(), time)
                


def printCookies(site, cookies, time):

    #Title
    toPrint = 'Checking Cookies for site: ' + site + '\n\n'
    # List all Cookies
    toPrint += 'Listing Cookies: \n'
    for cookie in cookies:
        toPrint += '>> ' + cookie.get('name') + checkCookieAttributes(cookie) + '\n'
        toPrint += json.dumps(cookie, indent=2) + '\n'

    # Print a consola
    print(
        toPrint,
        '===========================\n'
    )

    # Print en archivo .txt
    with open('Cookie-Attributes-' + time + '.txt', 'a') as f:
        f.write(toPrint + '\n===============================================================\n')

def checkCookieAttributes(cookie):
    # Check that Path is not /
    noPath = (cookie.get('path') == "/")
    notSecure = (not cookie.get('secure'))

    ret = ''
    # Return warning string
    if noPath or notSecure:
        ret += ' (!) '
        if noPath:
            ret += '[Path not secure] '
        if notSecure:
            ret += '[Secure attribute is false] '
    return ret 

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
