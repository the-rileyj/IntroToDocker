import json

from go_get_my_courses import download_courses, get_my_creds
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def main():
    download_directory = "/app/dl/"
    options = webdriver.ChromeOptions()

    # Specify download directory
    prefs = {'download.default_directory' : download_directory}
    options.add_experimental_option("prefs", prefs)

    # Get credentials
    username, password = get_my_creds("./creds.json")

    with webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_capabilities=options.to_capabilities()) as driver:
        download_courses(username, password, download_directory, driver)

if __name__ == "__main__":
    main()