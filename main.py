from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('http://localhost:5000/examples/1')

my_el = driver.find_element(By.ID,'btn')
my_el.click()

my_el = driver.find_element(By.ID,'title')
print(my_el.text)

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element(
        (By.ID,'title'),
        'Completed'
    )
)

print(my_el.text)