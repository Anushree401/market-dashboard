import streamlit as st
from modules.market_fetcher import fetch_live_data 
from modules.visualizer import plot_price, plot_volume 
from modules.sentiment import summarize_sentiment
from modules.headline_fetcher import fetch_headlines

# --------------------------------------
# Page Config & Title
# --------------------------------------
st.set_page_config(page_title="Market Dashboard", layout="wide")
st.title("📊 Real-Time Market Reaction Dashboard")

# --------------------------------------
# Welcome Section from Markdown File
# --------------------------------------
with st.expander("ℹ️ About this Dashboard", expanded=True):
    with open("welcome.md", "r", encoding="utf-8") as f:
        welcome_md = f.read()
    st.markdown(welcome_md, unsafe_allow_html=True)

# --------------------------------------
# Reusable Function to Show Dashboard for Each Symbol
# --------------------------------------
def show_dashboard_for(symbol):
    st.markdown(f"---\n### 🔍 {symbol}")
    try:
        with st.spinner(f"Fetching data for {symbol}..."):
            df = fetch_live_data(symbol)
        st.success(f"Data fetched successfully for {symbol}!")

        # Price Chart
        st.subheader(f"📈 Candlestick Chart")
        st.plotly_chart(plot_price(df, symbol), use_container_width=True)

        # Volume Chart
        st.subheader(f"📊 Volume Chart")
        st.plotly_chart(plot_volume(df, symbol), use_container_width=True)

        # News & Sentiment
        news = fetch_headlines(symbol)
        if not news:
            st.warning("No recent news found.")
        else:
            sentiment = summarize_sentiment(news)
            st.subheader(f"📰 Sentiment Analysis")
            st.markdown(
                f"**Sentiment:** {sentiment['emoji']} {sentiment['label']} "
                f"(Score: {sentiment['score']:.2f})"
            )
            st.caption(f"Average sentiment score: {sentiment['score']:.2f}")

            st.markdown("##### 🗞 Latest Headlines")
            for headline in news:
                st.write("•", headline)

        # Last Updated
        last_time = df['Datetime'].iloc[-1]
        st.caption(f"🕒 Last updated: {last_time}")

    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {e}")

# --------------------------------------
# Ticker Input
# --------------------------------------
ticker = st.text_input("Enter stock or crypto ticker (e.g., AAPL, TSLA, BTC-USD):", "").upper()

# --------------------------------------
# If Ticker Given: Show Single Dashboard
# Else: Show Top 3 Trending Expandable Section
# --------------------------------------
if ticker:
    show_dashboard_for(ticker)
else:
    with st.expander("🔥 Explore Top 3 Trending Stocks", expanded=False):
        for symbol in ["AAPL", "TSLA", "NVDA"]:
            with st.expander(f"📌 {symbol}", expanded=False):
                show_dashboard_for(symbol)
