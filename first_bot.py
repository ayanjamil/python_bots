from selenium import webdriver
from bs4 import BeautifulSoup

# Create a new instance of the Firefox webdriver
driver = webdriver.Firefox()

# Navigate to YouTube
driver.get("https://www.youtube.com/")

# Find the search bar and search for a video
search_bar = driver.find_element_by_name("search_query")
search_bar.send_keys("Python programming tutorial")
search_bar.submit()

# Wait for the search results to load
driver.implicitly_wait(10)

# Find the first video and skip it
video = driver.find_element_by_css_selector("#contents > ytd-video-renderer:nth-child(1)")
video.click()
skip_button = driver.find_element_by_css_selector(".ytp-ad-skip-button-container")
skip_button.click()
