# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = setup()

    title = driver.title
    assert title == "Web form"
    # assert 是一个内置的关键字，用于断言某个条件是真的。如果条件为真，则程序继续执行；如果条件为假，则程序抛出一个 AssertionError 异常。assert 通常用于调试阶段，确保代码中的某些条件一定为真，或者在单元测试中验证测试用例的预期结果。
    # assert 语句的基本语法如下：
    # assert 条件, "可选的错误信息"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

def teardown(driver):
    driver.quit()

# 执行
test_eight_components()