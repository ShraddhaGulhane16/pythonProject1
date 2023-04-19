from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
Open_Windows = driver.window_handles

driver.switch_to.window(Open_Windows[1])
getText = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
print(getText)

getEmail = getText.split("at")[1].strip().split(" ")[0]
print(getEmail)
driver.close()

driver.switch_to.window(Open_Windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(getEmail)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(getEmail)
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)





