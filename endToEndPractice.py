from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

Service_obj = Service("C:\Selenium\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.implicitly_wait(4)
driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productsName = product.find_element(By.XPATH,"div/h4/a").text
    if productsName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

cartProductName = driver.find_element(By.XPATH, "//a[text()='Blackberry']").text
print(cartProductName)

driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

successText = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(successText)
assert "Success! Thank you!" in successText