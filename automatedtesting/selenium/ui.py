# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import logging

def start_browser():
    print('Starting the browser...')
    logging.info('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # --uncomment when running locally.
    # driver = webdriver.Chrome()
    print('Browser started successfully.')
    logging.info('Browser started successfully.')
    return driver

def navigate_to_page(driver, url):
    print('Navigating to page:', url)
    logging.info('Navigating to page:' + url)
    driver.get(url)
    print('Navigated to page:', url)
    logging.info('Navigated to page:' + url)


# Start the browser and login with standard_user
def login (driver, user, password):
    print ('Logging in as user', user)
    logging.info ('Logging in as user' + user)
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    print ('Logged in as user', user)
    logging.info ('Logged in as user' + user)


#main
logging.basicConfig(filename="/var/log/selenium/ui.log",format='%(asctime)s %(message)s',filemode='w') #/var/log/selenium/ui.log
logger=logging.getLogger()
logger.setLevel(logging.INFO)

driver=start_browser()
navigate_to_page(driver, 'https://www.saucedemo.com/')
login(driver, 'standard_user', 'secret_sauce')

#Add all inventory items
inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
print('Adding cart items')
logging.info('Adding cart items')
for inventory_item in inventory_items:
    button = inventory_item.find_element_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']")
    button.click()
    print('  Added item', inventory_item.find_element_by_css_selector("div[class='inventory_item_name']").text)
    logging.info('  Added item' + inventory_item.find_element_by_css_selector("div[class='inventory_item_name']").text)
print('Added cart items')
logging.info('Added cart items')

#Open cart
print('Opening cart')
logging.info('Opening cart')
driver.find_element_by_css_selector("a[class='shopping_cart_link']").click()
print('Opened cart')
logging.info('Opened cart')

#Delete all inventory items
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
print('Removing cart items')
logging.info('Removing cart items')
for cart_item in cart_items:
    button = cart_item.find_element_by_css_selector("button[class='btn btn_secondary btn_small cart_button']")
    print('  Removed item', cart_item.find_element_by_css_selector("div[class='inventory_item_name']").text)
    logging.info('  Removed item' + cart_item.find_element_by_css_selector("div[class='inventory_item_name']").text)
    button.click()
print('Removed cart items')
logging.info('Removed cart items')

#Closing browser
driver.quit()
print('Exited the browser')
logging.info('Exited the browser')