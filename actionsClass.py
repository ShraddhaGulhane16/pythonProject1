from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(2)
action = ActionChains(driver)

#action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.double_click(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
