import matplotlib.pyplot as plt
import streamlit as st

def plot_economic_data(df, country, indicator):
    with plt.style.context('dark_background'):
        df.plot()
        plt.title(f"{country} - {indicator}")
        plt.xlabel("Years")
        plt.ylabel(f"{indicator}")
        plt.xticks(rotation=45)
        st.pyplot(plt)