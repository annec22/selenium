from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://google.com")

element = driver.find_element_by_name('q')
element.click()
element.send_keys("Hello WebDriver!")
element.submit()

driver.quit()
