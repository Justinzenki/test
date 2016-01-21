from selenium import webdriver

print('Input your user name')
userEmail = input()
print('Input your password')

browser = webdriver.Firefox()
browser.get('https://login.microsoftonline.com/')

emailElem = browser.find_element_by_id('cred_userid_inputtext')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('cred_password_inputtext')
passwordElem.send_keys(userPassword)


