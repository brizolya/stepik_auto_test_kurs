from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str( math.log( abs( 12*math.sin(int(x)) ) ) )

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input_answer = browser.find_element_by_id('answer')
input_answer.send_keys(y)

check_box = browser.find_element_by_id('robotCheckbox')
check_box.click()

radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

button = browser.find_element_by_tag_name('button').click()

time.sleep(30)

browser.quit()
