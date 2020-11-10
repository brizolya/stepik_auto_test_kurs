from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    button = browser.find_element_by_id("verify")
    button.click()

    message = browser.find_element_by_id("verify_message")

    assert "seccessful" in message.text

finally:
    time.sleep(5)
    browser.quit()



