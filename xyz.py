import pandas as pd
df = pd.read_csv('data.csv')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = 'chromedriver.exe'
browser = webdriver.Chrome(driver)
browser.get('https://your websites')
for i in range(0,1):
    j = 0
    username = browser.find_element_by_name('username')
    username.send_keys(df.iat[i,j])
    j = j+1
    password = browser.find_element_by_name('password')
    password.send_keys(df.iat[i,j])

    form = browser.find_element_by_id('login')
    form.submit()