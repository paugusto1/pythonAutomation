# import pandas as pd
# import camelot
# from news import *
from news.news import News

# listEps = pd.read_html("https://en.wikipedia.org/wiki/List_of_Naruto:_Shippuden_episodes")
# print(len(listEps))
# print(listEps[2])
#
# csv = pd.read_csv("https://www.football-data.co.uk/new/BRA.csv")
#
# print(csv.keys())
#
# csv.rename(columns={'HG':'home_goals', 'AG': 'away_goals'}, inplace=True)
#
# print(csv.keys())
#
# pdf = camelot.read_pdf('https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf')
# print(pdf)

with News(teardown=True, headless=False) as bot:
    bot.land_first_page(option = 'all')
    bot.listReviews()
