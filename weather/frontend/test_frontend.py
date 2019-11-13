from selenium import webdriver


baseurl = "https://en.wiktionary.org/"
apple_expected_string = 'A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.'
pear_expected_string = 'An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem'


xpaths = { 'search' : '//*[@name="search"]',
           'list_of_definitions' : "//ol",
           'submitButton' :   "//input[@name='login']"
         }

mydriver = webdriver.Chrome()
mydriver.get(baseurl)


mydriver.find_element_by_xpath(xpaths['search']).send_keys("apple")
## hit that 'Enter' button
mydriver.find_element_by_xpath(xpaths['search']).send_keys(u'\ue007')
definitions = [x.text for x in mydriver.find_elements_by_xpath(xpaths['list_of_definitions'])]

assert apple_expected_string in definitions[0], "{0} not found on the page!".format(apple_expected_string)


mydriver.get(baseurl)
mydriver.find_element_by_xpath(xpaths['search']).send_keys("pear")
## hit that 'Enter' button
mydriver.find_element_by_xpath(xpaths['search']).send_keys(u'\ue007')
definitions = [x.text for x in mydriver.find_elements_by_xpath(xpaths['list_of_definitions'])]

assert pear_expected_string in definitions[0], "{0} not found on the page!".format(pear_expected_string)

print("Done!")
mydriver.quit()