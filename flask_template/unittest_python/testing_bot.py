
import selenium as se
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time
import os
sys.path.append('/Users/luistoribio/Documents/curso_python_avanzado/sesion_11_python_avanzado/flask_template')


class TestingBot():
    
    def __init__(self,url_web):
        print("My class")
        self.browser = self.webdriver_firefox()
        self.browser.get(url_web)
        
    def webdriver_firefox(self):
        browser = webdriver.Firefox()
        return  browser
    
    def webdriver_chrome(self):
        browser = webdriver.Chrome()
        return browser
    
    
    def click_by_id(self,element_id):
        try:
            text_element = self.browser.find_element(By.ID, element_id).click()
            print(text_element)
        except:
            print("")
        else:
            return "[SUCCESFULL]"
            
    def find_by_id(self,url_web,element_id):
        try:
            self.browser.get(url_web)
            element_displyed = self.browser.find_element(By.ID, element_id).is_displayed
            print(element_displyed)
        except Exception as e:
            print("[ERROR] ", e)
        else:
            return element_displyed
            
    def send_value_xpath(self,xpath,value):
        try:
            element_displyed = self.browser.find_element(By.XPATH, xpath).send_keys(value)
            print(element_displyed)
        except:
            print("[ERRO] ")
        else:
            return "[SUCCESFULL]"
            
    
    def login_user(self,xpath_user,xpath_password,element_id):
        user = "standard_user"
        passowrd = "secret_sauce"
        list_returns = []
        list_returns.append(self.send_value_xpath(xpath_user,user))
        list_returns.append(self.send_value_xpath(xpath_password,passowrd))
        list_returns.append(self.click_by_id(element_id))
        
        return list_returns
    
    def close_browser(self):
        self.browser.quit()
        
if __name__ == '__main__':
    obj = TestingBot("https://www.saucedemo.com/")
    
    obj.login_user("//input[@id='user-name']","//input[@id='password']","login-button")
    obj.close_browser()
    
    
    
    
    
    