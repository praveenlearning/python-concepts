import re

domains = '''
https://www.google.com
http://isro.in
https://youtube.com
https://www.nasa.gov
'''

domain_name_pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

print(domain_name_pattern.sub(r'\2', domains))
