import streamlit as st
from PIL import Image

st.title("トップページ")
st.caption("これはstreamlitのデモアプリです")
st.subheader('自己紹介')
st.text('streamlitの使い方を紹介します。')

code = '''
st.title('Sample app')
st.title("トップページ")
st.caption("これはstreamlitのデモアプリです")
st.subheader('自己紹介')
st.text('streamlitの使い方を紹介します。')
'''
st.code(code, language='python')

image = Image.open('esp32.jpg')
st.image(image, width=400)
