from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
        return str( math.log( abs( 12*math.sin(int(x)) ) ) )

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book =browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)

    sub_button = browser.find_element_by_id("solve").click()

finally:

    time.sleep(5)
    browser.quit()    