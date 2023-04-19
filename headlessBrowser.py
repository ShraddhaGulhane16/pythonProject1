from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

Service_Obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(4)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")