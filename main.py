from exa_py import Exa
from dotenv import load_dotenv
import os

load_dotenv()
exa = Exa(os.getenv('EXA_API_KEY'))

query = input('Search here: ')

response = exa.search(
    query,
    num_results=5,
    type='keyword',
    include_domains=['https://www.tiktok.com'],
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
