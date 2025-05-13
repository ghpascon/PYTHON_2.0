import streamlit as st
import pandas as pd

def get_data():
    return 1,2,3,4,5

if __name__ == "__main__":
    with st.echo():
        data = get_data()
        st.write('This code will be printed')
        st.write(data)


#streamlit run teste/code_runing.py