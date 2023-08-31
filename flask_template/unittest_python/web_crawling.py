
import selenium as se
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time
import os
sys.path.append('/Users/luistoribio/Documents/curso_python_avanzado/sesion_11_python_avanzado/flask_template')
from app.db.mongodb import MongoDB as mongo
from app.utils.utils import Utils as utils



class WebCrawling(mongo,utils):
    def __init__(self):
        print("My class")
        
    def webdriver_firefox(self):
        browser = webdriver.Firefox()
        
        return browser
            
    def find_id(self,url_web,element_id):
        try:
            browser = self.webdriver_firefox()
            browser.get(url_web)
            text_element = browser.find_element(By.ID, element_id).text
            print(text_element)
            
        except:
            print("")
        else:
            return text_element
        finally:
            self.close_browser(browser)
            
        
    def find_xpath(self,url_web,element_xpath):
        try:
            browser = self.webdriver_firefox()
            browser.get(url_web)
            #"//div[@class='wpb_wrapper']/p[2]"
            text_element = browser.find_element("xpath", element_xpath).text
            print(text_element)
        except:
            print("")
        else:
            return text_element
        finally:
            self.close_browser(browser)
            
    def click_button_by_xpath(self,url_web,element_id):
        try:
            browser = self.webdriver_firefox()
            browser.get(url_web)
            #"//a[@href='/users/sign_up?ref=guide-selenium-webdriver-tutorial-top&product=automate']"
            text_element = browser.find_element("xpath", "//div[@class='wpb_wrapper']/p/a[@href='https://www.browserstack.com/users/sign_up']").click()
            print(text_element)
        
        except Exception as e:
            browser.find_element(By.ID, 'accept-cookie-notification-cross').click()
            text_element = browser.find_element("xpath", "//div[@class='wpb_wrapper']/p/a[@href='https://www.browserstack.com/users/sign_up']").click()
            print("[ERROR]: COOKIES")
        else:
            return text_element
        finally:
            time.sleep(2)
            self.close_browser(browser)
            
    def screen_shoot(self,url_web,folder_name):
        try:
            self.create_folder(os.environ['SELENIUM_PATH'],folder_name)
            browser = self.webdriver_firefox()
            browser.get(url_web)
            height = browser.execute_script('return document.documentElement.scrollHeight')
            width  = browser.execute_script('return document.documentElement.scrollWidth')
            browser.set_window_size(width, height)  # the trick
            print("width",width)
            print("height",height)
            for interval in range(0,height,500):
                browser.execute_script("window.scrollTo(0,"+str(interval)+")")
                browser.save_screenshot(os.environ['SELENIUM_PATH']+"/"+folder_name+"/scrape_"+str(interval)+".png")
        except Exception as e:
            print("[ERROR]: COOKIES")
        else:
            return "Completed"
        finally:
            time.sleep(2)
            self.close_browser(browser)
            
    def get_all_text(self,url_web):
        try:
            browser = self.webdriver_firefox()
            browser.get(url_web)
            text_element = browser.find_element(By.XPATH, "/html/body").text
        except Exception as e:
            print("[ERROR]: COOKIES")
        else:
            document = {"web_url": url_web, "website_text":text_element }
            self.insert_one_document(document)
            return "Completed"
        finally:
            time.sleep(2)
            self.close_browser(browser)
        
    def close_browser(self,browser):
        browser.quit()


if __name__ == '__main__':
    obj = WebCrawling()
    
    #obj.find_id("https://www.browserstack.com/guide/selenium-webdriver-tutorial",'toc0')
    #obj.click_button_by_xpath("https://www.browserstack.com/guide/selenium-webdriver-tutorial",'')
    #obj.screen_shoot("https://www.browserstack.com/guide/selenium-webdriver-tutorial","browserstack")
    obj.get_all_text("https://www.browserstack.com/guide/selenium-webdriver-tutorial")