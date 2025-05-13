import streamlit as st
import pandas as pd


if __name__ == "__main__":
    st.title('Title')
    st.markdown('Markdown')
    st.header('Header')
    st.subheader('Subheader')
    st.caption('Caption')
    st.code('Code = 1234')

    st.divider()

    with st.echo():
        st.write('This code will be printed')

    st.divider()

    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    st.divider()

    st.text('Text')
#streamlit run teste/test.py