from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('http://localhost:5000/examples/1')

my_el = driver.find_element(By.ID,'btn')
my_el.click()

com_el = driver.find_element(By.ID,'title')
print(com_el.text) # dosen't show complete message so we need to use explicit wait