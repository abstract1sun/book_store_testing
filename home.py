from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3").click()
reviews = driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a").click()
five = driver.find_element_by_class_name("star-5").click()
obzor = driver.find_element_by_id("comment")
obzor.send_keys("Good, good Book!")
imya = driver.find_element_by_id("author")
imya.send_keys("Dimka")
email = driver.find_element_by_id("email")
email.send_keys("a@b.ru")
submit = driver.find_element_by_id("submit").click()


