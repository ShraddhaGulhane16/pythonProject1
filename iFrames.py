from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)

# switch to i-frames - if iframes are present/ embedded into a html
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("It can be automated")

# switch to parent/default window
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
