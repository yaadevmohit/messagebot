from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

users = ["yaadevmohit", "yaadevmohit"]

class InstaBot:
    def __init__(self, username, pw, userList):
        options = Options()
        options.add_extension(f'Switcher.crx')
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        self.pw = pw
        self.userList = userList
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
    def text(self):
        for users in self.userList:
            self.driver.get("https://instagram.com/" + users)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Message')]").click()
            sleep(2)
            self.driver.find_element_by_xpath("//textarea[@placeholder]").send_keys("Hey " + users + "message")
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()
            sleep(2)








                        
my_bot = InstaBot('username', 'password', users)
my_bot.text()
