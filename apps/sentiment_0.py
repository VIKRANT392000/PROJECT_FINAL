import streamlit as st
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def app():
    def sentiment_scores(sentence):
        
       
        analyzer = SentimentIntensityAnalyzer()
        sentiment= analyzer.polarity_scores(sentence)
        return sentiment
        
    st.title("Reviews Sentiment Analyzer")
    st.subheader("Let us check the Sentiment")

    if st.checkbox("Show Sentiment of Text"):

        message = st.text_area("Enter the Summary to be analysed",)
        if st.button("Output"):
            sentiment_dict= sentiment_scores(message)
            st.write(sentiment_dict)
            if sentiment_dict['compound'] > -1 and sentiment_dict['compound'] <= -0.34:
                st.success("The Sentiment is Negative🙁🙁")
            elif sentiment_dict['compound'] > -0.34 and sentiment_dict['compound'] <= 0.32:
                st.success ("The Sentiment is Neutral😐😐")
            elif sentiment_dict['compound'] > 0.32  and sentiment_dict['compound'] <= 1: 
                st.success ("The Sentiment is Positive😊😊")
            


        
            