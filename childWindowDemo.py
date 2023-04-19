from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_Obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")


driver.find_element(By.LINK_TEXT, "Click Here").click()
openWindow = driver.window_handles

# switch to child window

driver.switch_to.window(openWindow[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

# Switch to parent window

driver.switch_to.window(openWindow[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"

