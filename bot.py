import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import keys

# Set the path to the chromedriver executable - make sure version matches with your version of chrome.
CHROMEDRIVER_PATH = 'chromedriver.exe'

# Set the URL of the web page you want to scrape, alternate url of another product for testing
url_to_scrape = 'https://www.ninjakitchen.com/products/-ninja-creami-deluxe-11-in-1-ice-cream-and-frozen-treat-maker-zidNC501'
#url_to_scrape = 'https://www.ninjakitchen.com/products/ninja-foodi-flexbasket-air-fryer-with-7qt-megazone-zidDZ071'

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

chrome_service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

cont = True

while cont == True:
    #Navigate to the URL
    driver.get(url_to_scrape)

    try:
        wait = WebDriverWait(driver, 10)
        target_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'price-container')))
        scraped_data = target_element.text
        print("Scraped Data:", scraped_data)
    except Exception as e:
        print("Error:", e)

    #Evaluate if product is "Out of Stock"
    if "Stock" not in scraped_data:
        cont = False
    else:
    # Wait for 5 minutes before re-scraping
        time.sleep(300)  # 300 seconds = 5 minutes

# Close the browser (this won't be reached in an infinite loop)
driver.quit()

# Email configuration
sender_email = keys.sender_email
receiver_emails = keys.receiver_emails # Pass in a list, even if it is a single item
subject = "Ninja Creami Stock Alert"
body = "There has been a restock of the Ninja Creami on the Ninja website. See shop link here: " + url_to_scrape

# Your Gmail credentials (use an App Password if 2-factor authentication is enabled)
smtp_server = keys.smtp_server
smtp_port = keys.smtp_port
username = keys.username
password = keys.password

#Create and send the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() 
    server.login(username, password)
    server.sendmail(sender_email, receiver_emails, message.as_string())
    print("Email sent successfully to:", ", ".join(receiver_emails))
except Exception as e:
    print("An error occurred:", str(e))
finally:
    server.quit()

