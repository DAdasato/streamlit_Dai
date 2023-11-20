import streamlit as st
st.title('1日消費カロリーメーター')
st.write('これからあなたの消費カロリーを測っていきましょう！')
st.title('一日消費カロリーメーター')
st.write('これからあなたの消費カロリーを測っていきましょう！')
text = st.text_input('今日の移動距離を教えてください')
st.write('今日の移動距離は'+text+'kmです。')
option = st.selectbox('移動方法を教えてください',list(['徒歩','自転車','車、バイク']))
