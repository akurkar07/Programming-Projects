from random import randint
from time import sleep
# from urllib2 import urlopen
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge("C:\\Program Files (x86)\\Microsoft\\Edge Dev\\Application\\msedgedev.exe")
randomUrl = "http://www.setgetgo.com/randomword/get.php"
# search_terms = ['a', 'b', 'c', 'd']
def bot():
    browser.get('https://www.bing.com')
    for _ in range(30):
        browser.set_page_load_timeout(5000)
        assert 'Bing' in browser.title
        # random_term = search_terms[randint(0, len(search_terms)-1)];
        random_term = request.urlopen(randomUrl).read()
        random_term = random_term.decode("utf-8")
        # print(random_term)
        # assert random_term.find(" ") == -1
        # sleep(3)
        search_box = browser.find_element_by_id('sb_form_q')
        # sleep(3)
        search_box.clear()
        # sleep(2)
        search_box.send_keys(random_term+" "+ Keys.RETURN)
        # sleep(3)
        browser.back()


if __name__ == "__main__":
    print('done')
    bot()
    browser.quit()