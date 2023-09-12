from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


generador_csr = "https://www.dondominio.com/es/products/ssl/tools/csr-create/"

class Csr:
    def __init__(self, driver):
        self.driver = driver
        self.generador_csr = generador_csr
        self.commonName = ".form-group:nth-child(1) input"
        self.organizationName = ".form-group:nth-child(2) input"
        self.organizationalUnitName = ".form-group:nth-child(3) input"
        self.csr_email = ".form-group:nth-child(4) .floating-placeholder > input"
        self.csr_estado = "//div[@id='app-router']/form/div[5]/div[2]/div[2]/div/div/div[2]/input"
        self.csr_ciudad = "//div[@id='app-router']/form/div[5]/div[3]/div[2]/div/div/div[2]/input"
        self.crear_csr = ".btn-violet"
        self.csr_generado = "//textarea[@name='csr_result']"

    def get_commonName (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.commonName)))
        
    def get_organizationName (self):
        return self.driver.find_element(By.CSS_SELECTOR, self.organizationName)

    def get_organizationalUnitName (self):
        return self.driver.find_element(By.CSS_SELECTOR, self.organizationalUnitName)
    
    def get_csr_email (self):
        return self.driver.find_element(By.CSS_SELECTOR, self.csr_email)
    
    def get_csr_estado (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, self.csr_estado)))
    
    def get_csr_ciudad(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, self.csr_ciudad)))
    
    def get_crear_csr(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.crear_csr)))
    
    def get_csr_generado(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, self.csr_generado)))
    
    def open_csr_generator(self):
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(self.generador_csr)

    def generar_csr (self, commonName, organizationName, organizationalUnitName, csr_email, csr_estado, csr_ciudad):
        Identificado_Ecommerce = self.driver.current_window_handle
        self.open_csr_generator()
        Identificador_Dondominio = self.driver.window_handles[-1]
        self.driver.switch_to.window(Identificador_Dondominio)
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        scroll_to_position = scroll_position + 600  # Ajusta el valor según tus necesidades
        self.driver.execute_script(f"window.scrollTo(0, {scroll_to_position});")
        self.get_commonName().send_keys(commonName)
        self.get_organizationName().send_keys(organizationName)
        self.get_organizationalUnitName().send_keys(organizationalUnitName)
        self.get_csr_email().send_keys(csr_email)
        self.get_csr_estado().send_keys(csr_estado + Keys.ENTER)
        self.get_csr_ciudad().send_keys(csr_ciudad + Keys.ENTER)
        self.get_crear_csr().click()
        csr_element = self.get_csr_generado()
        csr_value = csr_element.get_attribute("value")
        self.driver.close()
        self.driver.switch_to.window(Identificado_Ecommerce)
        return csr_value
    
    @staticmethod
    def get_generador_csr():
        return generador_csr