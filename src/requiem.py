import os
import re
import requests
import logging
import argparse
from urllib.parse import urljoin, urlparse


class Scraper:
    def __init__(self, url, depth=1):
        self.url = url
        self.depth = depth
        self.visited_urls = set()
        logging.basicConfig(filename='scraper.log', level=logging.INFO)

    def scrape(self, url=None, current_depth=0):
        """
        Recursively scrape all the links on a given page up to a certain depth.
        """
        if url is None:
            url = self.url

        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        # Get the page content
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            logging.exception(f"Error requesting {url}: {e}")
            return

        # Extract all the links on the page
        links = re.findall(r'href="(.*?)"', response.text)

        # Download all the files on the page
        file_urls = re.findall(r'<a.*?href="(.*?)".*?>', response.text)
        base_url = urlparse(url).netloc
        for file_url in file_urls:
            absolute_url = urljoin(url, file_url)
            self.download(absolute_url, base_url)

        # Recursively scrape all the links on the page
        if current_depth < self.depth:
            for link in links:
                absolute_url = urljoin(url, link)
                self.scrape(absolute_url, current_depth + 1)

    def download(self, url, base_url):
        # Create the directory structure
        parsed_url = urlparse(url)
        path = parsed_url.path
        if not path:
            path = '/'
        dir_path = os.path.join(base_url, os.path.dirname(path)[1:])
        if not dir_path:
            dir_path = '/'
        os.makedirs(dir_path, exist_ok=True)

        # Generate a unique file name
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(dir_path, file_name)
        file_count = 0
        while os.path.exists(file_path):
            file_count += 1
            file_path = os.path.join(dir_path, f"{file_name}_{file_count}")

        # Download the file
        response = requests.get(url)
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Web scraper')
    parser.add_argument('url', type=str, help='URL to start scraping from')
    parser.add_argument('-d', '--depth', type=int, default=1, help='Maximum depth to scrape')
    args = parser.parse_args()

    scraper = Scraper(args.url, args.depth)
    scraper.scrape()


if __name__ == '__main__':
    print("""wel come to : \n \n
    
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░░░░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██████████░░▄▀░░█
█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█
█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n \n \n""")
    main()