from distutils.log import error
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import os, random, re, requests, shutil
from tinder_profile import secret_mail, secret_key, driver_path

MAIL = secret_mail
PASSWORD = secret_key
path= driver_path
driver = webdriver.Chrome(path)
error_flg = False
target_url = 'https://tinder.com/'
driver.get(target_url)  
sleep(3)


try:
    login_button = driver.find_element_by_link_text('ログイン')
    login_button.click()
    sleep(3)
    login_button_google = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button')
    sleep(2)
    login_button_google.click()
    sleep(5)
    
except Exception:
    pass
    
handle_array = driver.window_handles
driver.switch_to.window(handle_array[1])
sleep(5)


if error_flg is False:
    try:
        sleep(1)
        mail_form = driver.find_element_by_xpath(r"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        sleep(1)
        mail_form.send_keys(secret_mail)
        sleep(3)
        next_button=driver.find_element_by_xpath(r'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        sleep(1)
        next_button.click()
        sleep(2)

        password_form = driver.find_element_by_xpath(r"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password_form.send_keys(secret_key)
        sleep(4)
        
        next_button=driver.find_element_by_xpath(r'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        sleep(1)
        next_button.click()
        sleep(3)
        
    except Exception:
        error_flg=True
        print('ログイン不可')
        
        
if error_flg is False:
    try:
        driver.switch_to.window(handle_array[0])
        sleep(2)
    except Exception:
        error_flg=True
        print('画面変更エラー')
        

if error_flg is False:
    try:
        sleep(3)
        location_button=driver.find_element_by_xpath(r'/html/body/div[2]/main/div/div/div/div[3]/button[1]')
        sleep(1)
        location_button.click()
        
    except Exception:
        sleep(30)
        print('位置情報認証エラー')
        error_flg=True
        
if error_flg is False:       
    try:
        sleep(3)
        notion_button=driver.find_element_by_xpath(r'/html/body/div[2]/main/div/div/div/div[3]/button[1]')
        sleep(1)
        notion_button.click()
        
    except Exception:
        error_flg=True
        print('通知を許可する')

if error_flg is False:
    try:
        cookie=driver.find_element_by_xpath(r'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
        cookie.click()
        sleep(1)
    except Exception:
        pass
    
    
if error_flg is False:
    while True:
   # 0-1の乱数を生成
        random_num = random.random()
        try:
            if (random_num <= 0.90):
                like_button = driver.find_element_by_xpath(
                    r"/html/body/div[1]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[4]/button")
                like_button.click()
                
            else:
                dislike_button = driver.find_element_by_xpath(
                    r'/html/body/div[1]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[2]/button')
                dislike_button.click()
                
        except Exception:
            not_intersted_button = driver.find_element_by_xpath(
                r'/html/body/div[2]/div/div/div[2]/button[2]')
            not_intersted_button.click()
            
        sleep(random_num^2)