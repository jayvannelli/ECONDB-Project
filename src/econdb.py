import pandas as pd
import requests

import streamlit as st
from src import constants

ECONDB_BASE_URL = "https://www.econdb.com/api/series/"

def get_available_country_indicators(country):
    ticker_and_descriptions = {}

    formatted_country = country.replace(" ", "+")

    starter_req_url = ECONDB_BASE_URL + f"?page=1&search={formatted_country}&format=json"
    starter_req = requests.get(starter_req_url).json()

    pages = starter_req['pages']
    counter = 2

    for i in starter_req['results']:
        if 'Exchange rate v dollar' in i['description']:
            pass
        else:
            ticker_and_descriptions[i['description'].split("-")[1]] = i['ticker']
    
    if pages == 1:
        pass
    else:
        while counter <= pages:
            req_url = ECONDB_BASE_URL + f"?page={counter}&search={formatted_country}&format=json"
            req = requests.get(req_url).json()

            for i in req['results']:
                if 'Exchange rate v dollar' in i['description']:
                    pass
                else:
                    ticker_and_descriptions[i['description'].split("-")[1]] = i['ticker']
            
            counter += 1

    return ticker_and_descriptions

def get_economic_data(full_indicator_symbol, return_df):
    req_url = ECONDB_BASE_URL + f"{full_indicator_symbol}/?format=json"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req['data'])
        df = df.set_index("dates")
    else:
        df = req

    return df