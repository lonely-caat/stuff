from selenium import webdriver

baseurl = "http://www.google.com.ua"
search_query = "Facebook"

xpaths = {'searchInput': '//input[@name="q"]',
          'paidResults': '//li[@class="ads-ad"]',
          'freeResults': '//div[@class="rc"]',
          'table': "//div[@id='ires']//table[@class='nrgt']"}

mydriver = webdriver.Chrome()
mydriver.get(baseurl)


# Fill search fields and submit
search_field = mydriver.find_element_by_xpath(xpaths['searchInput'])
search_field.send_keys(search_query)
search_field.submit()
table = mydriver.find_elements_by_xpath(xpaths['table'])
print len(table[0].find_elements_by_tag_name("a"))