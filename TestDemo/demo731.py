from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('https://www.baidu.com')
time.sleep(2)

if __name__ == '__main__':
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('云顶之弈')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="su"]').click()

    driver.quit()
    pass