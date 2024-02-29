from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://baidu.com")
# driver.find_element("id","xx").send_keys("ss")