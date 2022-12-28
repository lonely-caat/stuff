from selenium import webdriver

baseurl = "http://www.google.com.ua"
search_query = "MyHeritage"

xpaths = {'searchInput': '//input[@name="q"]',
          'paidResults': '//li[@class="ads-ad"]',
          'freeResults': '//div[@class="rc"]'}

mydriver = webdriver.Chrome()
mydriver.get(baseurl)


# Fill search fields and submit
search_field = mydriver.find_element_by_xpath(xpaths['searchInput'])
search_field.send_keys(search_query)
search_field.submit()

# Return second ad link if it exists, otherwise return the only add's link
try:
    add_links = mydriver.find_elements_by_xpath(xpaths['paidResults'])[1]

except IndexError:
    add_links = mydriver.find_elements_by_xpath(xpaths['paidResults'])[0]

# Print second 'a' tag from the add which contains the 'real' URL
print add_links.find_elements_by_tag_name("a")[1].get_attribute("href")

# Go to first not - ad link
mydriver.implicitly_wait(5)
not_add_link = mydriver.find_elements_by_xpath(xpaths['freeResults'])[0]
not_add_link.find_element_by_tag_name("a").click()
print len(add_links.find_elements_by_tag_name("li"))

