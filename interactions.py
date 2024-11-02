import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
print('success open selenium official')

# 1 点击
# Click on the element
driver.find_element(By.NAME, "color_input").click()


# 2 发送键位
# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()
# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev")


# 3 清除
# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
# Clear field to emtpy it from any previous data
driver.find_element(By.NAME, "email_input").clear()

# 4 提交
# 在Selenium 4中, 不再通过单独的端点以及脚本执行的方法来实现. 因此, 建议不要使用此方法, 而是单击相应的表单提交按钮.

time.sleep(3000)
driver.close()