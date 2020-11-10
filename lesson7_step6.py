from selenium import webdriver
import time
import math

try:

    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str( math.log( abs( 12*math.sin(int(x)) ) ) )

    button = browser.find_element_by_css_selector("button.trollface.btn").click()

    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)

    sub_button = browser.find_element_by_css_selector("button.btn").click()

finally:

    time.sleep(10)
    browser.quit()    

