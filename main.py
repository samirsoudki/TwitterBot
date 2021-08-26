url = "https://twitter.com/login/"
url_wifi_speed_testing = "https://www.speedtest.net/"
import os
username = os.getenv("username")
password = os.getenv("password")
PROMISED_UP = 10
PROMISED_DOWN = 100
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_web_driver = "C:\\Users\\Lenovo\\Desktop\\samourou python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_driver)
#checking internet speed
driver.get(url_wifi_speed_testing)
sleep(5)
press_go = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
press_go.click()
sleep(60)
download_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
down_speed = float(download_speed.text)
upload_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
up_speed = float(upload_speed.text)
sleep(5)
driver.get(url)
sleep(5)
#logging in
if PROMISED_DOWN >= down_speed:
    log_in_username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
    log_in_username.send_keys(username)
    log_in_password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
    log_in_password.send_keys(password)
    log_in = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
    log_in.click()
    sleep(5)
#write a tweet

    click_on_write = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    click_on_write.send_keys(f"Hello internet speed provider, why is my download speed {down_speed} and my upload speed {up_speed}, when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up ?")
    tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
    tweet.click()
else:
    pass


