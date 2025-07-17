# 🕵️‍♀️ Secret Message Hackathon Challenge

This repository contains my solution to a fun and brain-teasing hackathon challenge hosted by **Data Annotation**.

## 🎯 Challenge Objective

Decode a hidden message from a public Google Doc that contains:
- (x, y) coordinates
- Characters (`█`, `░`)

## 🧠 My Approach

1. Scraped the public Google Doc using Python (`requests`, `BeautifulSoup`)
2. Parsed the data and mapped it onto a 2D grid
3. Printed the output grid to reveal the secret message

✅ **Decoded Message:** `KICMEDB`

## 🔧 Tools & Technologies
- Python
- requests
- BeautifulSoup
- Grid logic using nested lists

## 🖼️ Screenshots

### 📥 Input Snippet from Google Doc
![Input Screenshot](screenshots/input.png)

### 📤 Output Grid
![Output Screenshot](screenshots/output.png)

## 🚀 How to Run It Locally

```bash
git clone https://github.com/ThakurAyushi404/secret-message-Hackthonchallenge.git
cd secret-message-Hackthonchallenge
pip install -r requirements.txt
python decode.py
