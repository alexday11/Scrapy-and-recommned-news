import pickle
import numpy as np
import pandas as pd
import streamlit as st

df = pd.read_csv('./Data/ProcessData.csv')
model = pickle.load(open('./Data/model.pkl','rb'))

st.set_page_config(
    page_title= 'TopNews',
    page_icon= '🎓'
)

st.title(':red[Top News]')


def recommend_news(Head):
    indexs = df[df['title'] == Head].index[0]
    contents = df['new_content'].iloc[indexs]
    pred = model.predict([contents])[0]
    filtered_results = df[df['types'] == pred][['title', 'short_content']].sample(5)

    if not filtered_results.empty:
        for i in range(len(filtered_results)):
            st.markdown("<b>{}</b>".format(pred), unsafe_allow_html=True)
            st.markdown("<h3 style='font-weight: bold;'>{}</h3>".format(filtered_results.iloc[i]['title']), unsafe_allow_html=True)
            st.markdown("{}".format(filtered_results.iloc[i]['short_content']))
            if st.button('Read',key=f'button{i}'):
                st.markdown("<p>{}</p>".format(df.iloc[i]['content']),unsafe_allow_html=True)  
            st.subheader('', divider='red')
    else:
        st.write("No recommended news found for this type.")

def display_news():
    np.random.seed(123)
    data = df.sample(10)
    for i in range(10):
        #st.markdown("<b>{}</b>".format(data.iloc[i]['types']),unsafe_allow_html=True)
        st.markdown("<h3 style='font-weight: bold;'>{}</h3>".format(data.iloc[i]['title']), unsafe_allow_html=True)
        st.markdown("{}".format(data.iloc[i]['short_content']))
        if st.button('Read More',key=f'readmore{i}'):
            st.markdown("<p>{}</p>".format(data.iloc[i]['content']),unsafe_allow_html=True)
            st.header('เนื้อหาข่าวประเภท {}'.format(data.iloc[i]['types']),divider='red')
            recommend_news(data.iloc[i]['title'])
        
        st.subheader('', divider='gray')
        
display_news()