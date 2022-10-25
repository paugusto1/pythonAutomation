import os
import sys

from news.constraints import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from datetime import date, datetime, timedelta
from prettytable import PrettyTable
import pandas as pd


class News(webdriver.Chrome):

    def __init__(self, driverpath = DRIVERS_PATH, teardown = False, headless = False):
        self.driver_path = driverpath
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.headless = headless
        super(News, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self, option = 'all'):
        self.get(BASE_URL)

        try:
            self.find_element(by= By.ID, value='onetrust-accept-btn-handler').click()
        except:
            pass

        self.find_element(by= By.ID, value=option).click()

    def listReviews(self, score="all", max_number=10):
        reviews = self.find_elements(by= By.XPATH, value="//a[@class='item-body']")
        res = []

        print(reviews)

        for i in reviews:

            aux = []

            aux.append(i.find_element(by = By.XPATH, value= "./descendant::span[contains(@class, 'item-title')]").text.replace("Review", ""))
            aux.append(
                i.find_element(by=By.XPATH, value="./descendant::figcaption").text)
            aux.append("".join(i.find_element(by = By.XPATH, value= "./descendant::div[contains(@class, 'item-subtitle')]").text.split(sep="-")[1:]))

            res.append(aux)

            if len(res) >= max_number:
                break

        table = PrettyTable(field_names=['Name', 'Score', 'Summary'])
        table.add_rows(res)
        print(table)

        dic = {'name': [i[0] for i in res], 'score': [i[1] for i in res], 'summary':[i[2] for i in res]}
        df_reviews = pd.DataFrame(dic)
        now = datetime.now()
        time_str = now.strftime("%d_%m_%y")
        application_path = os.path.dirname(sys.executable)
        file_name = os.path.join(application_path, f"results_{time_str}.csv")
        print(file_name)
        df_reviews.to_csv(file_name)




