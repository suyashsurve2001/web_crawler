import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

st.title("Web Crawler")

url = st.text_input("Enter URL", "https://www.google.com")

if st.button("Get Links"):
    links = get_links(url)
    st.write("Links on the page:")
    for link in links:
        st.write(link)
    print('Links:')
    