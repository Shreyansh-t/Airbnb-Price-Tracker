import time
import requests
# import nav
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


driver = None
headless_mode = True

def start():
    global driver
    chrome_options = webdriver.ChromeOptions()
    if headless_mode:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)


def open_site():
    global driver
    driver.get("https://www.airbnb.co.in/")
    return driver



class Entry:

    def __init__(self, where, check_in, check_out, adults, children, infants):
        self.where = where
        self.check_in = check_in
        self.check_out = check_out
        self.adults = adults
        self.children = children
        self.infants = infants


    def add_details(self):
        WebDriverWait(driver, 10)
        # time.sleep(2)
        where_to = driver.find_element(By.ID, "bigsearch-query-location-input")
        where_to.send_keys(self.where)

        WebDriverWait(driver, 4)
        check_in = driver.find_element(By.CSS_SELECTOR, "div .p1m42al0")
        check_in.click()

        flexible = driver.find_element(By.ID, "tab--tabs--2")
        flexible.click()

        
        
        who = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[2]/div[1]/div/div[2]")
        who.click()

        num_adults = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div/div/div[1]/div/button[2]")
        for i in range(self.adults):
            num_adults.click()
        
        num_children = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div/div/div[2]/div/button[2]")
        for i in range(self.children):
            num_children.click()
        
        num_infants = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[1]/div/div/div/div/div/div[3]/div/button[2]")
        for i in range(self.infants):
            num_infants.click()

        WebDriverWait(driver, 2)
        search_button = driver.find_element(By.CLASS_NAME, "bhtghtc")
        search_button.click()

        WebDriverWait(driver, 10)


def go_back():
    driver.back()


title_list = []
DESC = []
ROOMS = []
WEEK =[]
PRICE = []



def fetch_data():
    # WebDriverWait(driver, 2)
    
    time.sleep(2)
    title_list.clear()
    DESC.clear()
    ROOMS.clear()
    PRICE.clear()
    WEEK.clear()
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    
    while True:

        title = soup.select("div[data-testid='listing-card-title']")
        for t in title:
            title_list.append(t.text.strip())
        
        desc = soup.select("span[data-testid='listing-card-name']")
        for d in desc:
            DESC.append(d.text.strip())

        rooms = soup.select('div[data-testid="listing-card-subtitle"] span')
        for room in rooms:
            ROOMS.append(room.text.strip())

        price = soup.select("span._11jcbg2")
        for p in price:
            PRICE.append(p.text.strip())
        
        weeks = soup.select("span._a8jt5op")
        for week in weeks:
            WEEK.append(week.text.strip())

        

        time.sleep(1)

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next"]')
            next_button.click()
        except NoSuchElementException:
            break

        
    print(DESC)
    return title_list, DESC, PRICE 
    



# def fetch_data():
#     time.sleep(2)
#     data = {}
    
#     while True:
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'lxml')
        
#         titles = [t.text.strip() for t in soup.select("div[data-testid='listing-card-title']")]
#         prices = [p.text.strip() for p in soup.select("span._11jcbg2")]

#         for title, price in zip(titles, prices):
#             data[title] = price
#             print(f"Scraped: Title={title}, Price={price}")
        
#         time.sleep(2)

#         try:
#             next_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next"]')
#             next_button.click()
#         except NoSuchElementException:
#             break
#     print(data)
#     return data