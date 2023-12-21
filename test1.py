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
        for i in range (1, 18):
        #i = 1804
            response = self.browser.get('https://apicompuplaza.compuplaza.net.pe/api/tienda_v1/Store/getProductoById/' + str(i))

        # Leer requests
        for request in self.browser.requests:
            if request.response:
                printResponse(request, time)
                


def printResponse(request, time):
    response = request.response
    if 'firefox' not in request.url and request.response.headers['Content-type'] == 'application/json':
        # formar Body
        body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
        # formar body Pretty
        body2 = json.dumps(json.loads(body), indent=2)
        
        # Request
        toPrint = 'Request: ' + request.url + '\n'
        # Headers
        toPrint += 'Headers:\n' + json.dumps(request.response.headers.as_string()) + '\n'
        # Body
        toPrint += 'Body: \n' + str(body) + '\n'
        # Pretty
        toPrint += 'Pretty: \n' + body2 + '\n'

        # Print a consola
        print(
            toPrint,
            '===========================\n'
        )

        # Print en archivo .txt
        with open('Request-' + time + '.txt', 'a') as f:
            f.write(toPrint + '\n===============================================================\n')

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
