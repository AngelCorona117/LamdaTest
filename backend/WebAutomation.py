import os
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def testing():
    """Run the test and return True if it passes, False otherwise."""

    # performance logs are turned off by default, so we need to activate them
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}

    # step 0 Setup Selenium on your local machine
    driver = webdriver.Chrome(desired_capabilities=caps)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//html")))

    # step 1: Write the script for opening the URL:
    driver.get("https://www.lambdatest.com/")

    # step 2: click on each header navigation items
    driver.find_element(
        By.XPATH, "//header/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
    driver.find_element(
        By.XPATH, "// header/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    driver.find_element(
        By.XPATH, "//header/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
    driver.find_element(
        By.XPATH, "//header/nav[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
    driver.find_element(
        By.XPATH, "//a[contains(text(),'Pricing')]").click()

    # step 3: Store the network logs generated on the browser to your local machine.
    logs = driver.get_log('performance')
    for log in logs:
        # index 2 (message) is a string, we must convert it into a json
        log["message"] = json.loads(log["message"])

    output_file = 'E:/performanceLOGS/performance-log-updated(final).json'

    if not os.path.exists(output_file):
        with open(output_file, "w") as f:
            json.dump(logs, f)
            f.write("\n")


    with open(output_file, "a") as f:
        json.dump(logs, f)
        f.write("\n")

    driver.close()
    driver.quit()

    return True


if __name__ == "__main__":
    testing()
