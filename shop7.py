from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
basket_add = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(2)
cart = driver.find_element_by_class_name("amount").click()
proceed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-34']/div/div[1]/div/div/div/a"))).click()
first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_first_name"))).send_keys("Dimka")
last_name = driver.find_element_by_id("billing_last_name").send_keys("Dimkov")
email = driver.find_element_by_id("billing_email").send_keys("a@a.ru")
phone = driver.find_element_by_id("billing_phone").send_keys("+71234567890")
address = driver.find_element_by_id("billing_address_1").send_keys("fknstreet, 13")
city = driver.find_element_by_id("billing_city").send_keys("NSK")
state = driver.find_element_by_id("billing_state").send_keys("oblast")
postcode = driver.find_element_by_id("billing_postcode").send_keys("123456")
country = driver.find_element_by_id("s2id_billing_country").click()
country_enter = driver.find_element_by_id("s2id_autogen1_search").send_keys("Zimbabwe")
country_click = driver.find_element_by_class_name("select2-match").click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payment = driver.find_element_by_id("payment_method_cheque").click()
submit = driver.find_element_by_id("place_order").click()
thankyou = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))