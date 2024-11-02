import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.pingwest.com/')

print(driver.title)


news_list = driver.find_element(by=By.ID, value='J_newsListModule')
print(news_list)


print('success open pingwest')
time.sleep(3000)
driver.close()