from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.facebook.com/"
username = ""
password = ""

xpaths = { 'usernameTxtBox' : "//input[@id='email']",
           'passwordTxtBox' : "//input[@id='pass']",
           'submitButton' :   "//input[@value='Log In']",
           'findFriends' :   "//a[@id='findFriendsNav']",
           'friendsTable': "//div[@class='friendBrowserCheckboxContentGrid']//li[@class='friendBrowserListUnit']",
           'addFriend': "//div[@class='friendBrowserCheckboxContentGrid']//li[@class='friendBrowserListUnit']//button[@type='button']"
         }


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
mydriver = webdriver.Chrome(chrome_options=chrome_options)
mydriver.get(baseurl)


def scroll():
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = mydriver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        mydriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        mydriver.implicitly_wait(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = mydriver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

#Clear Username TextBox if already allowed "Remember Me"
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me"
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

mydriver.find_element_by_xpath(xpaths['findFriends']).click()

friends_table = mydriver.find_elements_by_xpath(xpaths['friendsTable'])
scroll()
import time;time.sleep(5)
for button in mydriver.find_elements_by_xpath(xpaths['addFriend']):
    button.click()


