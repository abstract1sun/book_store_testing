from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
my_account = driver.find_element_by_link_text("My Account").click()
username1 = driver.find_element_by_id("reg_email").send_keys("y@y.ru")
password1 = driver.find_element_by_id("reg_password").send_keys("qwiecksawrqwr123451561")
register = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]").click()
