import requests
from bs4 import BeautifulSoup

# set initial url
URL = "https://books.toscrape.com/"
next_url = ""

# Print out title for book list
print("All books with three stars")
print()

for i in range(0,50): 

    # Get html and pass to parser
    # Loop to correct url for page 3 forward
    if i < 2:
        this_url = URL + next_url.replace(" ", "")
        page = requests.get(this_url)
    else:
        this_url = URL + "catalogue/" + next_url.replace(" ", "")
        page = requests.get(this_url)

    # Pass HTML to parser
    soup = BeautifulSoup(page.content, "html.parser")
    default_container = soup.find(id="default")

    # Finds all books on page with three star ratings
    rating = default_container.find_all("p", {"class": "star-rating Three"})

    # Finds parent of elements so that other information about the book can be scraped
    parent_elements = [
        element.parent for element in rating
    ]

    # Finds the title of the book and prints to console
    for parent in parent_elements:
        element_title = parent.find("img", alt=True)
        print(element_title['alt'])
        print()
    
    # Find URL for next page, stop on page 50
    if i < 49:
        next_page = default_container.find("li", {"class": "next"})
        next_anchor = next_page.find("a")
        next_href = next_anchor['href']
        next_url = ' '.join(next_href)
