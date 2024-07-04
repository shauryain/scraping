import requests
from bs4 import BeautifulSoup
import csv

class PinterestScraper:
    def load_images(self):
        html = ""
        with open('images.html', 'r', encoding='utf-8') as images:
            for line in images:
                html += line
        return html
    
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        return [images['src'] for images in content.find_all('img')]

    def save_to_csv(self, urls, csv_filename):
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Image URL'])
            for url in urls:
                csvwriter.writerow([url])
        print(f"Saved {len(urls)} image URLs to {csv_filename}")

    def run(self):
        html = self.load_images()
        urls = self.parse(html)
        self.save_to_csv(urls, 'image_urls.csv')

if __name__ == '__main__':
    scraper = PinterestScraper()
    scraper.run()
