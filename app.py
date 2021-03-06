import streamlit as st
from multiapp import MultiApp
import matplotlib
import seaborn
import plotly
from apps import home, sentiment_2 ,sentiment_1, sentiment_0

app = MultiApp()

st.markdown("""
# Amazon Reviews Sentiment Analyzer

This Amazon Reviews Sentiment Analyzer app is using the [Vader Sentiment](https://github.com/cjhutto/vaderSentiment) Python Library.

""")


app.add_app("Home", home.app)
app.add_app("Web Scrapping", sentiment_2.app)
app.add_app("Online Review Analyzer", sentiment_1.app)
app.add_app("Text Review Analyzer", sentiment_0.app)
# The main app
app.run()
