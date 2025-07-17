import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def get_text_from_doc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('body')
    if not body:
        print("No body found in document.")
        return None
    return body.get_text(separator='\n').strip().splitlines()

doc_url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
lines = get_text_from_doc(doc_url)

# Process the data into rows
rows = []
i = 0
while i + 2 < len(lines):
    try:
        # Skip empty lines and headers
        if not lines[i].strip() or "x-coordinate" in lines[i]:
            i += 1
            continue
            
        x = int(lines[i].strip())
        char = lines[i+1].strip()
        y = int(lines[i+2].strip())
        rows.append({'x': x, 'char': char, 'y': y})
        i += 3
    except (ValueError, IndexError) as e:
        print(f"Skipping invalid data at line {i}: {e}")
        i += 1

# Visualize the grid
if rows:
    grid = defaultdict(dict)
    max_x = max(row['x'] for row in rows)
    max_y = max(row['y'] for row in rows)
    
    for row in rows:
        grid[row['y']][row['x']] = row['char']
    
    
    print("\nSecret Message:")
    for y in range(max_y + 1):
        print(''.join([grid[y].get(x, ' ') for x in range(max_x + 1)]))
else:
    print("No valid data found to visualize.")