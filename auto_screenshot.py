import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def open_url(url, searchtext):
    # This function will open an url and pass it to the next function save_screenshot()
    options = Options()

    options.headless = True     # this will make the chrome to run without UI (headless)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.maximize_window()    # it maximizes the webpage the webdriver is using
    driver.get(url)
    save_screenshot(driver, '{}.png'.format(searchtext))

def save_screenshot(driver, file_name):
    height = scroll_down(driver)    # scroll_down will auto scroll the page and return the height if the page
    driver.set_window_size(1080, height)
    driver.save_screenshot(file_name)
    print(" screenshot saved ")


def scroll_down(driver):
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = 0

    while True:

        new_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(1, 6):
            # this will scroll the page down a little bit each time, it helps webpage to load the images
            driver.execute_script("window.scrollTo(0, {});".format(last_height+i*(new_height - last_height) // 5))
            time.sleep(SCROLL_PAUSE_TIME)

        if last_height == new_height:   # when webpage cannot be scrolled down anymore, then we reach the bottom
            break

        last_height = new_height

    driver.execute_script("window.scrollTo(0, 0);")
    return last_height


def screenshot(searchtext):
    url = "https://www.google.co.in/search?q=" + searchtext + "&source=lnms&tbm=isch"
    open_url(url, searchtext)

