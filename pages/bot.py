import os
import time
import string
import requests
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 


class acreator:
        def __init__(self):
                self.html = ""
                self.proxies = []
                self.path = 'driver/chromedriver.exe'
                self.driver = webdriver.Chrome(executable_path=self.path)
                self.html = requests.get("https://www.fakenamegenerator.com/", headers={
                                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}).text
                self.email = self.html.split(
                        '<dt>Email Address</dt>')[1].split('<dd>')[1].split('        ')[0]

                self.user = self.html.split(
                        "<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]

                self.password = self.html.split(
                        "<dt>Password</dt>")[1].split("</dd>")[0].split("<dd>")[1]
            
                self.username = self.html.split(
                        "<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]
            
                try:
                        self.CVC = self.html.split(
                                "<dt>CVC2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
                except:
                        self.CVC = self.html.split(
                                "<dt>CVV2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        def start_process(self):
                self.baseURL = 'https://www.instagram.com/accounts/emailsignup/'
                self.driver.get(self.baseURL)
                emaili = WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.NAME, "emailOrPhone"))
                )
                emaili.send_keys(self.email)     
                self.driver.find_element_by_name("fullName").send_keys(self.username)
                self.driver.find_element_by_name("username").send_keys(self.username + self.CVC)
                self.driver.find_element_by_name("password").send_keys(self.password)
                weiter = self.driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")[1]
                weiter.click()
            
                month_one = WebDriverWait(self.driver, 60).until(
                        EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, '.h144Z option[value="3"]'))
                )
                month_one.click()
                WebDriverWait(self.driver, 5000)
            
                day_one = WebDriverWait(self.driver, 1000).until(
                        EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, '.h144Z option[value="12"]'))
                )
                day_one.click()
                WebDriverWait(self.driver, 5000)
            
                year_one = WebDriverWait(self.driver, 1000).until(
                        EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, '.h144Z option[value="1999"]'))
                )
                year_one.click()#sqdOP  L3NKy _4pI4F  y3zKF     
                weiter = self.driver.find_element_by_css_selector(".sqdOP.L3NKy._4pI4F.y3zKF")
                weiter.click()

                with open("instagramaccountinfo.txt",'a') as txtFile:
                        txtFile.writelines(self.email + ":" + self.password + "\n")
