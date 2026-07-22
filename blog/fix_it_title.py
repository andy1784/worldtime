import re
import sys

file_path = 'country-time-zones-by-utc-offset-it.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# English title
en_title = 'List of Countries by UTC Offset: Every Country (2026)'
# Italian translation
it_title = 'Elenco dei paesi per offset UTC: Ogni paese (2026)'

# Replace <title>...</title>
content = re.sub(r'<title>.*?</title>', f'<title>{it_title}</title>', content)
# Replace <meta name="title" content="..."/>
content = re.sub(r'<meta name="title" content="[^"]*"/>', f'<meta name="title" content="{it_title}"/>', content)
# Replace <meta property="og:title" content="..."/>
content = re.sub(r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{it_title}"/>', content)
# Replace <meta name="twitter:title" content="..."/>
content = re.sub(r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{it_title}"/>', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Updated {file_path} with Italian title: {it_title}')