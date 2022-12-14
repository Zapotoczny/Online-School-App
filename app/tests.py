from django.test import TestCase
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import names
# Create your tests here.

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(url='http://127.0.0.1:8000/')

def add_random_student():
    driver.find_element('xpath','/html/body/div/nav/div[1]/a[3]').click()
    time.sleep(1)
    driver.find_element('xpath','//*[@id="id_name"]').send_keys(names.get_first_name())
    driver.find_element('xpath','//*[@id="id_last_name"]').send_keys(names.get_last_name())
    driver.find_element('xpath','//*[@id="id_class_number"]').send_keys(6)
    time.sleep(1)
    driver.find_element('xpath','/html/body/div/div/div/div/form/button').click()

add_random_student()
