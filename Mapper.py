#!/usr/bin/env python
import sys
import re

# Regular expression to match URLs (http or https)
# url_pattern = re.compile(r'https?://[^\s"\'<>]+')
url_pattern = re.compile(r'href=\"(.*?)\"')

for line in sys.stdin:
    line = line.strip()
    # Find all URLs in the line
    urls = url_pattern.findall(line)
    for url in urls:
        print(f"{url}\t1")
    
