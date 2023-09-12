import unittest
import urllib3
from selenium import webdriver


class WebDriverSetup (unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #self.driver = webdriver.Chrome(executable_path=r'C:\Users\felipe.ayala\OneDrive - ANDES SERVICIO DE CERTIFICACION DIGITAL S A\Documentos\QA\Automatizacion\POM\drivers\Chrome\chromedriver.exe')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    #Aqui coloco el codigo para generar el reporte en pdf
    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
