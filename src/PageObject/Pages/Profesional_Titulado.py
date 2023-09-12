import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
       
class Profesional_Titulado:
    def __init__(self, driver):
        self.driver = driver
        self.tipocert = ".col-md-3:nth-child(6) > .btn"
        self.identificacion = "pregunta_411"
        self.fecha_exp = "412"
        self.nombre = "pregunta_134"
        self.apellido = "pregunta_135"
        self.departamento = "136"
        self.municipio = "137"
        self.direccion = "pregunta_138"
        self.correo_titular = "pregunta_139"
        self.telefono = "pregunta_140"
        self.celular = "pregunta_141"
        self.departamento_U = "142"
        self.municipio_U = "143"
        self.universidad = "144"
        self.titulo = "145"
        self.facultad = "pregunta_146" 
        self.matricula_P = "pregunta_147" 
        self.emisor_T = "pregunta_148"
        self.vigencia = "150"
        self.plataforma = "151"
        self.referido = "152"
        self.idfactuacion = "153"
        self.ccfacturacion = "pregunta_154"
        self.rzfacturacion = "pregunta_155"
        self.departamento_facturacion = "156"
        self.municipio_facturacion = "157"
        self.direccion_facturacion = "pregunta_158"
        self.telefono_factura = "pregunta_159"
        self.correo_factura = "pregunta_160"
        self.archivo_cc = "documento_11"
        self.tarjeta_P = "documento_2"
        self.siguiente_registro = ".flex-stack > div:nth-child(2)"



    def get_tipocert(self):
        return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, self.tipocert)))
    
    def get_identificacion (self):
        return self.driver.find_element(By.NAME, self.identificacion)
    
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
    
    def get_departamento_U(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.departamento_U)))

    def get_municipio_U(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.municipio_U)))
    
    def get_universidad(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.universidad)))

    def get_titulo(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.titulo)))
    
    def get_facultad (self):
        return self.driver.find_element(By.NAME, self.facultad)

    def get_matricula_P (self):
        return self.driver.find_element(By.NAME, self.matricula_P)
    
    def get_emisor_T (self):
        return self.driver.find_element(By.NAME, self.emisor_T)
    
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
    
    def get_tarjeta_P (self):
        return self.driver.find_element(By.ID, self.tarjeta_P)
    
    def get_siguiente_registro (self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, self.siguiente_registro)))
    
    def tipo_cer (self):
        self.get_tipocert().click()
    
    def datos_PT (self,identificacion,fecha_exp,nombre,apellido,departamento
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

    def datos_Personales_PT (self,departamento_U,municipio_U,universidad,titulo,facultad
                       ,matricula_P,emisor_T):
        
        self.get_departamento_U().send_keys(departamento_U)
        self.get_municipio_U().send_keys(municipio_U)
        self.get_universidad().send_keys(universidad)
        self.get_titulo().send_keys(titulo)
        self.get_facultad().send_keys(facultad)   
        self.get_matricula_P().send_keys(matricula_P)
        self.get_emisor_T().send_keys(emisor_T) 

    def otros_PT (self, plataforma, referido): 
        
        fecha_actual = datetime.datetime.now()
        fecha_hoy = fecha_actual.strftime("%d-%m")
        self.get_vigencia().send_keys(fecha_hoy)
        self.get_plataforma().send_keys(plataforma)
        self.get_referido().send_keys(referido)

    def facturacion_PT (self,idfactuacion,ccfacturacion,rzfacturacion,departamento_facturacion,municipio_facturacion
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

    def doc_PT (self, doc_tajeta_p, archivo_cc):    
        
        self.get_tarjeta_P().send_keys(doc_tajeta_p)
        self.get_archivo_cc().send_keys(archivo_cc)
        self.get_siguiente_registro().click()









        


            