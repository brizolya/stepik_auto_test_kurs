from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input_firstName = browser.find_element_by_name("firstname").send_keys("Ivan")
    input_lastName = browser.find_element_by_name("lastname").send_keys("Petrov")
    input_email = browser.find_element_by_name("email").send_keys("ivan@petrov.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    input_file = browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()    

finally:
    time.sleep(10)
    browser.quit()
