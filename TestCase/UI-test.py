from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.60.146:8080/demo1.html')
time.sleep(2)





if __name__ == '__main__':
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input').send_keys('艾欧尼亚,昂扬不灭')
    time.sleep(2)
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.clear()
    time.sleep(2)

    sc_el = driver.find_element_by_id('file1')
    time.sleep(2)
    sc_el.send_keys('C:/Users/Administrator/Pictures/搜狗截图20190609091444.png')
    time.sleep(2)
    sc_el.clear()
    time.sleep(2)

    dx_el = driver.find_elements_by_name('radio')
    time.sleep(1)
    dx_el[0].click()
    time.sleep(1)
    dx_el[1].click()
    time.sleep(1)

    duox_el = driver.find_elements_by_xpath('//input[@class="checkbox"and@type="checkbox"]')
    duox_el[0].click()
    time.sleep(1)
    duox_el[1].click()
    time.sleep(1)
    duox_el[2].click()
    time.sleep(1)
    duox_el[2].click()
    time.sleep(1)

    tk_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    time.sleep(1)
    tk_el.click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    # driver.switch_to.alert.dismiss()
    time.sleep(2)

    pws_el = driver.find_element_by_xpath('//input[@type="password"]')
    time.sleep(1)
    pws_el.send_keys('1324we')
    time.sleep(2)
    sc_el.clear()
    time.sleep(2)

    driver.find_element_by_tag_name('textarea').send_keys('德玛西亚,永世长存')
    sc_el.clear()
    time.sleep(2)


    select_el = driver.find_element_by_css_selector(
        'body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    s = Select(select_el)
    time.sleep(1)
    s.select_by_index(1)
    time.sleep(1)
    s.select_by_value('z1')
    time.sleep(1)
    s.select_by_visible_text('周龙3')
    time.sleep(2)

    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element_by_partial_link_text('度娘')
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)

    driver.quit()

    pass
