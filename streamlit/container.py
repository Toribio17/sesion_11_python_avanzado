import streamlit as st

container = st.container()
container.write('this is written inside the container')
st.write('This is written outside the container')