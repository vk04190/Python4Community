#! python3

import re
import pyperclip

# TODO: Create a regex for phone number
regexPhone = re.compile(r'''
 # 415-555-0000,555-0000,(415) 555-0000,555-0000 ext 12345,ext. 12345,x12345
(
    ((\d\d\d)|(\(\d\d\d\)))? #area code (optional)
    (\s|-)                  # first sepertater
    \d\d\d                  # first 3 digit
    (\s|-)                  #2nd sperater
    \d\d\d\d                # last 4 digit
    (((ext(\.)?\s)|x)        #Extension word-part
    (\d{2,5}))?             #extension
)
''', re.VERBOSE)

#  Create a regex for Email Address
regexEmail=re.compile(r'''
#some.+_thing@something.something
[a-zA-Z0-9_.+]+     #name Part
@                   # @ Symbol
[a-zA-Z0-9_.+]+   #domain Name Part
''',re.VERBOSE)

#  get the text off the clipboard
text=pyperclip.paste()
#  Extract the Email/PHone from the text
extractphone=regexPhone.findall(text)
extractEmail=regexEmail.findall(text)
allPhoneNumbers=[]
for phone in extractphone:
    allPhoneNumbers.append(phone[0])

# print(allPhoneNumbers)
# print(extractEmail)
# Copy the Extracted Email/Phone to the clipboard
result='\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractEmail)
print (result)