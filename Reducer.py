#!/usr/bin/env python
#!/usr/bin/env python3
import sys

current_url = None
current_count = 0
url = None

for line in sys.stdin:
    line = line.strip()
    try:
        url, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # Skip malformed lines
        continue

    if current_url == url:
        current_count += count
    else:
        if current_url:
            if current_count > 5:
                print(f"{current_url}\t{current_count}")
        current_count = count
        current_url = url

# Don’t forget the last one
if current_url == url:
    if current_count > 5:
        print(f"{current_url}\t{current_count}")
