from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfaiB8pHIV1wzLtrl4mqteS-WEVUoCEL_iWshXTljgq_XnxXg/viewform?usp=sf_link'
zillow_url = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177585009766%2C%22east%22%3A-122.31488314990234%2C%22south%22%3A37.68650107902021%2C%22north%22%3A37.86397631952457%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A694991%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
form_to_gsheet_url = 'https://docs.google.com/forms/d/1lV2uN2j92l6lQdgGKp_4w6qdtEEUsPFNkF_BfFmPVAE/edit'

email_id = '**********'
password_id = '**********'

chrome_driver_path = '/Users/nikhilmittal/Documents/Selenium/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
driver.get(zillow_url)

time.sleep(15)

list_address = driver.find_elements(by=By.CSS_SELECTOR, value='.result-list-container .photo-cards li address')
list_link = driver.find_elements(by=By.CSS_SELECTOR, value='.result-list-container .photo-cards li .list-card-info a')
list_price = driver.find_elements(by=By.CSS_SELECTOR, value='.result-list-container .photo-cards li .list-card-price')

address_list = []
link_list = []
price_list = []

# time.sleep(5)
for address in list_address:
    address_list.append(address.text)
    # print(address.text)

for link in list_link:
    link_list.append(link.get_attribute('href'))
    # print(link.get_attribute('href'))

for price in list_price:
    price_list.append(price.text)
    # print(price.text)

# #
driver.get(form_url)
#
time.sleep(7)
#
email = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email.send_keys(email_id)
email.send_keys(Keys.ENTER)

time.sleep(5)
#
pwd = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
pwd.send_keys(password_id)
pwd.send_keys(Keys.ENTER)

time.sleep(10)
# # #
for n in range(len(address_list)):

    # ADDRESS

    address = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(address_list[n])

    time.sleep(3)

    # PRICE
    #
    price = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(price_list[n])
    time.sleep(3)
    #
    # # PROPERTY LINK
    #
    link = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(link_list[n])
    time.sleep(5)

    #
    # SUBMIT BUTTON
    submit = driver.find_element(by=By.CSS_SELECTOR, value='.lrKTG .DE3NNc .lRwqcd .uArJ5e')
    submit.click()

    time.sleep(5)

    # ANOTHER RESPONSE
    new_response = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_response.click()

    time.sleep(5)

driver.get(form_to_gsheet_url)

time.sleep(3)

responses = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]/span/div')
responses.click()

time.sleep(3)

g_sheet = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div')
g_sheet.click()

time.sleep(8)

create = driver.find_element(by=By.CSS_SELECTOR, value='.OE6hId .l3F1ye')
create.click()

time.sleep(15)

driver.quit()

# data = requests.get(zillow_url)
# print(data.text)
# listings_html = data.text

# soup = BeautifulSoup(listings_html, 'html.parser')

# print(soup.html)
