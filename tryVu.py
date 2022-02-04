#from curses import COLOR_CYAN
#code won't run with this^ line 
st.cache 
from sqlite3 import Date
import streamlit as st 
import pandas as pd

st.title("Vugraph Sets")
st.header("SOLOWAY 2019")
st.markdown("DRIJVER BRINK GOOD MATCHES")

#sets = pd.DataFrame({
  #'first column': ["D 2019 Soloway QF - Segment 1 of 4", 2, 3, 4],
  #'second column': ["1/1/22", 20, 30, 40]
#})

st.subheader("15 BOARDS") 

s1 = st.checkbox("D 2019 Soloway QF - Segment 1 of 4")
if s1:
  dates1 = st.date_input("Enter")
s2 = st.checkbox("D 2019 Soloway QF - Segment 2 of 4")
if s2:
  dates2 = st.date_input("")
s3 = st.checkbox("D 2019 Soloway QF - Segment 3 of 4")
if s3:
  dates3 = st.date_input("") 
s4 = st.checkbox("D 2019 Soloway QF - Segment 4 of 4")
if s4:
  dates4 = st.date_input("")
s5 = st.checkbox("A 2019 Soloway SF - Segment 1 of 4")
if s5:
  dates5 = st.date_input("")
s6 = st.checkbox("A 2019 Soloway SF - Segment 2 of 4")
s7 = st.checkbox("A 2019 Soloway SF - Segment 4 of 4")
s8 = st.checkbox("2019 Soloway FINAL - Segment 1 of 4")
s9 = st.checkbox("2019 Soloway FINAL - Segment 2 of 4")
s10 = st.checkbox("2019 Soloway FINAL - Segment 4 of 4")







st.write("hi")
st.checkbox("")
#st.selectbox("",["D 2019 Soloway QF - Segment 1 of 4","D 2019 Soloway QF - Segment 2 of 4"])
#s11
