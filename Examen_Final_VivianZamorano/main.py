import time 
import unittest #pip install unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# LOCATORS
from Locators.Locators import MyLocators

# Test Cases
from TestCases.TC_1 import TC_1


class QAMinds(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("INICIO DE LA PRUEBA")
        miServicio = Service(MyLocators.Driver_Path) # Para llamar al elemento es: clase.elemento
        cls.driver = webdriver.Chrome(service = miServicio)
        time.sleep(5)

    def test_QAMinds(self):
        driver = self.driver
        tc_1 = TC_1(driver)
        tc_1.start()
        tc_1.Test_001()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("\nFIN DE LA PRUEBA")

if __name__ == '__main__':
    unittest.main()
    