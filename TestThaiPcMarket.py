from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("https://thaipcmarket.web.app/")

print(driver.title)


def findbyclassname():
    login = driver.find_element_by_class_name("authBut")
    login.send_keys(Keys.RETURN)


def findbylinktext():
    login = driver.find_element_by_link_text("สมัครสมาชิก")
    login.send_keys(Keys.RETURN)


# findbyclassname()
findbylinktext()

print(driver.current_url)
