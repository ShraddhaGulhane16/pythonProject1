from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Service_Obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("ScreenDown.png")