Welcome to the **Real-Time Market Reaction Dashboard**!  
This tool gives you **live stock/crypto data, charts, news**, and a **sentiment summary** — perfect for beginners and curious learners.

---

### 🔤 What is a *Ticker Symbol*?

A **ticker** is a unique short code used to identify a company or asset on the stock or crypto market.

Examples:
- `AAPL` → Apple Inc.
- `TSLA` → Tesla
- `BTC-USD` → Bitcoin vs US Dollar

You can look up symbols on [Yahoo Finance](https://finance.yahoo.com) or [CoinMarketCap](https://coinmarketcap.com).

---

### 📈 What Does This Dashboard Show?

#### ✅ **Candlestick Chart** (Price Movement)

A candlestick shows **how price changed** during a time period (like 5 minutes):

- 🟩 Green = Price went up
- 🔴 Red = Price went down
- **Wick** = Highest/lowest prices during that time

🔗 Learn in 5 mins: [Candlestick chart basics (video)](https://youtu.be/nSJP0kXrZ4k)

---

#### 📊 **Volume Chart**

Shows **how many shares or coins were traded**.  
High volume = More interest or activity.  
Use it with price to detect **buy/sell pressure**.

---

### 📰 **News Headlines + Sentiment**

We fetch the **5 latest news articles** about your ticker and use **NLP (TextBlob)** to guess if they’re:
- ✅ Positive
- ❌ Negative
- 😐 Neutral

This gives you **quick insight** into public or investor sentiment.

---

### 🧠 How to Use This Tool:

1. Type a symbol like `AAPL` or `BTC-USD`
2. See charts + news load instantly
3. Check the **sentiment label and emoji**
4. Watch how **prices respond to news**

---

### ⚙️ Built Using:

- [Streamlit](https://streamlit.io) – Web UI framework
- [yfinance](https://pypi.org/project/yfinance/) – Market data from Yahoo Finance
- [NewsAPI](https://newsapi.org) – News headlines
- [TextBlob](https://textblob.readthedocs.io/en/dev/) – Sentiment analysis
- [Plotly](https://plotly.com/python/) – Interactive charts

---

### 📚 Want to Learn More?

- What is a ticker? → [Investopedia Guide](https://www.investopedia.com/terms/t/ticker.asp)
- How to read candlesticks → [TradingView Academy](https://www.tradingview.com/education/)
- Sentiment analysis intro → [TextBlob Docs](https://textblob.readthedocs.io/en/dev/)

Happy learning 📊🚀