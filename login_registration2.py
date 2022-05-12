from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
my_account = driver.find_element_by_link_text("My Account").click()
username2 = driver.find_element_by_id("username").send_keys("y@y.ru")
password2 = driver.find_element_by_id("password").send_keys("qwiecksawrqwr123451561")
login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
knopka_logout = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
if knopka_logout is True:
    print("кнопка логаут присутствует")
