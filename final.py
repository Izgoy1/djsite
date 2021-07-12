import codecs
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://timeweb.com/ru/services/hosting/?_ga=2.164408568.654383956.1625444262-1308702186.1625444262#hosting-optimo')

elem_login = browser.find_element_by_xpath("/html/body[@class='pattern1']/div[@class='overlay']/div[@class='table']/div[@class='cell']/div[@class='form w560']/form/div[@class='double']/div[@class='left']/div[@class='label js-fiz']/div[2]/input[@class='suggestions-input']")
elem_email = browser.find_element_by_xpath("/html/body[@class='pattern1']/div[@class='overlay']/div[@class='table']/div[@class='cell']/div[@class='form w560']/form/div[@class='double']/div[@class='left']/div[@class='columns']/div[@class='c5-5']/div[@class='label']/div[2]/input[@class='suggestions-input']")

elem_login.send_keys('login')
elem_email.send_keys('email@mail.com')

browser.find_element_by_xpath("/html/body[@class='pattern1']/div[@class='overlay']/div[@class='table']/div[@class='cell']/div[@class='form w560']/form/div[@class='double']/div[@class='left']/div[@class='hosting-items__button js-send-hosting-form mt10']").click()

time.sleep(15)

browser.find_element_by_xpath("/html/body/section[2]/div[3]/div/div[3]/div[3]/div[1]/div/a").click()

Uptime, Uptime1 = browser.find_element_by_xpath("/html/body/section[2]/div[3]/div/div[3]/div/div/div[1]/section/section[1]/div/section[1]/div[2]/p/span[1]"), browser.find_element_by_xpath("/html/body/section[2]/div[3]/div/div[3]/div/div/div[1]/section/section[1]/div/section[1]/div[2]/p/span[3]")
print("Uptime: ", Uptime.text, " | ", Uptime1.text)
SubScri = browser.find_element_by_xpath("/html/body/section[2]/div[3]/div/div[3]/div/div/div[2]/section/article[1]/div[2]/p")
print("Абоненнтская плата: ", SubScri.text)
DaysLeft = browser.find_element_by_xpath("/html/body/section[2]/div[3]/div/div[3]/div/div/div[2]/section/article[2]/div[2]/p[2]")
print("Дней осталось: ", DaysLeft.text)

writetxt = [Uptime.text, Uptime1.text, SubScri.text, DaysLeft.text]
f = codecs.open('text.txt', 'w', "utf-8")
for index in writetxt:
    f.write(index + ' ')
f.close()

