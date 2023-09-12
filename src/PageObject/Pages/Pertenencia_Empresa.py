import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
       
class Pertenencia_Empresa:
    def __init__(self, driver):
        self.driver = driver
        self.tipocert = ".col-md-3:nth-child(11) > .btn"
        self.identificacion = "pregunta_289"
        self.fecha_exp = "290"
        self.nombre = "pregunta_291"
        self.apellido = "pregunta_292"
        self.departamento = "293"
        self.municipio = "294"
        self.direccion = "pregunta_295"
        self.correo_titular = "pregunta_296"
        self.telefono = "pregunta_297"
        self.celular = "pregunta_298"
        self.nit = "pregunta_299"
        self.razonsocial = "pregunta_300"
        self.departamento_entidad = "301"
        self.municipio_entidad = "302"
        self.direccion_entidad = "pregunta_303"
        self.correo_ent = "pregunta_304"
        self.cargo = "pregunta_305"
        self.organizacional = "pregunta_306"
        self.vigencia = "309"
        self.plataforma = "310"
        self.referido = "311"
        self.idfactuacion = "312"
        self.ccfacturacion = "pregunta_313"
        self.rzfacturacion = "pregunta_314"
        self.departamento_facturacion = "315"
        self.municipio_facturacion = "316"
        self.direccion_facturacion = "pregunta_317"
        self.telefono_factura = "pregunta_318"
        self.correo_factura = "pregunta_409"
        self.archivo_vinculacion = "documento_4"
        self.archivo_rut = "documento_12"
        self.archivo_cc = "documento_2"
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

    def get_nit (self):
        return self.driver.find_element(By.NAME, self.nit)

    def get_razonsocial (self):
        return self.driver.find_element(By.NAME, self.razonsocial)

    def get_departamento_entidad(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.departamento_entidad)))

    def get_municipio_entidad(self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ID, self.municipio_entidad)))

    def get_direccion_entidad (self):
        return self.driver.find_element(By.NAME, self.direccion_entidad)

    def get_correo_ent (self):
        return self.driver.find_element(By.NAME, self.correo_ent)
    
    def get_cargo (self):
        return self.driver.find_element(By.NAME, self.cargo)
    
    def get_organizacional (self):
        return self.driver.find_element(By.NAME, self.organizacional)
    
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
    
    def get_archivo_vinculacion (self):
        return self.driver.find_element(By.ID, self.archivo_vinculacion)
    
    def get_archivo_rut (self):
        return self.driver.find_element(By.ID, self.archivo_rut)
    
    def get_archivo_cc (self):
        return self.driver.find_element(By.ID, self.archivo_cc)
    
    def get_siguiente_registro (self):
        return WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, self.siguiente_registro)))
    
    def tipo_cer (self):
        self.get_tipocert().click()
    
    def datos_PE (self,identificacion,fecha_exp,nombre,apellido,departamento
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

    def datos_ent_PE (self, nit,razonsocial,departamento_entidad,municipio_entidad,direccion_entidad,correo_ent,cargo
                       ,organizacional):

        self.get_nit().send_keys(nit)
        self.get_razonsocial().send_keys(razonsocial)
        self.get_departamento_entidad().send_keys(departamento_entidad)
        self.get_municipio_entidad().send_keys(municipio_entidad)
        self.get_direccion_entidad().send_keys(direccion_entidad)
        self.get_correo_ent().send_keys(correo_ent)
        self.get_cargo().send_keys(cargo)
        self.get_organizacional().send_keys(organizacional)

    def otros_PE (self, plataforma, referido): 
        
        fecha_actual = datetime.datetime.now()
        fecha_hoy = fecha_actual.strftime("%d-%m")
        self.get_vigencia().send_keys(fecha_hoy)
        self.get_plataforma().send_keys(plataforma)
        self.get_referido().send_keys(referido)

    def facturacion_PE (self,idfactuacion,ccfacturacion,rzfacturacion,departamento_facturacion,municipio_facturacion
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

    def doc_PE (self, archivo_vinculacion,archivo_rut,archivo_cc):    
        
        self.get_archivo_vinculacion().send_keys(archivo_vinculacion)
        self.get_archivo_rut().send_keys(archivo_rut)
        self.get_archivo_cc().send_keys(archivo_cc)
        self.get_siguiente_registro().click()









        


            