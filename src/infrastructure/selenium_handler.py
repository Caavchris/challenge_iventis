from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumHandler:
    
    def __init__(self, headless=False):
        options = Options()
        
        if headless:
            options.add_argument('--headless=new')
        
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(15)
    
    def open_url(self, url):
        self.driver.get(url)
    
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    
    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
    
    def close(self):
        self.driver.close()
    
    def quit(self):
        self.driver.quit()