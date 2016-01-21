from selenium import webdriver

print('Input your user name')
userEmail = input()
print('Input your password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://login.microsoftonline.com/')

emailElem = browser.find_element_by_id('cred_userid_inputtext')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('cred_password_inputtext')
passwordElem.send_keys(userPassword)
passwordElem.submit()

shellElem = browser.find_element_by_id('ShellMail_link_text')
shellElem.click()

newElem = browser.find_element_by_xpath('//*[@id="primaryContainer"]/div[4]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/button')
newElem.click()
