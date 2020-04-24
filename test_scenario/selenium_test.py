import time
from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get('http://c82/test.php')
time.sleep(3)

driver.save_screenshot('/home/suzuki/screenshot0.png')

search_box = driver.find_element_by_name("comment")
search_box.send_keys('Selenium')

driver.save_screenshot('/home/suzuki/screenshot1.png')

search_box.submit()
time.sleep(2)

driver.save_screenshot('/home/suzuki/screenshot2.png')

driver.quit()

