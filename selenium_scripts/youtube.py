import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scroll_to_end(driver):
    """Scroll to the end of the page."""
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        try:
            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.documentElement.scrollHeight") > last_height
            )
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
        except TimeoutException:
            break  # Break the loop if no new content is loaded

def parse_comments(driver):
    """Parse comments from the YouTube page."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content #content-text"))
    )
    comments = driver.find_elements(By.CSS_SELECTOR, "#content #content-text")
    return [comment.text for comment in comments]

def main(url):
    # Setup Chrome options for WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--disable-gpu")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "ytd-comment-thread-renderer"))
        )

        # Scroll to load comments
        scroll_to_end(driver)

        # Parse comments
        comments = parse_comments(driver)
        for comment in comments:
            print(comment)

    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Comment Parser")
    parser.add_argument("url", help="YouTube video URL to parse comments from")
    args = parser.parse_args()
    main(args.url)
