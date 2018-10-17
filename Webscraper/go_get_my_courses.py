import json
import selenium.webdriver.support.ui as ui

from os import path
from time import sleep

from selenium import webdriver


def click_download_link(driver: webdriver) -> None:
    driver.find_element_by_xpath(r"""//a[text()="Download"]""").click()

def download_videos(url: str, download_path: str, lower: int, upper: int, driver: webdriver) -> None:
    for x in range(lower, upper+1):
        # Sentinal value to indicate page has loaded, necessary because sometimes the page will hang
        bad = True
        while bad:
            try:
                # Format the URL to be the correct page for the given lesson
                driver.get(url.format(x if x > 9 else "0{}".format(x)))

                # Wait until the page has loaded (indicated by the "Download" button)
                ui.WebDriverWait(driver, 30).until(lambda d: d.find_element_by_xpath(r"""//a[text()="Download"]""") is not None)

                # Indicate the the page has successfully loaded
                bad = False
            except:
                pass

        file_name = get_download_file(driver)
        if not path.exists(path.join(download_path, file_name)):
            print("DOWNLOADING:", file_name, flush=True)
            click_download_link(driver)
            sleep(.1)

            # Navigate to downloads, then wait until all downloads are finished
            driver.get("chrome://downloads")
            print("WAITING FOR DOWNLOAD TO FINISH", flush=True)
            while not driver.execute_script(r"""return downloads.Manager.get().items_.every(e => e.state === "COMPLETE");"""):
                sleep(5)
            print("DOWNLOAD FINISHED", flush=True)


def get_download_file(driver: webdriver) -> str:
    return path.basename(driver.find_element_by_xpath(r"""//a[text()="Download"]""").get_attribute("href"))


def get_my_creds(path: str) -> (str, str):
    # Read in credentials from file
    with open(path) as fi:
        creds: dict = json.load(fi)

    return (creds["username"], creds["password"])


def download_courses(username: str, password: str, download_path: str, driver: webdriver):
    wait30: ui.WebDriverWait = ui.WebDriverWait(driver, 30)

    print("LOGGING IN", flush=True)
    # Request the login page and wait for it to load
    driver.get("https://members.usegolang.com/login")
    wait30.until(lambda driver: driver.find_element_by_xpath(r"""//input[@id="email"]""") is not None)

    # Fill in the email and password fields, then hit enter to login
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password + "\n")

    # Wait until login finishes
    wait30.until(lambda driver: driver.find_element_by_xpath(r"""//small[contains(text(), "Access all of your course contents belows")]""") is not None)

    print("LOGGED IN", flush=True)
    print("DOWNLOADING MAIN LESSONS", flush=True)
    # Download all of the main lessons
    download_videos("https://members.usegolang.com/twg/lessons/lesson-{}", download_path, 1, 83, driver)

    # Download all of the project lessons
    download_videos("https://members.usegolang.com/twg/projects/lesson-{}", download_path, 1, 19, driver)

    # driver.get("chrome://downloads")
    # while not driver.execute_script(r"""return downloads.Manager.get().items_.every(e => e.state !== "COMPLETE");"""):
    #     sleep(5)