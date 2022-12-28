
#ScriptName : Login.py
#---------------------
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


baseurl = "https://coub.com/"
username = ""
password = ""

xpaths = { "login": '//button[contains(text(), "Log in")]',
           "first_coub": "//div[@class='viewer__shadow viewer__click -fill']"[0],
           "controls": "//div[@class='viewer__controls__play']",
           "facebook": '//div[@page-id="sign-in-page"]//button[contains(text(), "Facebook")]',
            'email' : "//input[@id='email']",
            'password' : "//input[@id='pass']",
           'pause' : "//div[@class='viewer__play viewer__click box--vertical -pause']",
           'loginButton' : '//input[@name="login"]',
           'continueButton': '//button[@name="__CONFIRM__"]',
           'skipButton': '//button[@name="__SKIP__"]',

           'avatar': "//div[@class='box--vertical current header-channel__avatar']",


         }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

#silence first coub while we login

ActionChains(mydriver).move_to_element(mydriver.find_element_by_xpath(xpaths['controls'])).perform()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(mydriver, 3).until(EC.presence_of_element_located((By.XPATH, xpaths['pause'])))
mydriver.find_element_by_xpath(xpaths['pause']).click()

mydriver.find_element_by_xpath(xpaths['login']).click()
mydriver.find_element_by_xpath(xpaths['facebook']).click()

# mydriver.find_element_by_xpath(xpaths['email']).click()
window_before = mydriver.window_handles[0]
window_after = mydriver.window_handles[1]



#Write Password in password TextBox
mydriver.switch_to.window(window_after)
mydriver.find_element_by_xpath(xpaths['email']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['password']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['loginButton']).click()
import pdb;pdb.set_trace()



# pause = "//div[@class='viewer__pause__content']"
# controls = "//div[@class='viewer__controls__play']"
# mydriver.find_element_by_xpath("//div[@class='viewer__shadow viewer__click -fill']").click()