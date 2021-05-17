import webbrowser
import time
import random
from selenium import webdriver

pathBrowser = "D:\\Python\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(pathBrowser)

# videos = [
#     'https://youtu.be/q3O7hoA-G3U',
#     'https://www.youtube.com/watch?v=q3O7hoA-G3U'
# ]

# sleep_time = 0

for i in range(100):
    print("Watching for {} time".format(i))

    driver.get('https://www.youtube.com/watch?v=24KDUdwuVtg')
    time.sleep(200)  # Let the user actually see something!

driver.quit()

# driver.get('https://www.youtube.com/watch?v=q3O7hoA-G3U')
# time.sleep(2)
