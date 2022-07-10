import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def app():

    def fetch_data():
        link=st.text_input("Enter product review link")
        url=link
        if not url:
            st.stop()
        if url:   
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            reviews = soup.find_all('div', {'data-hook': 'review'})
            reviewlist = []
            
            def get_soup(url):
                r = requests.get(url,params={'url': url, 'wait': 5})
                soup = BeautifulSoup(r.text, 'html.parser')
                return soup
                    
                df = pd.DataFrame(reviews)
            reviewlist = []
            def get_reviews(soup):
                reviews = soup.find_all('div', {'data-hook': 'review'})
                try:
                    for item in reviews:
                        review = {
                            'product': soup.title.text.replace('Amazon.ca:Customer reviews: ', '').strip(), 
                            'date': item.find('span', {'data-hook': 'review-date'}).text.strip(),
                            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                            'review_list': item.find('span', {'data-hook': 'review-body'}).text.strip(),
                        }
                        reviewlist.append(review)
                except:
                    pass
                
            for x in range(0,100):
                soup = get_soup(url)
                get_reviews(soup)
                if not soup.find('li', {'class': 'a-disabled a-last'}):
                    pass
                else:
                    break

            df = pd.DataFrame(reviewlist)        
            return df 

    def main():
        df1 = fetch_data()
        # df1.to_csv(r'C:/Users/Vicky/Desktop/Web_App_Deployment/Web_App_Deployment/Amazon_reviews_2.csv', index=False)
        

    main()

if __name__ == '__app__':
    app()