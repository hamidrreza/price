import streamlit as st
import datetime
#import jdatetime
import requests
from bs4 import BeautifulSoup
#import random
#from streamlit_autorefresh import st_autorefresh

##########################################################
url = 'https://tabangohar.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
taban = soup.find('div', id='gram18_price_now').text
##########################################################
url1 = 'https://www.tgju.org/profile/geram18'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
price1= soup1.find('div', class_='fs-cell fs-xl-3 fs-lg-3 fs-md-6 fs-sm-12 fs-xs-12 top-header-item-block-2 mobile-top-item-hide').span.find_next('span').span.text
price11 = price1[:-1].replace(',','')
##forma = format_number(price11, locale='en_US')
##print('tgju : ',forma)
tgju1 = ""
for i in range(len(price11)):
    if i % 3 == 0 and i != 0:
        tgju1 += ","
    tgju1 += price11[len(price11)-1-i]
tgju = tgju1[::-1]
###########################################################
url2 = 'https://arzdigital.com/coins/bitcoin/'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
btc = soup2.find('div', class_='arz-coin-page-data__coin-price coinPrice btcprice pulser-dollar-bitcoin').text
###############################################################################
st.set_page_config(page_title='Gold Price', page_icon=':yellow_circle:', layout='wide')

################################
st.markdown("""
    <style>
    /* تمام نوشته‌ها و عناصر وسط‌چین بشن */
    html, body, .stApp, [class^="css"] {
        text-align: center !important;
        align-items: center !important;
        justify-content: center !important;
    }
    /* همه متن‌ها bold بشن */
    html, body, div, span, h1, h2, h3, h4, h5, h6, p, a, li, td, th, input, label, button, [class^="css"] {
        font-weight: bold !important;
    }
    </style>""", unsafe_allow_html=True)
st.markdown("""
    <style>
        .stApp {
            background-color: #a8d080;  /* سبز ماچایی ملایم */
        }
    </style>""", unsafe_allow_html=True)
#st_autorefresh(interval=1000, key="refresh")
#st_autorefresh(interval=1000, key="time_refresh")
now = datetime.datetime.now()
#date = jdatetime.datetime.fromgregorian(datetime=now)
#date_str = date.strftime("%Y/%m/%d")
time_str = now.strftime("%H:%M")

#st.markdown(
#    f"""
#    <div style="display: flex; justify-content: center; align-items: center; gap: 50px; margin-top: 40px;">
#        <div style="font-size: 40px; font-weight: bold; color: #333;">📅 {date_str}</div>
#        <div style="font-size: 40px; font-weight: bold; color: #333;">⏰ {time_str}</div>
#    </div>
#    """, unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 50px; margin-top: 40px;">
        <div style="font-size: 40px; font-weight: bold; color: #333;">⏰ {time_str}</div>
    </div>
    """, unsafe_allow_html=True)

#st.header('Price of GOLD:')
st.write("---")
#st.markdown(
#    "<h2 style='text-align: center; margin-top: 50px; color: #222;'>Gold 18K Prices</h2>", unsafe_allow_html=True)
st.header('Gold 18K Prices')
#st.markdown(
#    f"""
#    <div style="display: flex; justify-content: center; align-items: center; gap: 60px; font-size: 22px; margin-top: 20px; color: #333;">
#        <div>🌐 <strong>Taban:</strong> {taban}</div>
#        <div>📊 <strong>TGJU:</strong> {tgju} تومان</div>
#    </div>
#   """, unsafe_allow_html=True)
#st.markdown(
#    f"""
#    <div style="display: flex; justify-content: center; gap: 40px; margin-top: 30px;">
#        <div style="background-color: #fff; padding: 25px 30px; border-radius: 15px; box-shadow: 2px 2px 10px #aaa; text-align: center;">
#            <div style="font-size: 20px; font-weight: bold; color: #555;">🌐 Taban</div>
#            <div style="font-size: 28px; font-weight: bold; color: #111; margin-top: 10px;">{taban}</div>
#        </div>
#        <div style="background-color: #fff; padding: 25px 30px; border-radius: 15px; box-shadow: 2px 2px 10px #aaa; text-align: center;">
#           <div style="font-size: 20px; font-weight: bold; color: #555;">📊 TGJU</div>
#            <div style="font-size: 28px; font-weight: bold; color: #111; margin-top: 10px;">{tgju} Toman</div>
#        </div>
#    </div>
#    """, unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    /* Responsive styles */
    .price-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }}

    .price-card {{
        background-color: #fff;
        padding: 25px 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px #aaa;
        text-align: center;
        width: 280px;
        max-width: 90%;
        
    }}

    @media (max-width: 768px) {{
        .price-card {{
            width: 90% !important;
        }}
    }}
    </style>

    <div class="price-container">
        <div class="price-card">
            <div style="font-size: 20px; font-weight: bold; color: #555;">🌐 Taban</div>
            <div style="font-size: 28px; font-weight: bold; color: #111; margin-top: 10px;">{taban}</div>
        </div>
        <div class="price-card">
            <div style="font-size: 20px; font-weight: bold; color: #555;">📊 TGJU</div>
            <div style="font-size: 28px; font-weight: bold; color: #111; margin-top: 10px;">{tgju} تومان</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write('---')




