from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
my_account = driver.find_element_by_link_text("My Account").click()
username2 = driver.find_element_by_id("username").send_keys("y@y.ru")
password2 = driver.find_element_by_id("password").send_keys("qwiecksawrqwr123451561")
login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
shop = driver.find_element_by_link_text("Shop").click()
html = driver.find_element_by_link_text("HTML").click()
count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
count_num = len(count)
if count_num == 3:
    print("Количество книг про HTML - три")
