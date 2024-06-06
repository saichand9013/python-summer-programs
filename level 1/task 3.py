#level1-T3
#Task: Email Validator
#Develop a Python function that validates whether a given string is a valid email address. Implement checks for the format, including the presence of an "@" symbol and a domain name

import re

def is_valid_email(email):
    
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Simple regex pattern for basic email validation
    
    if re.match(email_pattern, email):  # Match the pattern with the email string
        return "true the email is valid email"
    return "false this is not a valid email"

# Test cases
print(is_valid_email("test@example.com"))  # True
print(is_valid_email("invalid-email.com"))  # False
print(is_valid_email("another.test@domain.co.uk"))  # True
print(is_valid_email("wrong@domain"))  # False
