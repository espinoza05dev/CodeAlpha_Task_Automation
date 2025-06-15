import re
from datetime import datetime
import requests


def scrape_and_save_title(url, output_file='webpage_title.txt'):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        html_content = response.text

        title_match = re.search(r'<title[^>]*>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)

        if title_match:
            title = title_match.group(1).strip()
            title = re.sub(r'\s+', ' ', title)
        else:
            title = "No title found"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print(f"Successfully scraped title: '{title}'")
        print(f"Saved to: {output_file}")

        return title

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"Error processing the webpage: {e}")
        return None

if __name__ == "__main__":

    target_url = input("Enter the target URL: ")
    output_filename = "title.txt"
    scraped_title = scrape_and_save_title(target_url, output_filename)

    if scraped_title: print(f"\nTitle successfully saved to '{output_filename}'")
