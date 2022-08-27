from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.implicitly_wait(5)

driver.get('localhost:5000/examples/2')

sum1 = driver.find_element(By.ID,'sum1')
sum1.send_keys(15)

sum2 = driver.find_element(By.ID,'sum2')
# sum2.send_keys(30)
sum2.send_keys(Keys.NUMPAD3,Keys.NUMPAD0)

btn = driver.find_element(By.CSS_SELECTOR,'button[onclick="return total()"]')
btn.click()
# https://www.w3schools.com/cssref/css_selectors.asp -> css selectors

result = driver.find_element(By.ID,'displayvalue')
print(result.text)