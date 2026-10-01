import re

text = """
Contact us at alice@example.com or bob.smith123@gmail.com.
You can also email support@company.co.uk.
"""

# Regular expression for finding email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all matching email addresses
emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)
