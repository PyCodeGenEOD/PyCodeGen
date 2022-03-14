import streamlit as st
import pandas as pd
from datetime import datetime as dt
from Functions import *

st.markdown("""

    <style>

footer {visibility: hidden;}

    </style> 
    
""", unsafe_allow_html = True)

padding = 2
st.markdown(f""" 

    <style>

.reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} 
    
    </style> 
    
""", unsafe_allow_html = True)

st.markdown(""" 

    <style> 
    
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.title {
    font-size: 40px; 
    font-family: 'Poppins'; 
    color: #F05F40; 
    line-height: 1;
}

.note {
    font-size: 25px; 
    font-family: 'Poppins'; 
    color: #F05F40; 
    line-height: 1;
}

.text {
    font-size: 16px; 
    font-family: 'Poppins'; 
    color: gray; 
    line-height: 1.2;
} 

.output-titles {
    font-size: 35px; 
    font-family: 'Poppins'; 
    color: #151515; 
    line-height: 1;
}

    </style> 
    
""", unsafe_allow_html = True)

st.sidebar.markdown('<p class="title">PyCodeGen</p>', unsafe_allow_html = True)
st.sidebar.markdown('<p class="text">generate python code to get your desired data from the APIs of EOD Historical Data</p>', unsafe_allow_html = True)

st.sidebar.markdown('')

apis = ['End-Of-Day Historical Stock Data']
api = st.sidebar.selectbox('CHOOSE API', apis, key = 'apis_selectbox')

if api == 'End-Of-Day Historical Stock Data':
    p_expander = st.sidebar.expander('PARAMETERS', expanded = True)
    
    a_exchanges = pd.read_csv('available_exchanges.csv')
    a_exchanges = a_exchanges.set_index('name')
    exchange = p_expander.selectbox('EXCHANGE', a_exchanges.index)
    exchange = a_exchanges.loc[exchange]['code']
    
    a_tickers = pd.read_csv(f'https://eodhistoricaldata.com/api/exchange-symbol-list/{exchange}?api_token={api_key}')[3:].dropna().set_index('Name')
    ticker = p_expander.selectbox('TICKER', a_tickers.index)
    ticker = a_tickers.loc[ticker]['Code']
    start_date = str(p_expander.date_input('STARTING DATE', value = dt(2017,1,1), min_value = dt(2000,1,1)))
    end_date = str(p_expander.date_input('ENDING DATE', value = dt(2022,1,1), min_value = dt(2000,1,1))) 
    period = p_expander.selectbox('PERIOD', ['Daily (d)', 'Weekly (w)', 'Monthly (m)'])
    
    if st.sidebar.button('Generate code'):
        st.markdown('<p class="output-titles">the code</p>', unsafe_allow_html = True)
        st.markdown('')
        code = '''def end_of_day_historical_stockdata(ticker, start_date, end_date, period):
        api_key = 'YOUR API KEY'
        p = period[-2]
        url = f'https://eodhistoricaldata.com/api/eod/{ticker}?api_token={api_key}&from={start_date}&to={end_date}&fmt=json&period={period}'
        raw_df = requests.get(url).json()
        df = pd.DataFrame(raw_df).set_index('date')
        
        return df

'''
        code = code + f"df = end_of_day_historical_stockdata('{ticker}', '{start_date}', '{end_date}', '{period}')"
        st.code(code, language = 'python')
        
        st.markdown('')
        st.markdown('')
        
        st.markdown('<p class="output-titles">the output</p>', unsafe_allow_html = True)
        st.markdown('')
        output_df = end_of_day_historical_stockdata(ticker, start_date, end_date, period) 
        st.dataframe(output_df)
        
        st.markdown('')
        st.markdown('')
        
        st.markdown('<p class="note">note</p>', unsafe_allow_html = True)
        st.markdown("To get the code working properly and produce the same result as shown above, replace YOUR API KEY with your EOD Historical Data secret [API key](https://eodhistoricaldata.com/cp/settings). If you don't have one, [create](https://eodhistoricaldata.com/register) an EOD Historical Data account to access your secret API key")

    else:
        st.info('Select the Generate Code button on the bottom right to view the output')