from assets.info import *
from methods.scrapingEmails import scrap_mails
from methods.scrapingEmails_ import scrapEmails_
from methods.sendEmail import sendMail

# Open the file for writing nothing
with open(mails_filename, 'w') as file_:
    pass

# Open the file for reading
with open(urlLinks, 'r') as file:
    # Read each line in the file
    for url in file:
        # Print the line to the console
        print(url.strip())
        # scrap_mails(url, mails_filename)
        scrapEmails_(url, mails_filename)

# Open the file for reading
with open(urlLinks, 'r') as file:
    # Read each line in the file
    for url in file:
        # Print the line to the console
        print(url.strip())

        # scrap_mails(url, mails_filename)
        sendMail(sender_email, sender_password, mailTemplateFile, mails_filename, mail_subject, product_name, company_name)

