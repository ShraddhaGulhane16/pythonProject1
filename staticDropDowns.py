from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

staticDropDown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
staticDropDown.select_by_index(0)

driver.close()