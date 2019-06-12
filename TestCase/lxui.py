from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
if __name__ == '__main__':

    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    time.sleep(2)


    action_chains = ActionChains(driver)
    time.sleep(2)
    dd_link = driver.find_element_by_link_text('当当')

    dl_link = driver.find_element_by_partial_link_text('度娘')

    jd_link = driver.find_element_by_partial_link_text('东')

    action_chains.key_down(Keys.CONTROL).click(dd_link).key_up(Keys.CONTROL).perform()

    time.sleep(2)
    action_chains1 = ActionChains(driver)
    action_chains.key_down(Keys.CONTROL).click(dl_link).key_up(Keys.CONTROL).perform()
    time.sleep(2)
    action_chains2 = ActionChains(driver)
    action_chains.key_down(Keys.CONTROL).click(jd_link).key_up(Keys.CONTROL).perform()
    time.sleep(2)

    window_handles = driver.window_handles
    for i in window_handles:
        driver.switch_to.window(i)
        if driver.title.__contains__('当当'):
            break
    time.sleep(3)

    driver.quit()
