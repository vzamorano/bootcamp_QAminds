import time 
import copy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import csv

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains #Libreria para uso de perifericos (mouse, teclado)


# LOCATOR
from Locators.Locators import MyLocators

class TC_1():

    def __init__(self, driver):
        self.driver = driver
        self.xPath_Popup = MyLocators.xPath_Popup
        self.xPath_Directorio = MyLocators.xPath_Directorio
        self.linkText_Proveedores = MyLocators.linkText_Proveedores
        self.xPath_Prov_Abrasivos = MyLocators.xPath_Prov_Abrasivos
        self.cssSelector_Elementos = MyLocators.cssSelector_Elementos
        self.xPath_Frismex = MyLocators.xPath_Frismex
        self.xPath_Boton_Abrasivos = MyLocators.xPath_Boton_Abrasivos
        self.xPath_JC = MyLocators.xPath_JC
        self.xPath_MG = MyLocators.xPath_MG
        self.xPath_Prov_Aceites_Lub = MyLocators.xPath_Prov_Aceites_Lub
        self.xPath_Adibaja = MyLocators.xPath_Adibaja
        self.xPath_Boton_Aceites_Lub = MyLocators.xPath_Boton_Aceites_Lub
        self.xPath_Chevrolet_Tijuana = MyLocators.xPath_Chevrolet_Tijuana
        self.xPath_Lubricantes_Akron = MyLocators.xPath_Lubricantes_Akron
        self.xPath_Prov_Aceros_Met = MyLocators.xPath_Prov_Aceros_Met
        self.xPath_Airpipe = MyLocators.xPath_Airpipe
        self.xPath_Boton_Aceros_Met = MyLocators.xPath_Boton_Aceros_Met
        self.xPath_Buy_Metals = MyLocators.xPath_Buy_Metals
        self.xPath_CD_Metales = MyLocators.xPath_CD_Metales
        self.xPath_Prov_Aire_Refri = MyLocators.xPath_Prov_Aire_Refri
        self.xPath_Aislantes = MyLocators.xPath_Aislantes
        self.xPath_Boton_Aire_Refri = MyLocators.xPath_Boton_Aire_Refri
        self.xPath_AQS_Ind = MyLocators.xPath_AQS_Ind
        self.xPath_Aro_Construcciones = MyLocators.xPath_Aro_Construcciones
        self.xPath_Art_Promocionales = MyLocators.xPath_Art_Promocionales
        self.xPath_Arma_Promo = MyLocators.xPath_Arma_Promo
        self.xPath_Boton_Art_Promocionales = MyLocators.xPath_Boton_Art_Promocionales
        self.xPath_Conceptos_Graf = MyLocators.xPath_Conceptos_Graf
        self.xPath_Malka_Impre = MyLocators.xPath_Malka_Impre
        self.xPath_Asesoria_Cons = MyLocators.xPath_Asesoria_Cons
        self.xPath_Adalid = MyLocators.xPath_Adalid
        self.xPath_Boton_Asesoria_Cons = MyLocators.xPath_Boton_Asesoria_Cons
        self.xPath_Banuelos_Salazar = MyLocators.xPath_Banuelos_Salazar
        self.xPath_Conadin = MyLocators.xPath_Conadin
        self.xPath_Automatizacion = MyLocators.xPath_Automatizacion
        self.xPath_Advamex = MyLocators.xPath_Advamex
        self.xPath_Boton_Automatizacion = MyLocators.xPath_Boton_Automatizacion
        self.xPath_Auto_Zen = MyLocators.xPath_Auto_Zen
        self.xPath_Electrok = MyLocators.xPath_Electrok
        self.xPath_Baleros = MyLocators.xPath_Baleros
        self.xPath_Baleros_Refac_Tijuana = MyLocators.xPath_Baleros_Refac_Tijuana
        self.xPath_Bandas_Ind = MyLocators.xPath_Bandas_Ind
        self.xPath_Bandas_Refac_Tijuana = MyLocators.xPath_Bandas_Refac_Tijuana
        self.xPath_Basculas = MyLocators.xPath_Basculas
        self.xPath_Sipcons = MyLocators.xPath_Sipcons
        self.xPath_Cables_Arneses = MyLocators.xPath_Cables_Arneses
        self.xPath_Viakon = MyLocators.xPath_Viakon
        self.xPath_Calibracion = MyLocators.xPath_Calibracion
        self.xPath_Arrega_Ind = MyLocators.xPath_Arrega_Ind
        self.xPath_Boton_Calibracion = MyLocators.xPath_Boton_Calibracion
        self.xPath_Exis_Soluciones = MyLocators.xPath_Exis_Soluciones
        self.xPath_Hexagon = MyLocators.xPath_Hexagon
        self.xPath_Calzado_Seguridad = MyLocators.xPath_Calzado_Seguridad
        self.xPath_CC_Inter = MyLocators.xPath_CC_Inter
        self.xPath_Boton_Calzado_Seguridad = MyLocators.xPath_Boton_Calzado_Seguridad
        self.xPath_CE_HP = MyLocators.xPath_CE_HP
        self.xPath_Crisosa = MyLocators.xPath_Crisosa
        self.xPath_Capacitacion = MyLocators.xPath_Capacitacion
        self.xPath_Alfa_K9 = MyLocators.xPath_Alfa_K9
        self.xPath_Boton_Capacitacion = MyLocators.xPath_Boton_Capacitacion
        self.xPath_Alfa_Primeros_Auxilios = MyLocators.xPath_Alfa_Primeros_Auxilios
        self.xPath_Avancer = MyLocators.xPath_Avancer
        self.cssSelector_Elementos2 = MyLocators.cssSelector_Elementos2
        

    def start(self):
        #pass
        global info_a_guardar 
        info_a_guardar = []
        archivo_csv = 'proveedores.csv'
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
    
    #escritor_csv.writerow(['Columna1', 'Columna2'])  
    
    #Escribe los datos
        escritor_csv.writerows(info_a_guardar)

        print(f"Los datos se han escrito en {archivo_csv}")


    def Test_001(self):
        inicio_tiempo_prueba = time.time() # Se inicia el temporizador para el tiempo de la prueba
        self.driver.get(MyLocators.URL)        
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Para cerrar el popup emergente
        self.driver.find_element(By.XPATH, self.xPath_Popup).click()
        time.sleep(2)

        # Posicionarse sobre Directorio
        directorio = ActionChains(self.driver)
        find_directorio = self.driver.find_element(By.XPATH, self.xPath_Directorio)
        directorio.move_to_element(find_directorio).click().perform()
        time.sleep(2)

        # Redireccionamiento a Proveedores
        proveedores = ActionChains(self.driver)
        find_proveedores = self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores)
        proveedores.move_to_element(find_proveedores).click().perform()
        time.sleep(2)

        # Proveedor: Abrasivos
        self.driver.find_element(By.XPATH, MyLocators.xPath_Prov_Abrasivos).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Abrasivos: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Frismex).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Abrasivos).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_JC).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Abrasivos).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_MG).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            # Retornar a Proveedores
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Aceites y Lubricantes
        self.driver.find_element(By.XPATH, MyLocators.xPath_Prov_Aceites_Lub).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Aceites y Lubricantes: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Adibaja).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Aceites_Lub).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Chevrolet_Tijuana).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Aceites_Lub).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Lubricantes_Akron).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Aceros y Metales
        self.driver.find_element(By.XPATH, MyLocators.xPath_Prov_Aceros_Met).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos2)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Aceros y Metales: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Airpipe).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Aceros_Met).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Buy_Metals).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Aceros_Met).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_CD_Metales).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        
        # Proveedor: Aire Acond. y Refrigeración
        self.driver.find_element(By.XPATH, MyLocators.xPath_Prov_Aire_Refri).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos2)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Aire Acond. y Refrigeración: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Aislantes).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Aire_Refri).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_AQS_Ind).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Aire_Refri).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Aro_Construcciones).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Artículos Promocionales
        self.driver.find_element(By.XPATH, MyLocators.xPath_Art_Promocionales).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Artículos Promocionales: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Arma_Promo).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Art_Promocionales).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Conceptos_Graf).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Art_Promocionales).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Malka_Impre).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Asesoría y Consultoría
        self.driver.find_element(By.XPATH, MyLocators.xPath_Asesoria_Cons).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Asesoría y Consultoría: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Adalid).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Asesoria_Cons).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Banuelos_Salazar).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Asesoria_Cons).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Conadin).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Automatización
        self.driver.find_element(By.XPATH, MyLocators.xPath_Automatizacion).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Automatización: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Advamex).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Automatizacion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Auto_Zen).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Automatizacion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Electrok).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Baleros
        self.driver.find_element(By.XPATH, MyLocators.xPath_Baleros).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Baleros: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Baleros_Refac_Tijuana).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        
        # Proveedor: Bandas Industriales
        self.driver.find_element(By.XPATH, MyLocators.xPath_Bandas_Ind).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Bandas Industriales: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Bandas_Refac_Tijuana).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Básculas
        self.driver.find_element(By.XPATH, MyLocators.xPath_Basculas).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Básculas: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Sipcons).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Cables y Arneses
        self.driver.find_element(By.XPATH, MyLocators.xPath_Cables_Arneses).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Cables y Arneses: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Viakon).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Calibración, Equipos de Medición
        self.driver.find_element(By.XPATH, MyLocators.xPath_Calibracion).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos2)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Calibración, Equipos de Medición: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Arrega_Ind).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Calibracion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Exis_Soluciones).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Calibracion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Hexagon).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Calzado Industrial y Seguridad
        self.driver.find_element(By.XPATH, MyLocators.xPath_Calzado_Seguridad).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos2)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Calzado Industrial y Seguridad: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_CC_Inter).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Calzado_Seguridad).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_CE_HP).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Calzado_Seguridad).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Crisosa).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Proveedor: Capacitación
        self.driver.find_element(By.XPATH, MyLocators.xPath_Capacitacion).click()
        div_element = self.driver.find_element(By.CSS_SELECTOR, self.cssSelector_Elementos)
        elementos = div_element.find_elements(By.CSS_SELECTOR, 'div.row.raya')
        cantidad_elementos = len(elementos)
        print(f'Cantidad de proveedores de Capacitación: {cantidad_elementos}')
        if cantidad_elementos >= 3:
            self.driver.find_element(By.XPATH, MyLocators.xPath_Alfa_K9).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Boton_Capacitacion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Alfa_Primeros_Auxilios).click()
            self.driver.find_element(By.XPATH, self.xPath_Boton_Capacitacion).click()
            self.driver.find_element(By.XPATH, MyLocators.xPath_Avancer).click()
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()
        else:
            self.driver.find_element(By.LINK_TEXT, self.linkText_Proveedores).click()

        # Para calcular el tiempo de la prueba
        fin_tiempo_prueba = time.time() # Se finaliza con el temporizador del tiempo de la prueba
        tiempo_total_segundos = fin_tiempo_prueba - inicio_tiempo_prueba # Se calcula el tiempo transcurrido en segundos
        horas_prueba = int(tiempo_total_segundos // 3600) # Se convierte el tiempo total a horas
        minutos_prueba = int((tiempo_total_segundos % 3600) // 60) # Se convierte el tiempo total a minutos
        segundos_prueba = int(tiempo_total_segundos % 60) # Se convierte el tiempo total a segundos
        print(f'Tiempo transcurrido de la prueba: {horas_prueba:02d}:{minutos_prueba:02d}:{segundos_prueba:02d}')
      


    
      
        