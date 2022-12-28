import random
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://zabbix-stage.llnw.net/"
triggerurl = "https://zabbix-stage.llnw.net/triggers.php?form=update&hostid=100100000049140&triggerid=100100004422417&sid=8e39de01d2f757fa"
username = "zabbix-api-limon-qa"
password = ""

xpaths = { 'usernameTxtBox': "//input[@id='name']",
           'passwordTxtBox': "//input[@name='password']",
           'submitButton':   "//input[@id='enter']",
           'clone': "//input[@id='clone']",
           'prio_aver': '//span[contains(text(), "Average")]',
           'prio_high': '//span[contains(text(), "High")]',
           'prio_disas': '//span[contains(text(), "Disaster")]',
           'name': "//input[@id='description']",
           'save': "//input[@id='save']"
         }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

for el in xrange(1,100):
    mydriver.get(triggerurl)
    mydriver.find_element_by_xpath(xpaths['clone']).click()
    mydriver.implicitly_wait(3)
    mydriver.find_element_by_xpath(xpaths['name']).clear()
    mydriver.find_element_by_xpath(xpaths['name']).send_keys(("outbound bandwidth above max percent threshold of 1% 10GigabitEthernet7/1 (BBLLNW | 10GE | FR3.TYO3 | E11/3 | LB | LLNW-{0}) on fr3.meow.meow.net").format(random.randint(1000,10000))
)
    print el
    if random.randint(3,5) == 3:
        mydriver.find_element_by_xpath(xpaths['prio_disas']).click()
    elif random.randint(3,5) == 4:
        mydriver.find_element_by_xpath(xpaths['prio_aver']).click()
    else:
        mydriver.find_element_by_xpath(xpaths['prio_high']).click()
    mydriver.find_element_by_xpath(xpaths['save']).click()
