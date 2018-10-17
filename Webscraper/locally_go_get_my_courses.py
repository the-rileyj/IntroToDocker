import json

from go_get_my_courses import download_courses, get_my_creds
from selenium import webdriver


def main():
    download_directory = "C:/RJFiles/Consumables/GoTesting/"
    options = webdriver.ChromeOptions()

    # Specify download directory
    prefs = {'download.default_directory' : download_directory}
    options.add_experimental_option("prefs", prefs)

    # Get credentials
    username, password = get_my_creds("./creds.json")

    with webdriver.Chrome("C:/RJFiles/Assets/chromedriver_win32/chromedriver.exe", chrome_options=options) as driver:
        download_courses(username, password, download_directory, driver)

if __name__ == "__main__":
    main()