from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from time import sleep

#choosing type of autoliker
print('\tPress 1 for auto like posts of home feed\n\tOr press 2 for autoliking posts of specific username')
autoLikerType= input('1 or 2 ? : ')
if autoLikerType== '2':
    targetUsername= input('Username to like: ')

#taking login credential
url= ('https://www.instagram.com/accounts/login')
username= input(str('Username: '))
password= getpass('Password: ')

print('\tYou are logging in...\n\tWelcome @'+username)

#opening url
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
sleep(3)

#signing in
usernameField= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
passwordField= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
loginButton= driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
sleep(3)

#skiping login info, notification info and reaching home page
skipLoginInfo= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(2)
skipNotificationInfo= driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

#autoliking posts from home feed
if autoLikerType== '1':
    postCounter= 1
    while True:
        xpathValue= '/html/body/div[1]/section/main/section/div[1]/div[2]/div/article['+str(postCounter)+']/div[3]/section[1]/span[1]/button'
        liker=driver.find_element_by_xpath(xpathValue).click()
        postCounter+= 1
        sleep(2)

#autoliking posts of specific username
elif autoLikerType== '2':
    visitTarget= ('https://www.instagram.com/'+str(targetUsername))
    driver.get(visitTarget)
    sleep(3)
    try:
        openPost= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]').click()
    except:
        openPost= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a').click()
    sleep(2)
    liker= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
    nextPost= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
    while True:
        sleep(2)
        liker= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        nextPost= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
        sleep(2)
