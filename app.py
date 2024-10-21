import streamlit as st
import pandas as pd
st.title("application")
st.title("Upload an excel file")
uploaded_file = st.file_uploader("Choose an excel file", type=["xlsx"])
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  st.write("First lines of youre file")
  st.write(df.head())
  st.write("Stats description")
  st.write(df.describe())