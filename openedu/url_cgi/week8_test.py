"""
from urllib.parse import urlparse
import urllib.request
import re

url=input()
url_res=urlparse(url)
print(tuple(url_res))
url_file=urllib.request.urlopen(url)
html_file=url_file.read().decode('utf-8')
pattern = re.compile(r'(?is)<h1[^>]*>(.+?)</h1>')
for gr in re.findall(pattern, html_file):
    print(gr)
############
"""
from urllib.parse import urlparse
import urllib.request
import re
#import htmlparser

url=input()
url_res=urlparse(url)
print(tuple(url_res))
url_file=urllib.request.urlopen(url)
html_file=url_file.read().decode('utf-8')
#pattern = re.compile(r'(?is)<h1[^>]*>(.+?)</h1>')
pattern = re.compile(r'<h1>(.*?)</h1>')
print(*re.findall(pattern, html_file))
for gr in re.findall(pattern, html_file):
    print(gr)
#hrml_dict=htmlparser.parse(html_file)
#for h in htmldict['h1']:
#	print(h)