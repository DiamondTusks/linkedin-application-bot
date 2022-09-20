from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3230860528&distance=25&f_AL=true&geoId=104769905&keywords=python%20developer&location=Sydney%2C%20New%20South%20Wales%2C%20Australia&refresh=true&sortBy=R"
USERNAME = "diamondtusks@gmail.com"
PASSWORD = "nLXv)G0M*fH3"
MOBILE = "0406579199"

chrome_driver_path = "/Users/me/Documents/development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(URL)
login_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login_button.click()
# time.sleep(5)
login_username = driver.find_element(By.NAME, "session_key")
login_username.send_keys(USERNAME)
login_password = driver.find_element(By.NAME, "session_password")
login_password.send_keys(PASSWORD)
login_password.send_keys(Keys.ENTER)
time.sleep(3)

all_listing = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

for listing in all_listing:
    print("called")
    listing.click()
    time.sleep(2)

    # try to locate submit button, if cant locate skip the job.
    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        easy_apply.click()
        time.sleep(3)

        # If phone field is empty, fill in your phone number.
        mobile_input = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if mobile_input == "":
            mobile_input.send_keys(MOBILE)
            time.sleep(3)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If submit button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue-unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.XPATH, '//*[@id="ember406"]')
            discard_button.click()
            print("Complex application, skipped.")
            continue

        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")

time.sleep(5)
driver.quit()