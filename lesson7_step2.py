from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
        return str(int(x) + int(y))

    arg1_element = browser.find_element_by_id('num1')
    arg2_element = browser.find_element_by_id('num2')
    arg1 = arg1_element.text
    arg2 = arg2_element.text
    answer = calc(arg1, arg2)
    
    select =Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(answer)
    
    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)

    browser.quit()