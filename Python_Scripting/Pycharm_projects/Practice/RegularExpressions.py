import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
800.555.1234
900.555.1234

Mr.Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

match   - Matches at the begining
seach   - Searched in entire string
findall - Find all the occurances (if group is there in the pattern, then searches only first pattern)
sub     - Substitues with 
"""

sentence  = "Start a sentence and then bring it to an end Start Start"


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
321-schafer@my-work.net
'''


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


print(r"\t Tab")


#pattern = re.compile(r'abc')
#pattern = re.compile(r'cba')
#pattern = re.compile(r'\.')
#pattern = re.compile(r'coreyms\.com')

#pattern = re.compile(r'\d')
#pattern = re.compile(r'\W')
#pattern = re.compile(r'\bHa')

#pattern = re.compile(r'^Start')
#pattern = re.compile(r'end$')

#pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'[1-5]')
#pattern = re.compile(r'[a-z]')
#pattern = re.compile(r'[a-zA-Z]')

#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')

#pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#
# sub_urls = pattern.sub(r'\2\3', urls)
# print(sub_urls)
#
# print(pattern)
#
# matches = pattern.finditer(urls)

pattern = re.compile(r'Start')

#matches = pattern.finditer(sentence)

matches = pattern.findall(sentence)
for match in matches:
    print(match)
    #print(match.group(2), " ", match.group(3))



matches = pattern.match(sentence)
print(matches)
# for match in matches:
#     print(match)
#     #print(match.group(2), " ", match.group(3))
#
# print(text_to_search[1:4])






phone_num_regex = re.compile(r'(\+91)?\s?\d{10}$')
mail_id_regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+')
url_regex = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


lst_phone_nums = []
lst_mail_ids = []
lst_urls = []

with open('RegEx.txt', 'r') as f:
    for line in f.readlines():
        if phone_num_regex.match(line.strip()):
            lst_phone_nums.append(line.strip())
        elif mail_id_regex.match(line.strip()):
            lst_mail_ids.append(line.strip())
        elif url_regex.match(line.strip()):
            lst_urls.append(line.strip())

print("Phone numbers are: ", lst_phone_nums)
print("Email ids are: ", lst_mail_ids)
print("URLs are: ", lst_urls)
