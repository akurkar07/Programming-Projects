from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.edge.service import Service
s=Service("C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedgedev.exe")
#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Edge(s) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://bing.com")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent"))