import streamlit as st

# To run streamlit python script on terminal use streamlit run scriptname.py
# this provides you with a local host address. You can check the website there!

st.header('My First Streamlit App')
name = st.text_input('Enter your name:')
st.markdown(f'your name is: {name}')

uni_list = ["University of Alberta", "University of Toronto",
            "Toronto Met University"]

selected_uni = st.selectbox("select your university",uni_list)
