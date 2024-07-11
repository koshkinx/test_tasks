import requests
from prettytable import PrettyTable

class CountryInfo:
    def __init__(self):
        self.api_url = "https://restcountries.com/v3.1/all"
    
    def get_country_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def display_country_data(self):
        country_data = self.get_country_data()
        if country_data:
            table = PrettyTable()
            table.field_names = ["Country Name", "Capital", "Flag URL"]
            
            for country in country_data:
                name = country.get("name", {}).get("common", "N/A")
                capital = country.get("capital", ["N/A"])[0]
                flag_url = country.get("flags", {}).get("png", "N/A")
                
                table.add_row([name, capital, flag_url])
            
            print(table)
        else:
            print("Failed to retrieve data from the API")

if __name__ == "__main__":
    country_info = CountryInfo()
    country_info.display_country_data()
