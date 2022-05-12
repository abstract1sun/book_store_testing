from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
kniga = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[1]/h3").click()
zagolovok = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-181 > div.summary.entry-summary > h1"), "HTML5 Forms"))
if zagolovok is True:
    print("название книги HTML5 Forms")
