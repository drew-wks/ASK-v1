from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def check_app_status(url):
    """
    This function checks the status of a web application by navigating to the provided URL 
    and searching for specific text strings ("USCG Auxiliary" and "Zzzz") on the page.
    
    The function uses Selenium to automate a Chrome browser in headless mode, which means 
    it operates without a visible GUI. This is particularly useful in environments like 
    GitHub Actions, where a graphical user interface is not available.

    Args:
        url (str): The URL of the web page to check.

    Behavior:
        - If the text "USCG Auxiliary" is found on the page, the function prints "USCG Auxiliary".
        - If the text "Zzzz" is found on the page, the function prints "Zzzz".
        - If neither text is found, the function prints the entire text content of the page.
        - The function includes error handling to catch and report issues such as network errors or problems with the web driver setup.

    Note:
        This script is designed to run in headless mode, making it suitable for use in 
        environments without a GUI, such as in automated CI/CD pipelines on GitHub Actions.

    Example:
        >>> check_app_status("https://ask-test.streamlit.app/")
        USCG Auxiliary
    """
    try:
        # Set up Chrome options for headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, required for running in containers
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        # Set up the Selenium WebDriver with Chrome in headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # remove options= paraamter for non-headless model
        

        driver.get(url)
        time.sleep(5) # give time for javascript to load
        page_text = driver.find_element(By.TAG_NAME, "body").text

        # Check for specific strings and print the found text
        if "Hosted with Streamlit" in page_text:
            print("App is working: 'Hosted with Streamlit'")
        elif "Zzzz" in page_text:
            print("App is down: 'Zzzz'")
        else:
            print("Text found on the page:")
            print(page_text)

    except Exception as e:
        print(f"An error occurred while trying to access {url}: {e}")
    finally:
        driver.quit()

# Run the check
check_app_status('https://uscg-auxiliary-ask.streamlit.app/')
