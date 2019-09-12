from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".trollface")
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    submit_btn = browser.find_element_by_css_selector("button[type='submit']")
    submit_btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()