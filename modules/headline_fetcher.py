import streamlit as st
import requests

def fetch_headlines(ticker):
    api_key = st.secrets.get("NEWS_API_KEY")
    if not api_key:
        st.error("API key for news not found. Please set it in Streamlit secrets.")
        return []
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] != 'ok':
        st.error(f"Error fetching news: {data.get('message', 'Unknown error')}")
        return []
    headlines = [article["title"] for article in data["articles"][:5]]  # Fetch top 5 headlines

    return headlines