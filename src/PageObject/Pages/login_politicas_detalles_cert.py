import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC


base_url ="https://ecommerce.andesscd.com.co/auth/login"

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username = "mail"
        self.password = "password"
        self.clickinicio = "kt_sign_in_submit"

    
    def get_username (self):
        return self.driver.find_element(By.NAME, self.username)
    
    def get_password (self):
        return self.driver.find_element(By.NAME, self.password)
    
    def get_submit_button(self):
        return self.driver.find_element(By.ID, self.clickinicio)
    
    def inicio_Sesion (self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
    
    def click_inicio(self):
        self.get_submit_button().click()

    @staticmethod
    def get_base_url():
        return base_url
    

class Politicas:
    def __init__(self, driver):
        self.driver = driver
        self.politica_terminos = "politica_terminos"
        self.politica_tratamiento = "politica_tratamientos"
        self.siguiente = ".indicator-label"

    def get_politica_terminos(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.ID, self.politica_terminos)))

    def get_politica_tratamiento(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.ID, self.politica_tratamiento)))

    def get_siguiente(self):    
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.siguiente)))    
    
    def politicas (self):
        self.get_politica_terminos().click()
        self.get_politica_tratamiento().click()
        self.get_siguiente().click()

class Detalles_Cert:
    def __init__(self, driver):
        self.driver = driver
        self.cupon = ".form-control-lg"
        self.pkcs10 = ".btn-outline"
        self.token_virtual = ".col:nth-child(2) > .btn"
        self.oneyear = ".col-md-4:nth-child(1) .fw-bolder"
        self.siguiente2 = ".indicator-label"

    def get_cupon (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.cupon)))
    
    def get_token_virtual (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.token_virtual)))
    
    def get_pkcs10 (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.pkcs10)))

    def get_oneyear(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.oneyear)))
    
    def get_siguiente2(self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.siguiente2))) 
       
    def detalle_cert_token_virtual (self, cupon):
        self.get_cupon().send_keys(cupon)
        self.get_token_virtual().click()
        self.get_oneyear().click()
        self.get_siguiente2().click()  

    def detalle_cert_pkcs10 (self, cupon):
        self.get_cupon().send_keys(cupon)
        self.get_pkcs10().click()
        self.get_oneyear().click()
        self.get_siguiente2().click()          