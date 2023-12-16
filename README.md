Domain Categorization Script

Overview

This repository contains a Python script for automating the process of categorizing domains. The script utilizes Selenium WebDriver to interact with a specific website for domain categorization. It reads a list of domains from a file, processes each domain through the website, and handles CAPTCHAs if encountered.


Features

Automated Domain Categorization: Processes a list of domains and categorizes them based on the information retrieved from a specified website.
CAPTCHA Detection: Detects the presence of CAPTCHA during the process and logs the occurrence.
Result Logging: Stores the categorization results and CAPTCHA detections in separate files for easy review.

Files in the Repository

domain_categorization.py: The main Python script for categorizing domains.
domains.txt: Input file where you should list the domains to be categorized, one per line.
results.txt: Output file where the script logs the categorization results.
captcha.txt: Output file where the script logs any CAPTCHA detections.

Requirements

Python 3.x 
Selenium WebDriver 4.x
Chrome WebDriver (compatible with your Chrome version)

Setup and Execution

Install Python: Ensure Python 3.x is installed on your system.
Install Selenium: Install Selenium WebDriver using pip: pip install selenium.
Set up Chrome WebDriver: Download and set up Chrome WebDriver, ensuring it's added to your system's PATH.
Prepare domains.txt: Populate domains.txt with the domains you wish to categorize, one domain per line.
Run the Script: Execute the script with python domain_categorization.py.

Output

results.txt: Contains the domain name and its corresponding categories. If a domain is recognized as a URL shortening service or hasn't been rated, specific messages are recorded.
captcha.txt: Contains messages for each domain where a CAPTCHA was detected, indicating that the script could not process that domain.
