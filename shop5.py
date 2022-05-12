from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
basket_add = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(5)
amount = driver.find_element_by_class_name("cartcontents").text
assert amount == "1 Item"
price = driver.find_element_by_class_name("amount")
assert price.text == "₹180.00"
price.click()
subtotal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[1]/td/span")))
subtotal_text = subtotal.text
assert subtotal_text == "₹180.00"
total = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span")))
total_text = total.text
assert total_text == "₹189.00"
