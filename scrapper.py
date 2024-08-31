# We thought of giving you a gift this new year by sharing the web scraping script
# Understanding the script before using is always appreciated
# We left few blanks in the script for your exploration
# Make sure to replace FILL_IN_THE_BLANK in the code to make it work

import requests
import numpy as np
from bs4 import BeautifulSoup

# def scrapper(imdbId):
#     id = str(int(imdbId))
#     n_zeroes = 7 - len(id)
#     new_id = "0"*n_zeroes + id
#     URL = f"https://www.imdb.com/title/tt{new_id}/"
#     request_header = {'Content-Type': 'text/html; charset=UTF-8', 
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
#                       'Accept-Encoding': 'gzip, deflate, br'}
#     response = requests.FILL_IN_THE_BLANK(URL, headers=request_header)
#     soup = FILL_IN_THE_BLANK(response.text)
#     imdb_rating = soup.find('FILL_IN_THE_BLANK', attrs={'FILL_IN_THE_BLANK' : 'FILL_IN_THE_BLANK'})
#     return imdb_rating.text if imdb_rating else np.nan

# def scrapper(imdbId):
#     id = str(int(imdbId))
#     n_zeroes = 7 - len(id)
#     new_id = "0" * n_zeroes + id
#     URL = f"https://www.imdb.com/title/tt{new_id}/reviews"
#     request_header = {
#         'Content-Type': 'text/html; charset=UTF-8', 
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
#         'Accept-Encoding': 'gzip, deflate, br'
#     }
#     response = requests.get(URL, headers=request_header)
#     print(response.text)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     imdb_rating = soup.find('span', attrs={'itemprop': 'ratingValue'})
#     return imdb_rating.text if imdb_rating else np.nan

# print(scrapper('0114709'))

# import requests
# from bs4 import BeautifulSoup

# def scrape_imdb_rating(imdb_id):
#     url = f'https://www.imdb.com/title/tt{imdb_id}/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
    
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
        
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         rating_element = soup.select_one('span[class*="AggregateRatingButton__RatingScore"]')
        
#         if rating_element:
#             rating = rating_element.text.strip()
#             return float(rating)
#         else:
#             return None
    
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return None

# # Example usage
# imdb_id = '0114709'  # The Shawshank Redemption
# rating = scrape_imdb_rating(imdb_id)
# if rating:
#     print(f"The IMDb rating for tt{imdb_id} is: {rating}")
# else:
#     print("Unable to retrieve the rating.")

import requests
from bs4 import BeautifulSoup
import numpy as np

def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0"*n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    print(f"Accessing URL: {URL}")  # Debug print
    
    request_header = {'Content-Type': 'text/html; charset=UTF-8', 
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
    
    response = requests.get(URL, headers=request_header)
    print(f"Response status code: {response.status_code}")  # Debug print
    
    soup = BeautifulSoup(response.text, 'html.parser')
    imdb_rating = soup.find('span', attrs={'class': 'sc-eb51e184-1 ljxVSS'})
    
    if imdb_rating:
        print(f"Found rating: {imdb_rating.text}")  # Debug print
    else:
        print("Rating not found")  # Debug print
    
    return imdb_rating.text if imdb_rating else np.nan

# Test the function
result = scrapper('0114709')
print(f"Final result: {result}")