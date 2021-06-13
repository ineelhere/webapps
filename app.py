import streamlit as st
import pandas as pd
import speedtest
import datetime

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


x = datetime.datetime.now()
st.write(f'Test finished on : {x.strftime("%d")} {x.strftime("%B")} {x.strftime("%Y")} at {x.strftime("%I")}:{x.strftime("%M")}:{x.strftime("%S")} {x.strftime("%p")} \n ### Have a great day!')

