import random
from time import sleep
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "version": "77.0",
    "screenResolution": "1280x1024x24",
    "enableVNC": True,
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities
)

driver.maximize_window()

for i in range(10):
    driver.get("https://www.yandex.ru/")
    random.choice(driver.find_elements_by_tag_name("a")).click()

driver.close()
