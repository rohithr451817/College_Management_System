# Test Case 1: Search for Restaurants

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

search_box = driver.find_element_by_name("q")
search_box.send_keys("Italian restaurants in Delhi")
search_box.submit()

results = driver.find_elements_by_class_name("search_result")
assert len(results) > 0

driver.quit()


# Test Case 2: Filter Restaurants by Rating

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

rating_filter = driver.find_element_by_class_name("rating-filter")
rating_filter.click()

four_star_filter = driver.find_element_by_class_name("four-star")
four_star_filter.click()

results = driver.find_elements_by_class_name("search_result")
assert len(results) > 0

driver.quit()


# Test Case 3: Sort Restaurants by Price

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

price_sort = driver.find_element_by_class_name("price-sort")
price_sort.click()

low_to_high = driver.find_element_by_class_name("low-to-high")
low_to_high.click()

results = driver.find_elements_by_class_name("search_result")
assert len(results) > 0

driver.quit()


# Test Case 4: Verify Restaurant Details

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

name = driver.find_element_by_class_name("restaurant-name")
assert name.text == "Italian Restaurant"

address = driver.find_element_by_class_name("restaurant-address")
assert address.text == "New Delhi, NCR"

driver.quit()


# Test Case 5: Add Restaurant to Favorites

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

favorite_button = driver.find_element_by_class_name("favorite-button")
favorite_button.click()

assert driver.find_element_by_class_name("favorite-added")

driver.quit()


# Test Case 6: Verify Search Results Count

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

count = driver.find_element_by_class_name("search-count")
assert count.text == "50+ results"

driver.quit()


# Test Case 7: Verify Restaurant Menu

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("(link unavailable)")

menu_items = driver.find_elements_by_class_name("menu-item")
assert len(menu_items) > 0

driver.quit()