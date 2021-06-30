import streamlit as st
import pandas as pd
import speedtest
from datetime import datetime
import pytz

st.write("# Internet Connection Speed Test")  
spd = speedtest.Speedtest()
down = spd.download()/1000000
up = spd.upload()/1000000
st.write(f"### Download Speed = {round(down, 2)} mbps")  
st.write(f"### Upload Speed = {round(up, 2)} mbps")
st.write(f"### Other Information :\n")
ip = pd.DataFrame.from_dict(spd.get_config()['client'], orient='index')
# ip = spd.get_config()['client']['ip']
st.table(ip)

IST = pytz.timezone('Asia/Kolkata') 
datetime_ist = datetime.now(IST)
st.write(f"Test finished on - {datetime_ist.strftime('%d/%m/%Y %H:%M:%S %Z')}")

st.write(""" * github: https://github.com/ineelhere/webapps/blob/main/app.py 
* docker: https://hub.docker.com/r/ineelhere/netspeed/ """)

st.write("*Indraneel*")
