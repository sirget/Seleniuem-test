from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')

driver.get("https://thaipcmarket.web.app/")
# driver.get("https://thaipcmarket.web.app/cpu")

# get อาจมีปัญหาถ้าใช้ AJAX มากเกินไป

print(driver.title)


def findbyclassname():
    login = driver.find_element_by_class_name("authBut")
    login.send_keys(Keys.RETURN)


def findbylinktext():
    regis = driver.find_element_by_link_text("สมัครสมาชิก")
    regis.send_keys(Keys.RETURN)


def fillinform():
    email = driver.find_element_by_name('email')
    email.send_keys('test@test.com')
    passw = driver.find_element_by_name('password')
    passw.send_keys('test@test.com')


def selectwithSelect():
    select = Select(driver.find_element_by_name('type'))
    select.select_by_visible_text('New')  # เลือกด้วย text
    select.select_by_index(2)  # เลือกด้วยลำดับ
    select.select_by_value()  # เลือกด้วยค่า value
    all_select_op = select.all_selected_options  # หาค่าที่เลือกอยู่
    print(all_select_op[0].get_attribute('value'))
    op = select.options  # หา option ทั้งหมด
    print(op[2].get_attribute('value'))


def select():
    element = driver.find_element_by_xpath("//select[@name = 'type']")
    all_op = element.find_elements_by_tag_name("option")
    for op in all_op:
        if op.get_attribute('value') == 'New':
            op.click()

        print(op.get_attribute('value'))


def intoalert():
    alert = driver.switch_to.alert  # เข้าไปใน alert


def drugdrop():
    ele = ''  # ของที่จะเอาไปใส่
    tar = ''  # ที่ ๆ จะเอาไปวาง
    ac_chain = ActionChains(driver)
    ac_chain.drag_and_drop(ele, tar).perform()


def location():
    driver.forward()  # ไปหน้า
    driver.back()  # กลับหลัง


def cookies():
    cookies = {'name': 'foo'}
    driver.add_cookie(cookies)
    driver.get_cookies()  # all cookie


# findbyclassname()
# findbylinktext()
# select()
# selectwithSelect()

print(driver.current_url)
