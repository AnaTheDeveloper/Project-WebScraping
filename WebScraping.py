import requests
import requests as Requests
import bs4 as BeautifulSoup4
import lxml

if __name__ == '__main__':

    # -------------------------------------UDEMY COURSE NOTES----------------------------------

    # Prints out the html page
    result = Requests.get("https://en.wikipedia.org/wiki/Valorant")
    type(result)
    # print(result.text)

    # Store result of request in a variable
    # webpage_result = result.thisIsTheNewVariable
    # print(webpage_result)

    # Prints out the html page but without the indentation and makes it easier to read
    soup = BeautifulSoup4.BeautifulSoup(result.text, "lxml")
    # print(soup)

    # Find tag with that name
    # print(soup.select('title'))

    # Grab actual text
    # print(soup.select('title')[0].getText())

    site_paragraphs = soup.select("p")
    # print(site_paragraphs[0].getText())

    # Grabbing a class
    res = requests.get('https://en.wikipedia.org/wiki/Valorant')
    soup2 = BeautifulSoup4.BeautifulSoup(res.text, "lxml")
    second_item = soup2.select('.toc'[1])
    # for item in soup.select('.toc'):
    #     print(item.text)

    # https://toscrape.com/

    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    base_url.format('20')

    res2 = requests.get(base_url.format(1))
    soup3 = BeautifulSoup4.BeautifulSoup(res2.text, 'lxml')
    products = soup3.select(".product_pod")
    example = products[0]
    # print(example)
    # print(example.select(".star_rating.Three"))

    # Use dot to fill in any spaces

    # two_star_titles = []
    # for n in range(1, 51):
    #     scrape_url = base_url.format(n)
    #     res = requests.get(scrape_url)
    #     soup = BeautifulSoup4.BeautifulSoup(res.text, 'lxml')
    #     books = soup.select(".product_pod")
    #     for book in books:
    #         if len(book.select('.star-rating.Two')) != 0:
    #             book_title = book.select('a')[1]['title']
    #         two_star_titles.append(book_title)

    # -------------------------------------CODE ACADEMY NOTES------------------------------------

    # webpage_response = requests.get('example.html')
    # webpage = webpage_response.content
    # soup = BeautifulSoup(webpage, "html.parser")
    # turtle_links = soup.find_all("a")
    #     # print(turtle_links)
    # links = []
    # #go through all of the a tags and get the links associated with them"
    # for a in turtle_links:
    #   links.append(prefix+a["href"])
    #
    # #Define turtle_data:
    # turtle_data = {}
    #
    # #follow each link:
    # for link in links:
    #   webpage = requests.get(link)
    #   turtle = BeautifulSoup(webpage.content, "html.parser")
    #   turtle_name = turtle.select(".name")[0].get_text()
    #
    #   stats = turtle.find("ul")
    #   stats_text = stats.get_text("|")
    #   turtle_data[turtle_name] = stats_text.split("|")
    #
    # turtle_df = pd.DataFrame.from_dict(turtle_data, orient='index')
    # print(turtle_df)
    # for child in soup.div.children:
    #   print(child)
    # print(soup)
    # print(soup.p.string)

    # Using Regex
    # import re
    # soup.find_all(re.compile("h[1-9]"))

    # Using Lists
    # soup.find_all(['h1', 'a', 'p'])

    # Using Attributes
    # soup.find_all(attrs={'class':'banner'})
    # soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

    # Using a function
    # def has_banner_class_and_hello_world(tag):
    #     return tag.attr('class') == "banner" and tag.string == "Hello world"
    # soup.find_all(has_banner_class_and_hello_world)

    # Select CSS
    # soup.select(".recipeLink")
    # soup.select("#selected")
    # for link in soup.select(".recipeLink > a"):
    #   webpage = requests.get(link)
    #   new_soup = BeautifulSoup(webpage)
    # -------------------------------------------



