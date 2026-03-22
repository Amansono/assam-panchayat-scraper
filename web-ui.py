import streamlit as st
from scraper_logic import AssamVoterScraper

st.title("Assam Panchayat Electoral Roll Scraper")

# User Inputs
dist = st.sidebar.text_input("Enter District")
zilla = st.sidebar.text_input("Enter Zilla Parishad")
gp = st.sidebar.text_input("Enter GP Name")
ward = st.sidebar.text_input("Enter Ward")

if st.button("Fetch List"):
    with st.spinner('Scraping data... please wait.'):
        scraper = AssamVoterScraper()
        result = scraper.get_data(dist, zilla, gp, ward)
        st.success(result)
