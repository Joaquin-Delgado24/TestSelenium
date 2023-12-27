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
        i = 1804
        response = self.browser.get('https://apicompuplaza.compuplaza.net.pe/api/tienda_v1/Store/getProductoById/' + str(i))
        ## ¡Realizar pruebas en todas las solicitudes que contengan datos sensibles! ##

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
        # Pretty
        toPrint += 'Headers Pretty:\n' + request.response.headers.as_string() + '\n'

        # Find Headers
        toPrint += 'Searching for Cache Control headers: \n\n'

        # Cache-control
        toPrint += checkHeader(request.response.headers, 'Cache-control', 'no-store') + '\n'
        # Pragma
        toPrint += checkHeader(request.response.headers, 'Pragma', 'no-cache') + '\n'


        # Print a consola
        print(
            toPrint,
            '===========================\n'
        )

        # Print en archivo .txt
        with open('Cache-Control-' + time + '.txt', 'a') as f:
            f.write(toPrint + '\n===============================================================\n')

def checkHeader(headers, toCheck, value=None):
    if(headers.get(toCheck)):
        if(value):
            value = str(value)
            if(value in headers.get(toCheck)):
                return 'Header and Correct value Found: [' + toCheck + ']: ' + value
            else:
                return '[!] Header [' + toCheck + '] Found, but value [' + value + '] was not: ' + headers.get(toCheck)
        else:
            return 'Header Found: ' + toCheck
    else:
        return '[!] Header not Found: ' + toCheck
        

if __name__ == '__main__':
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    # Iniciar Unit test
    unittest.main(verbosity=2)
