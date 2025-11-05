import urllib.request

try:
    with urllib.request.urlopen('http://localhost:8000/blog/') as response:
        html = response.read().decode('utf-8')

    # Check for internal links
    internal_links = []
    start = 0
    while True:
        pos = html.find('href="', start)
        if pos == -1:
            break
        start = pos + 6
        end_pos = html.find('"', start)
        if end_pos != -1:
            link = html[start:end_pos]
            if link.startswith('/') and not link.startswith('//'):
                internal_links.append(link)
            start = end_pos + 1

    print('Internal links found:')
    for link in internal_links:
        print(f'  {link}')

    # Check for broken links (basic check)
    broken_links = []
    for link in internal_links:
        try:
            with urllib.request.urlopen('http://localhost:8000' + link) as response:
                if response.getcode() != 200:
                    broken_links.append(link)
        except:
            broken_links.append(link)

    if broken_links:
        print('Broken internal links:')
        for link in broken_links:
            print(f'  {link}')
    else:
        print('No broken internal links found')

except Exception as e:
    print(f'ERROR: Could not connect to server: {e}')
