from selenium import webdriver
# browser = webdriver.Chrome("chromedriver-2")
# brower.get("https://www.seleniumhq.org")
# elem = browser.find_element_by_link_text('Download')
# elem.click()
# search = browser.find_element_by_id('q')
# search.send_keys('Download')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("chromedriver-2")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target = '"Ravikiran' # Enter your friends name
string = "Message sent using python"  # The message you need to send to ypur friend
x_arg = '//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = driver.find_element_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)
