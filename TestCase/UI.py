from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


def input_demo(driver):
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.send_keys('Hello World! 你好')
    time.sleep(2)
    input_el.clear()
    time.sleep(2)


def id_demo1(driver):
    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/Administrator/Pictures/下午作业/work.png')
    time.sleep(2)
    file_el.clear()
    time.sleep(2)


def id_demo2(driver):
    radio_els = driver.find_elements_by_name('radio')
    radio_els[0].click()
    time.sleep(2)
    radio_els[1].click()
    time.sleep(2)


def class_demo(driver):
    class_name = driver.find_elements_by_class_name('checkbox')
    class_name[0].click()
    time.sleep(1)
    class_name[1].click()
    time.sleep(1)
    class_name[2].click()
    time.sleep(1)
    class_name[2].click()
    time.sleep(1)


def button_demo(driver):
    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    button_el.click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    # driver.switch_to.alert.dismiss()
    # time.sleep(1)


def pwd_demo(driver):
    pws_el = driver.find_element_by_xpath('//input[@type="password"]')
    time.sleep(2)
    pws_el.send_keys('123456')
    time.sleep(1)
    pws_el.clear()
    time.sleep(1)


def xiala_demo(driver):
    select_el = driver.find_element_by_css_selector(
        'body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    s = Select(select_el)
    s.select_by_index(1)
    time.sleep(1)
    s.select_by_value('z1')
    time.sleep(1)
    s.select_by_visible_text('周龙3')
    time.sleep(2)


def link_demo():
    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    driver.back()
    time.sleep(1)
    driver.find_element_by_partial_link_text('度娘').click()
    time.sleep(2)
    driver.back()
    time.sleep(1)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)



if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    link_demo()
    # 关闭网页
    driver.quit()
    pass
