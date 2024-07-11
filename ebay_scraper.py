import requests
from bs4 import BeautifulSoup
import json

class EbayScraper:
    def __init__(self, product_url):
        self.product_url = product_url
    
    def get_product_data(self):
        response = requests.get(self.product_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            data = {}
            
            data['name'] = soup.find(id='itemTitle').get_text().replace('Details about  ', '')
            data['price'] = soup.find(id='prcIsum').get_text()
            data['seller'] = soup.find(id='mbgLink').get_text()
            data['shipping_price'] = soup.find(id='fshippingCost').get_text()
            data['product_url'] = self.product_url
            data['image_url'] = soup.find(id='icImg')['src']
            
            return data
        else:
            return None
    
    def display_product_data(self):
        product_data = self.get_product_data()
        if product_data:
            print(json.dumps(product_data, indent=4))
        else:
            print("Failed to retrieve data from the product page")

if __name__ == "__main__":
    product_url = "https://www.ebay.com/itm/your_product_id"
    ebay_scraper = EbayScraper(product_url)
    ebay_scraper.display_product_data()
