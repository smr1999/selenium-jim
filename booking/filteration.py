from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookFilteration:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def filter_stars(self,*star_vals):
        star_filter_elm_parent = 'div[data-filters-group="class"]'
        
        star_filter_elms = self.driver.find_element(By.CSS_SELECTOR,star_filter_elm_parent).find_elements(By.CSS_SELECTOR,'*')

        for star_val in star_vals:
            for elm in star_filter_elms:
                if elm.get_attribute('innerHTML').strip() == f'{star_val} stars':
                    elm.click()

    def sort_lowest_price(self):
        try:
            sort_elm = 'button[data-testid="sorters-dropdown-trigger"]'
            self.driver.find_element(By.CSS_SELECTOR,sort_elm).click()
            
            lowest_price_elm = 'button[data-id="price"]'
            self.driver.find_element(By.CSS_SELECTOR,lowest_price_elm).click()
        except Exception:
            print('can not find sort lowest item')