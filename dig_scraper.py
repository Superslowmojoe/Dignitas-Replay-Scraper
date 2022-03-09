from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

joreuz_url = 'https://ballchasing.com/?title=&player-name=Joreuz&pro=1&season=&min-rank=&max-rank=&map=&replay-after=&replay-before=&upload-after=&upload-before='
jack_url = 'https://ballchasing.com/?title=&player-name=apparentlyjack&pro=1&season=&min-rank=&max-rank=&map=&replay-after=&replay-before=&upload-after=&upload-before='
scrub_url = 'https://ballchasing.com/?title=&player-name=scrub+killa&pro=1&season=&min-rank=&max-rank=&map=&replay-after=&replay-before=&upload-after=&upload-before='

driver.get(joreuz_url)
replay_page = driver.find_element_by_css_selector('a.replay-link')
replay_page.click()
link = driver.find_element_by_id('$0')
#link.click()
#driver.quit()