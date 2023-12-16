# Import Selenium webdriver and support classes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open input file and read domains into list
with open('domains.txt') as f:
    domains = f.read().splitlines()

# Open output file for writing results
with open('results.txt', 'w') as out_file:
    # Open captcha file for writing CAPTCHA detections
    with open('captcha.txt', 'a') as captcha_file:
        # Iterate through each domain
        for domain in domains:

            # Launch headless Chrome browser
            browser = webdriver.Chrome()

            # Navigate to the website
            browser.get("https://sitereview.bluecoat.com/#/")

	    # Set default name variable
            name = domain

            # Find search box, input domain, hit Enter
            search_box = browser.find_element(By.ID, "txtUrl")
            search_box.clear()
            search_box.send_keys(domain)
            search_box.send_keys(Keys.RETURN)

            # Check for CAPTCHA
            try:
                captcha = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "imgCaptcha")))
                captcha_message = f"Captcha detected for domain {domain}. Stopping execution.\n"
                print(captcha_message)
                captcha_file.write(captcha_message)
                browser.quit()
                continue
            except:
                pass  # No captcha found, continue execution

            # Try getting details of a categorized domain
            try:
                elm1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "lnkRatedSite")))
                elm2 = browser.find_element(By.ID, "txtUrlShortener")

                # Check for URL shortener page
                if elm2:
                    categories = "The URL you entered is a URL shortening service"
                else:
                    # Extract name and categories from elements
                    name = elm1.text
                    categories = ",".join([x.text for x in browser.find_elements(By.CLASS_NAME, "clickable-category")])

            except:
                # If error, try checking for uncategorized domain page
                try:
                    elm = browser.find_element(By.CLASS_NAME, "url-display")
                    if "ng-star-inserted" in elm.get_attribute("class"):
                        categories = ",".join([x.text for x in browser.find_elements(By.CLASS_NAME, "clickable-category")])
                    else:
                        categories = "This_URL_has_not_yet_been_rated"

                except:
                    # If no match, set default category text
                    categories = "This_URL_has_not_yet_been_rated"

            # Write domain results to output file
            out_file.write(f"{domain},{categories}\n")

            # Close browser instance
            browser.quit()

print("Scraping complete, output saved in results.txt")