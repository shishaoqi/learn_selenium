# https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.使用驱动实例开启会话
driver = webdriver.Chrome()



# 2.在浏览器上执行操作
# 本例，我们导航到一个网页
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


# 3. 请求 浏览器信息
# 您可以请求一系列关于浏览器的信息 , 包括窗口句柄、浏览器尺寸/位置、cookie、警报等.
title = driver.title


# 4. 建立等待策略
# 将代码与浏览器的当前状态同步 是Selenium面临的最大挑战之一, 做好它是一个高级主题.

# 基本上, 您希望: 1.在尝试定位元素之前, 确保该元素位于页面上,
#                2.在尝试与该元素交互之前, 该元素处于可交互状态.

# 隐式等待很少是最好的解决方案, 但在这里最容易演示, 所以我们将使用它作为占位符.
# 阅读更多关于 等待策略(https://www.selenium.dev/zh-cn/documentation/webdriver/waits) 的信息.
driver.implicitly_wait(0.5)


# 5. 发送命令 查找元素
# 大多数Selenium会话中的主要命令都与元素相关, 如果不先找到元素, 就无法与之交互.
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 6. 操作元素
# 对于一个元素, 只有少数几个操作可以执行, 但您将经常使用它们.
text_box.send_keys("Selenium")
submit_button.click()

# 7. 获取元素信息
# 元素存储了很多被请求的信息.
message = driver.find_element(by=By.ID, value="message")
text = message.text


# 8. 结束会话
# 这将结束驱动程序进程, 默认情况下, 该进程也会关闭浏览器. 无法向此驱动程序实例发送更多命令.
driver.quit()