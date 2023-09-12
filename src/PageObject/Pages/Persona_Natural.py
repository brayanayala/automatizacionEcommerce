import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
       
class PersonaNatural:
    def __init__(self, driver):
        self.driver = driver
        self.tipocert = ".col-md-3:nth-child(4) > .btn"
        self.identificacion = "pregunta_2"
        self.fecha_exp = "3"
        self.nombre = "pregunta_4"
        self.apellido = "pregunta_5"
        self.departamento = "6"
        self.municipio = "7"
        self.direccion = "pregunta_8"
        self.correo_titular = "pregunta_9"
        self.telefono = "pregunta_10"
        self.celular = "pregunta_11"
        self.vigencia = "12"
        self.plataforma = "13"
        self.referido = "14"
        self.idfactuacion = "15"
        self.ccfacturacion = "pregunta_16"
        self.rzfacturacion = "pregunta_17"
        self.departamento_facturacion = "18"
        self.municipio_facturacion = "19"
        self.direccion_facturacion = "pregunta_20"
        self.telefono_factura = "pregunta_21"
        self.correo_factura = "pregunta_22"
        self.archivo_cc = "documento_2"
        self.siguiente_registro = ".flex-stack > div:nth-child(2)"

         


    def get_tipocert(self):
        return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.tipocert)))
    
    def get_identificacion (self):
        return WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.NAME, self.identificacion)))
    
    def get_fecha_exp (self):
        return self.driver.find_element(By.ID, self.fecha_exp)

    def get_nombre (self):
        return self.driver.find_element(By.NAME, self.nombre)
    
    def get_apellido (self):
        return self.driver.find_element(By.NAME, self.apellido)

    def get_departamento(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.departamento)))

    def get_municipio(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.municipio)))
    
    def get_direccion (self):
        return self.driver.find_element(By.NAME, self.direccion)
    
    def get_correo_titular (self):
        return self.driver.find_element(By.NAME, self.correo_titular)

    def get_telefono (self):
        return self.driver.find_element(By.NAME, self.telefono)
    
    def get_celular (self):
        return self.driver.find_element(By.NAME, self.celular)
    
    def get_vigencia (self):
        return self.driver.find_element(By.ID, self.vigencia)
    
    def get_plataforma (self):
        return self.driver.find_element(By.ID, self.plataforma)
    
    def get_referido (self):
        return self.driver.find_element(By.ID, self.referido)
    
    def get_idfactuacion (self):
        return self.driver.find_element(By.ID, self.idfactuacion)

    def get_ccfacturacion (self):
        return self.driver.find_element(By.NAME, self.ccfacturacion)
    
    def get_rzfacturacion (self):
        return self.driver.find_element(By.NAME, self.rzfacturacion)

    def get_departamento_facturacion (self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.departamento_facturacion)))

    def get_municipio_facturacion (self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.municipio_facturacion)))

    def get_direccion_facturacion (self):
        return self.driver.find_element(By.NAME, self.direccion_facturacion)

    def get_telefono_factura (self):
        return self.driver.find_element(By.NAME, self.telefono_factura)
    
    def get_correo_factura (self):
        return self.driver.find_element(By.NAME, self.correo_factura)
    
    def get_archivo_cc (self):
        return self.driver.find_element(By.ID, self.archivo_cc)
    
    def get_siguiente_registro (self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, self.siguiente_registro)))
    
    def tipo_cer (self):
        self.get_tipocert().click()
    
    def datos_PN (self,identificacion,fecha_exp,nombre,apellido,departamento
                       ,municipio,direccion,correo_titular,telefono,celular):
        
        self.get_identificacion().clear()
        self.get_nombre().clear()
        self.get_apellido().clear()
        self.get_correo_titular().clear()
        self.get_celular().clear()
        self.get_identificacion().send_keys(identificacion)
        self.get_fecha_exp().send_keys(fecha_exp)
        self.get_nombre().send_keys(nombre)
        self.get_apellido().send_keys(apellido)
        self.get_departamento().send_keys(departamento)
        self.get_municipio().send_keys(municipio)
        self.get_direccion().send_keys(direccion)
        self.get_correo_titular().send_keys(correo_titular)
        self.get_telefono().send_keys(telefono)
        self.get_celular().send_keys(celular)

    def otros_PN (self, plataforma, referido): 
        
        fecha_actual = datetime.datetime.now()
        fecha_hoy = fecha_actual.strftime("%d-%m")
        self.get_vigencia().send_keys(fecha_hoy)
        self.get_plataforma().send_keys(plataforma)
        self.get_referido().send_keys(referido)

    def facturacion_PN (self,idfactuacion,ccfacturacion,rzfacturacion,departamento_facturacion,municipio_facturacion
                       ,direccion_facturacion,telefono_factura,correo_factura):
        
        self.get_idfactuacion().send_keys(idfactuacion)
        self.get_ccfacturacion().clear()
        self.get_ccfacturacion().send_keys(ccfacturacion)
        self.get_rzfacturacion().clear()
        self.get_rzfacturacion().send_keys(rzfacturacion)
        self.get_departamento_facturacion().send_keys(departamento_facturacion)
        self.get_municipio_facturacion().send_keys(municipio_facturacion)
        self.get_direccion_facturacion().send_keys(direccion_facturacion)
        self.get_telefono_factura().clear()
        self.get_telefono_factura().send_keys(telefono_factura)
        self.get_correo_factura().clear()
        self.get_correo_factura().send_keys(correo_factura)

    def doc_PN (self, archivo_cc):    
        
        self.get_archivo_cc().send_keys(archivo_cc)
        self.get_siguiente_registro().click()









        


            