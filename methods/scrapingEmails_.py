import requests
from bs4 import BeautifulSoup


# Define the URL of the website you want to scrape
# url = 'http://universdeck.com/'
def scrapEmails_(url, mails_bundle):
    # Send a GET request to the website and store the response
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the tags that may contain email ids (you may need to adjust this to match the structure of the website)
    email_tags = soup.find_all(['a', 'p', 'span', 'div'])

    def decode_email(encoded_string):
        """Decode a string encoded with Cloudflare's email obfuscation."""
        k = int(encoded_string[:2], 16)
        decoded = ''.join([chr(int(encoded_string[i:i + 2], 16) ^ k) for i in range(2, len(encoded_string), 2)])
        return decoded

    # Loop through each tag and extract any email ids it contains
    emails = set()
    for tag in email_tags:
        if tag.has_attr('href') and 'mailto:' in tag['href']:
            email = tag['href'][7:]
            emails.add(email)
        elif tag.has_attr('data-cfemail'):
            email = decode_email(tag['data-cfemail'])
            emails.add(email)
        else:
            for string in tag.stripped_strings:
                if '@' in string:
                    emails.add(string)

    # Print the list of email ids found
    print(emails)

    # Define the name of the output file
    # output_file = 'data.txt'

    # Open the output file for writing
    with open(mails_bundle, 'a') as file:
        # Loop through each data element in the set
        for mail in emails:
            # Write the data element to a new line in the output file
            file.write(mail + '\n')
