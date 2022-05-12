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
shop = driver.find_element_by_link_text("Shop").click()
android = driver.find_element_by_xpath("//*[@id='content']/ul/li[1]/a[1]/h3").click()
old_price = driver.find_element_by_xpath("//*[@id='product-169']/div[2]/div[1]/p/del/span").text
assert old_price == "₹600.00"
new_price = driver.find_element_by_xpath("//*[@id='product-169']/div[2]/div[1]/p/ins/span").text
assert new_price == "₹450.00"
pic = driver.find_element_by_xpath("//*[@id='product-169']/div[1]/a").click()
close_btn = driver.find_element_by_class_name("pp_close")
close_btn_enable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
