from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
basket_add1 = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(2)
basket_add2 = driver.find_element_by_xpath("//*[@id='content']/ul/li[5]/a[2]").click()
price = driver.find_element_by_class_name("amount").click()
time.sleep(2)
remove = driver.find_element_by_class_name("remove").click()
time.sleep(2)
undo = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/div[1]/a").click()
js_qty = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
js_qty.clear()
js_qty.send_keys("3")
update = driver.find_element_by_name("update_cart").click()
kolvo = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input").get_attribute('value')
assert kolvo == "3"
time.sleep(5)
coupon = driver.find_element_by_name("apply_coupon").click()
message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
print(message)
