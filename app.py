import streamlit as st
from src import constants, econdb, charts

st.title("Deep Dive into ECONDB")

left_column, right_column = st.columns(2)
with left_column:
    selected_country = st.selectbox("Country:", options=constants.country_abbreviations.keys())
with right_column:
    possible_indicators = econdb.get_available_country_indicators(country=selected_country)
    indicator_selection = st.selectbox("Data:", possible_indicators.keys())

data = econdb.get_economic_data(full_indicator_symbol=possible_indicators[indicator_selection], return_df=True)

data_tab, chart_tab = st.tabs(["RAW DATA", "CHART"])
with data_tab:
    st.dataframe(data)

with chart_tab:
    charts.plot_economic_data(data, country=selected_country, indicator=indicator_selection)
    st.dataframe(data)