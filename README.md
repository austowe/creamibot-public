# creamibot-public

CreamiBot was a small project I made in a moment of desperation when my Amazon Ninja Creami order was canceled. The Ninja Creami deluxe was out of stock, so I decided to make a bot to let me know when it became available. I scraped Ninja's own website, as you can get 20% off by signing up for SMS/email marketing.

## Dependencies

- Selenium
- smtplib

## Instructions

1. Create a `keys.py` file in the project directory containing the following with your own email credentials:

```python
smtp_server = 'your_smtp_server'
smtp_port = 'your_smtp_port'
username = 'your_username'
password = 'your_password'
sender_email = 'from_email'
receiver_emails = ['to_email']
```

Replace the placeholders with your actual email credentials. `sender_email` should be the email address you want to send from, and `receiver_emails` should be a list of email addresses you want to send notifications to.
