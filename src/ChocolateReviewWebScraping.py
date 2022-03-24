# Dataset Link: https://content.codecademy.com/courses/beautifulsoup/cacao/index.html

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import Dataset

chocolate = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(chocolate.content, "html.parser")

# print(soup)

# How are the Chocolate ratings distributed?

rating_tags = soup.find_all(attrs={"class": "Rating"})
# print(rating_tags)

ratings = []

for rating in rating_tags[1:]:
    rate_text = rating.get_text()
    rate_score = float(rate_text)
    ratings.append(rate_score)
# print(ratings)

plt.hist(ratings)
plt.title("A Histogram Showing the Number of Chocolate Bars and their Ratings.")
plt.xlabel("Chocolate Rating")
plt.ylabel("Number of Chocolate Bars")
plt.show()

# Which company makes the best chocolate?

company_tags = soup.select(".Company")
# print(company_tags)

names = []

for td in company_tags[1:]:
    names.append(td.get_text())

company_ratings = {"Company": names, "Ratings": ratings}
cacao_df = pd.DataFrame.from_dict(company_ratings)

mean_ratings = cacao_df.groupby("Company").Ratings.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)

# Is stronger chocolate better?

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
    percent = float(td.get_text().strip('%'))
    cocoa_percents.append(percent)

cocoa = {"Company": names, "Ratings": ratings, "CocoaPercentage": cocoa_percents}
cocoa_df = pd.DataFrame.from_dict(cocoa)

plt.scatter(cocoa_df.CocoaPercentage, cocoa_df.Ratings)
plt.title("A Scatter Graph Showing if the Cocoa Percentage is Rated Higher Than \n"
          "Those With a Lower Level of Cocoa")
plt.xlabel("Chocolate Cocoa Percentage")
plt.ylabel("Chocolate Rating")
z = np.polyfit(cocoa_df.CocoaPercentage, cocoa_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cocoa_df.CocoaPercentage, line_function(cocoa_df.CocoaPercentage), "r-")
plt.show()

# plt.clf()

# Where are the best cocoa beans grown?

origins = []
origin_tags = soup.select(".BroadBeanOrigin")

for td in origin_tags[1:]:
    country = td.get_text()
    origins.append(country)

beans = {"Bean Origin": origins, "CocoaPercentage": cocoa_percents}
beans_df = pd.DataFrame.from_dict(beans)

mean_percent = beans_df.groupby("Bean Origin").CocoaPercentage.mean()
ten_best = mean_percent.nlargest(10)
print(ten_best)

# Which countries produce the highest-rated bars?

countries = []
country_tags = soup.select(".CompanyLocation")

for td in country_tags[1:]:
    country = td.get_text()
    countries.append(country)

bars = {"CompanyLocation": countries, "Rating": ratings}
bars_df = pd.DataFrame.from_dict(bars)

mean_rating = bars_df.groupby("CompanyLocation").Rating.mean()
ten_best = mean_rating.nlargest(10)
print(ten_best)



