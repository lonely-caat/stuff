import random
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://zabbix-command01.dev.phx7.llnw.net/index.php"
# baseurl = "https://zabbix-stage.llnw.net/index.php"
triggerurl = "https://zabbix-command01.dev.phx7.llnw.net/triggers.php?form=update&triggerid=23079&sid=5af91ffdc9de71c8"
# triggerurl = "https://zabbix-stage.llnw.net/triggers.php?form=update&triggerid=100100004397305&sid=64c61129e5b34736"
username = "zabbix-api-limon-qa"
password = "YuN0cH4nGem4%"

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

mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

for el in range(1,10):
    mydriver.get(triggerurl)
    mydriver.find_element_by_xpath(xpaths['clone']).click()
    mydriver.implicitly_wait(3)
    mydriver.find_element_by_xpath(xpaths['name']).clear()
    mydriver.find_element_by_xpath(xpaths['name']).send_keys(("bidirectional bandwidth below minimum threshold of 1Mbps 10GigabitEthernet1/1 (PRIVATEP | 10GE | VNPT | 45899 | LLNW-00007081 [MEGA-I:C178982-00 NETPROV-{0}]) on fr3.hkg2.llnw.net").format(random.randint(1000,10000))
)
    print(el)
    if random.randint(3,5) == 3:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[4]/label').click()
    elif random.randint(3,5) == 4:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[5]/label').click()
    else:
        mydriver.find_element_by_xpath('//*[@id="priority"]/li[6]/label').click()
    mydriver.find_element_by_xpath(xpaths['save']).click()

mydriver.close()

# MA TRIGGERS https://zabbix-command01.dev.phx7.llnw.net/triggers.php?form=update&hostid=10001&triggerid=22314