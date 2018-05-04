import random
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://zabbix-command01.dev.phx7.llnw.net/index.php"
triggerurl = "https://zabbix-command01.dev.phx7.llnw.net/triggers.php?form=update&hostid=10084&triggerid=19922"
username = "zabbix-api-limon-qa"
password = "YuN0cH4nGem3%"

xpaths = { 'usernameTxtBox': "//input[@id='name']",
           'passwordTxtBox': "//input[@name='password']",
           'submitButton':   "//button[@name='enter']",
           'clone': "//button[@id='clone']",
           'prio_aver': "//input[@id='priority_3']",
           'prio_high': "//input[@id='priority_4']",
           'prio_disas': "//input[@id='priority_5']",
           'name': "//input[@id='description']",
           'save': "//button[@id='add']"
         }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

for el in xrange(1,10):
    mydriver.get(triggerurl)
    mydriver.find_element_by_xpath(xpaths['clone']).click()
    mydriver.implicitly_wait(3)
    mydriver.find_element_by_xpath(xpaths['name']).clear()
    mydriver.find_element_by_xpath(xpaths['name']).send_keys(("outbound bandwidth above max percent threshold of 26% 10GigabitEthernet7/1 (BBLLNW | 10GE | FR3.TYO3 | E11/3 | LB | LLNW-{0}) on fr3.meow.meow.net").format(random.randint(1000,10000))
)
    print el
    if random.randint(3,5) == 3:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[4]/label').click()
    elif random.randint(3,5) == 4:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[5]/label').click()
    else:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[6]/label').click()
    mydriver.find_element_by_xpath(xpaths['save']).click()
