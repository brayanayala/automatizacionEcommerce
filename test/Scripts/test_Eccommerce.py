import time
import unittest
from openpyxl import load_workbook
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.Fe_Persona_Juridica import FePersonaJuridica
from src.PageObject.Pages.login_politicas_detalles_cert import Login, Politicas, Detalles_Cert
from src.PageObject.Pages.Fe_Persona_Natural import FePersonaNatural
from src.PageObject.Pages.Persona_Natural_RUT import PersonaNaturalRUT
from src.PageObject.Pages.Persona_Natural import PersonaNatural
from src.PageObject.Pages.Persona_Juridica import PersonaJuridica
from src.PageObject.Pages.Profesional_Titulado import Profesional_Titulado
from src.PageObject.Pages.Comunidad_Academica import Comunidad_Academica
from src.PageObject.Pages.Funcion_Publica import Funcion_Publica
from src.PageObject.Pages.Funcion_publica_SIFF import Funcion_Publica_SIFF
from src.PageObject.Pages.Representante_Legal import Representante_Legal
from src.PageObject.Pages.Pertenencia_Empresa import Pertenencia_Empresa

data = load_workbook('C:/Users/felipe.ayala/OneDrive - ANDES SERVICIO DE CERTIFICACION DIGITAL S A/Documentos/QA/Automatizacion/POM_copia/Generador_de_datos.xlsx', data_only=True)
hoja2 = data['Nombres']
identificacion = hoja2['C1'].value
nombre = hoja2['A1'].value
apellido = hoja2['B1'].value
tipo_id = hoja2['G2'].value
fecha_doc = hoja2['G3'].value
departamento = hoja2['G4'].value
ciudad = hoja2['G5'].value
direccion = hoja2['G6'].value
correo = hoja2['G7'].value
telefono = hoja2['G8'].value
celular = hoja2['G9'].value
nit = hoja2['I2'].value
empresa = hoja2['I3'].value
cargo = hoja2['I4'].value
unidadO = hoja2['I5'].value
sucursal = hoja2['I6'].value
dominio = hoja2['K2'].value
ent_dominio = hoja2['K3'].value
area = hoja2['K4'].value
provincia = hoja2['K5'].value
plataforma = hoja2['M2'].value
referido = hoja2['M3'].value
universidad = hoja2['O2'].value
titulo = hoja2['O3'].value
facultad = hoja2['O4'].value
matricula = hoja2['O5'].value
emisor_t = hoja2['O6'].value
doc_CEDULA = hoja2['Q2'].value
doc_RUT = hoja2['Q3'].value
doc_CYC = hoja2['Q4'].value
doc_tajeta_p = hoja2['Q5'].value
doc_Vinculacion_E = hoja2['Q6'].value
usuario = hoja2['A1048576'].value
password = hoja2['B1048576'].value

class TestEcommerce(WebDriverSetup):

    def test_Facturacion_Electronica_PJ(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = FePersonaJuridica(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_pkcs10("123456")
        tipo_cert.datos_Fe_Pj(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_Fe_Pj(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO, sucursal)
        csr = (dominio, ent_dominio, area, correo, provincia, ciudad)
        tipo_cert.otros_Fe_Pj(plataforma, referido , csr)
        tipo_cert.facturacion_Fe_Pj(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_Fe_Pj(doc_CYC, doc_RUT, doc_CEDULA)

        time.sleep(3)

    def test_Facturacion_Electronica_PN(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = FePersonaNatural(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)

        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_pkcs10("123456")
        tipo_cert.datos_Fe_PN(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        csr = (dominio, ent_dominio, area, correo, provincia, ciudad)
        tipo_cert.otros_Fe_PN(plataforma, referido , csr)
        tipo_cert.facturacion_Fe_PN(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_Fe_PN(doc_RUT, doc_CEDULA)

    def test_Persona_Natural_RUT(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = PersonaNaturalRUT(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)

        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_PN_RUT(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.otros_PN_RUT(plataforma, referido)
        tipo_cert.facturacion_PN_RUT(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_PN_RUT(doc_RUT, doc_CEDULA)    

    def test_Persona_Natural(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        tipo_cert = PersonaNatural(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        pagina_inicio_sesion = Login(driver)

        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_PN(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.otros_PN(plataforma, referido)
        tipo_cert.facturacion_PN(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_PN(doc_CEDULA) 

    def test_Persona_Juridica(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = PersonaJuridica(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)

        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_pkcs10("123456")
        tipo_cert.datos_Pj(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_Pj(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        csr = (dominio, ent_dominio, area, correo, provincia, ciudad)
        tipo_cert.otros_Pj(plataforma, referido , csr)
        tipo_cert.facturacion_Pj(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_Pj(doc_CYC, doc_RUT, doc_CEDULA)        
    
    def test_Profesional_Titulado(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Profesional_Titulado(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)

        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_PT(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_Personales_PT(departamento, ciudad, universidad, titulo, facultad, matricula, emisor_t)
        tipo_cert.otros_PT(plataforma, referido)
        tipo_cert.facturacion_PT(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_PT(doc_tajeta_p, doc_CEDULA) 

    def test_Comunidad_Academica(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Comunidad_Academica(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_CA(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_CA(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        tipo_cert.otros_CA(plataforma, referido)
        tipo_cert.facturacion_CA(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_CA(doc_Vinculacion_E, doc_RUT, doc_CEDULA)

    def test_Funcion_Publica(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Funcion_Publica(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_FP(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_FP(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        tipo_cert.otros_FP(plataforma, referido)
        tipo_cert.facturacion_FP(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_FP(doc_Vinculacion_E, doc_RUT, doc_CEDULA)

    def test_Funcion_Publica_SIFF(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Funcion_Publica_SIFF(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_FP(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_FP(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        tipo_cert.otros_FP(plataforma, referido)
        tipo_cert.facturacion_FP(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_FP(doc_Vinculacion_E, doc_RUT, doc_CEDULA)

    def test_Representante_Legal(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Representante_Legal(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_RL(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_RL(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        tipo_cert.otros_RL(plataforma, referido)
        tipo_cert.facturacion_RL(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_RL(doc_Vinculacion_E, doc_RUT, doc_CEDULA)     

    def test_Pertenencia_Empresa(self):

        driver = self.driver
        driver.get(Login.get_base_url())
        pagina_inicio_sesion = Login(driver)
        tipo_cert = Pertenencia_Empresa(driver)
        politicas = Politicas(driver)
        detalles_cert = Detalles_Cert(driver)
        
        pagina_inicio_sesion.inicio_Sesion(usuario, password)
        pagina_inicio_sesion.click_inicio()
        tipo_cert.tipo_cer()
        politicas.politicas()
        detalles_cert.detalle_cert_token_virtual("123456")
        tipo_cert.datos_PE(identificacion, fecha_doc, nombre, apellido, departamento, ciudad, direccion, correo, telefono, celular)
        tipo_cert.datos_ent_PE(nit, empresa, departamento, ciudad, direccion, correo, cargo, unidadO)
        tipo_cert.otros_PE(plataforma, referido)
        tipo_cert.facturacion_PE(tipo_id, identificacion, empresa, departamento, ciudad, direccion, celular, correo)
        tipo_cert.doc_PE(doc_Vinculacion_E, doc_RUT, doc_CEDULA)        


if __name__ == "__main__":
    unittest.main()


