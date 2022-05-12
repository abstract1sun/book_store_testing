from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
shop = driver.find_element_by_link_text("Shop").click()
sorting_value = driver.find_element_by_css_selector("[value='menu_order']")
sorting_text = sorting_value.text
assert sorting_text == "Default sorting"
sorting_price = Select(driver.find_element_by_class_name("orderby"))
sorting_price.select_by_visible_text("Sort by price: high to low")
sorting_new = driver.find_element_by_class_name("orderby")
sorting_value_new = driver.find_element_by_css_selector("[value='price-desc']")
sorting_text_new = sorting_value_new.text
assert sorting_text_new == "Sort by price: high to low"
close_btn = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))