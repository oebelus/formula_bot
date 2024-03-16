import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

url = "https://www.fiaformulae.com/en/calendar"
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

formula_e_cards = soup.find_all(class_="race-card__round-info")
formula_e = {}

for card in formula_e_cards:
    title = card.find("span", class_="race-card__round-name").text
    start_date = card.find("span", class_="race-card__round-day notranslate").text
    month = card.find("span", class_="race-card__round-month").text
    location = card.find("span", class_="race-card__round-location").text
    
    formula_e[title] = {
        "start_date": start_date,
        "month": month,
        "location": location
    }

driver.quit()

formula_one_url = "https://www.formula1.com/en/racing/2024.html"
formula_one_page = requests.get(formula_one_url)

formula_e_url = "https://www.fiaformulae.com/en/calendar"

formula_one_soup = BeautifulSoup(formula_one_page.content, "html.parser")

formula_one_cards = formula_one_soup.find_all("fieldset", class_="race-card-wrapper")

formula_one = {}

for card in formula_one_cards: 
    title = card.find("legend", class_="card-title").text.strip()
    start_date = card.find("span", class_="start-date").text.strip()
    end_date = card.find("span", class_="end-date").text.strip()
    month = card.find("span", class_="month-wrapper").text.strip()
    location = card.find("div", class_="event-place").text.strip()
    event_title = card.find("div", class_="event-title").text.strip()

    formula_one[title] = {
        "start_date": start_date,
        "end_date": end_date,
        "month": month,
        "location": location,
        "event_title": event_title
    }

with open("formula_one.json", "w") as outfile: 
    json.dump(formula_one, outfile)

with open("formula_e.json", "w") as outfile: 
    json.dump(formula_e, outfile)