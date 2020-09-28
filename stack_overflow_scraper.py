from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stackoverflow.com/')

search_box = driver.find_element_by_xpath('//*[@id="search"]/div/input')
search_box.send_keys('python')
search_box.send_keys(webdriver.common.keys.Keys.ENTER)

total_answers = 0
current_page = 1
while True:
    try:
        answers = driver.find_elements_by_class_name('question-summary')
        total_answers += len(answers)
        print(f'Current page: {current_page}')
        print(f'Answers gathered: {total_answers}')


        if current_page == 1:
            close_alert = driver.find_element_by_xpath('//*[@id="js-gdpr-consent-banner"]/div/div[2]/a')
            close_alert.click()

        if current_page == 14:
            os.system('pause')

        # next_page = driver.find_element_by_link_text(f"{current_page + 1}") 
        next_page = driver.find_element_by_xpath(f'//*[@title="Go to page {current_page + 1}"]')
        next_page.click()

        # driver.implicitly_wait(5)
        sleep(4)
        # wait = WebDriverWait(driver, 5)
        
        
        current_page += 1
        
    except NoSuchElementException:
        print('Finished')
        break