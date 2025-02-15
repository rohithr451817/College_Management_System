import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_video_on_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com")
        self.assertIn("YouTube", driver.title)

        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Daily Max")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer.style-scope.ytd-item-section-renderer"))
        )

        # Select the first video result
        video_title = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer.style-scope.ytd-item-section-renderer")
        video_title.click()

        # Wait for the video to start playing
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.ytp-play-button.ytp-button"))
        )

        # Play the video for 4 seconds
        time.sleep(4)

        # Exit the video
        driver.quit()

if __name__ == "__main__":
    unittest.main()