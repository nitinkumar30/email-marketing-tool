import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


def nameFromEmail(mail):
    username, domain = mail.split('@')
    domain_name = domain.split('.')[0]
    return domain_name


def sendMail(sender_email, sender_password, mail_template, mails_filename, subject, product_name, company_name):

    # Open the file for reading
    with open(mails_filename, 'r') as file:
        # Read each line in the file
        for mail in file:
            # Print the line to the console
            print(mail.strip())
            recipient_email = mail.strip()

            recipient_name = nameFromEmail(recipient_email)
            ceo_name = nameFromEmail(sender_email)

            # --------------------------------------------------
            # Create a message object
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient_email
            message['Subject'] = subject

            with open(mail_template) as file:
                template_text = file.read()

            # Use Jinja2 to render the template with some data
            template = Template(template_text)
            email_body = template.render(SUBJECT_NAME=subject, RECIPIENT_NAME=recipient_name, PRODUCT_NAME=product_name,
                                         EMAIL_ADDRESS=recipient_email, YOUR_NAME=ceo_name,
                                         YOUR_COMPANY_NAME=company_name)

            message.attach(MIMEText(email_body, 'plain'))

            # Connect to the SMTP server and login with the sender's credentials
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)

            # Send the email
            smtp_server.sendmail(sender_email, recipient_email, message.as_string())

            # Close the SMTP server connection
            smtp_server.quit()
