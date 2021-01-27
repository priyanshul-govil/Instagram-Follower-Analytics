from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

######################################################
########## DO NOT MAKE CHANGES TO THIS FILE ##########
######################################################

class InstagramUnfollower:

    unfollowers = []            # People you follow who don't follow you back
    ghost_followers = []        # People you don't follow back

    _whitelist = set()          # People who don't follow you back but you don't want to unfollow them
    _blacklist = set()          # People you dont't follow back and never want to follow

    _follower_accounts = []
    _following_accounts = []


    # Initialize data members
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'.\geckodriver.exe')


    # Login to account
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        while driver.current_url == "https://www.instagram.com/accounts/login/":
            try:
                username_box = driver.find_element_by_xpath("//input[@name='username']")
                username_box.clear()
                username_box.send_keys(self.username)
                password_box = driver.find_element_by_xpath("//input[@name='password']")
                password_box.clear()
                password_box.send_keys(self.password)
                password_box.send_keys(Keys.RETURN)
                time.sleep(0.5)
            
            except StaleElementReferenceException:
                pass
        
        time.sleep(2)
        return driver


    # Load whitelist and blacklist
    def load_data(self):
        # Load Whitelist
        try:
            with open("whitelist.txt", "r") as wl:
                for acc in wl:
                    self._whitelist.add(acc.rstrip('\n'))
        except (OSError, IOError):
            pass

        #Load Blacklist
        try:
            with open("blacklist.txt", "r") as bl:
                for acc in bl:
                    self._blacklist.add(acc.rstrip('\n'))
        except (OSError, IOError):
            pass


    # Generate list of accounts you follow
    def find_followings(self, driver, buttons):
        following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
        following_button[0].click()
        time.sleep(2)
        
        following_window = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

        prev_li_count = 0
        curr_li_count = len(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").find_elements_by_tag_name("li"))
        
        # Keep on scrolling till all users are loaded
        while prev_li_count != curr_li_count:
            following_window.send_keys(Keys.END)
            time.sleep(1)
            prev_li_count = curr_li_count
            curr_li_count = len(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").find_elements_by_tag_name("li"))

        for i in range(1, curr_li_count + 1):
            text = driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a").text
            self._following_accounts.append(text)


    # Generate list of accounts that follow you
    def find_followers(self, driver, buttons):
        follower_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
        follower_button[0].click()
        time.sleep(2)
        
        follower_window = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

        prev_li_count = 0
        curr_li_count = len(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").find_elements_by_tag_name("li"))
        
        # Keep on scrolling till all users are loaded
        while prev_li_count != curr_li_count:
            follower_window.send_keys(Keys.END)
            time.sleep(1)
            prev_li_count = curr_li_count
            curr_li_count = curr_li_count = len(driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul").find_elements_by_tag_name("li"))

        for i in range(1, curr_li_count + 1):
            text = driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a").text
            self._follower_accounts.append(text)


    # Compares list of followers and following and generates results
    def compare_following_and_followers(self, followers, followings):
        followers = set(self._follower_accounts)
        followings = set(self._following_accounts)
        
        self.unfollowers = followings - (followers | self._whitelist)
        self.ghost_followers = followers - (followings | self._blacklist)


    # Combines all function calls and generates data in CSV
    def execute_script(self):
        self.load_data()

        driver = self.login()
        driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)

        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
        self.find_followings(driver, buttons)
        time.sleep(2)

        driver.refresh()
        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")
        self.find_followers(driver, buttons)
        time.sleep(2)

        driver.quit()

        self.compare_following_and_followers(self._follower_accounts,self._following_accounts)
