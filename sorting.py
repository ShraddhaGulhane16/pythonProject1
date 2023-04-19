from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


browserSortedVeggies = []

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieElementList = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieElementList:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList