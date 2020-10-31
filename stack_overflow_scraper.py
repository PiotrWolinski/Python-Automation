from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from time import sleep

def send_keys_slowly(text, element):
    for char in text:
        element.send_keys(char)
        sleep(0.2)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stackoverflow.com/')

tag_to_search = 'python'

search_box = driver.find_element_by_xpath('//*[@id="search"]/div/input')
send_keys_slowly(tag_to_search, search_box)
search_box.send_keys(webdriver.common.keys.Keys.ENTER)

total_answers = 0
current_page = 1
while True:
    try:
        sleep(2)

        answers = driver.find_elements_by_class_name('question-summary')
        total_answers += len(answers)
        
        print(f'Current page: {current_page}')
        print(f'Answers gathered: {total_answers}')

        if current_page == 1:
            close_alert = driver.find_element_by_xpath('//*[@id="js-gdpr-consent-banner"]/div/div[2]/a')
            close_alert.click()

        next_page = driver.find_element_by_xpath(f'//*[@title="Go to page {current_page + 1}"]')
        next_page.click()

        current_page += 1
        
    except NoSuchElementException:
        print('Finished')
        break