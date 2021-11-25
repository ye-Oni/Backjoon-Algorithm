from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://naver.com")

search_box = browser.find_element_by_id("query")
search_box.send_keys("예워나 사랑해")

search_btn = browser.find_element_by_id("search_btn")
search_btn.click()

# 크롤링 기초