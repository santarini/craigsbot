import schedule
import time
import datetime
import random
from selenium import webdriver


driver = webdriver.Edge('C:\Program Files\Python\Python36\chromedriver.exe')
driver.get('https://newyork.craigslist.org/');
postButton = driver.find_element_by_id('post')
postButton.click()
time.sleep(3)
subArea = driver.find_element_by_xpath('/html/body/article/section/form/ul/li[1]/label')
subArea.click()
time.sleep(3)
subSubArea = driver.find_element_by_xpath('/html/body/article/section/form/ul/li[1]/label/span[2]')
subSubArea.click()
time.sleep(3)
forSale = driver.find_element_by_xpath('/html/body/article/section/form/ul/li[6]/label/span[2]')
forSale.click()
time.sleep(3)
category = driver.find_element_by_xpath('//*[@id="picker"]/ul/li[22]/label/span[2]')
category.click()
time.sleep(3)
postTitle = driver.find_element_by_id('PostingTitle')
postTitle.send_keys('This is the title YO!')
price = driver.find_element_by_name('price')
price.send_keys('1000')
postBody = driver.find_element_by_id('PostingBody')
postBody.send_keys('California, knows how to party')

                                      
##    js_text_box = driver.find_element_by_class_name('commit-create')
##    js_text_box.click()
##    content = driver.find_element_by_class_name('CodeMirror-code')
##    timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
##    content.send_keys('* <b>' + timenow + '</b> >> Office Computer; \n')
##    time.sleep(3) #necessary sleep time for send_keys to fully run
##    submit = driver.find_element_by_id('submit-file')
##    submit.submit()
##    driver.quit()
##    print("Completed: " + timenow)
##    f = open("GitLog.txt","a")
##    f.write("Completed: " + timenow + "\n")
##    f.close() 
##
##
##schedule.every().day.at("09:00").do(job,'It is 09:00')
##
##while True:
##    schedule.run_pending()
##    #time.sleep(60) # wait one minute
