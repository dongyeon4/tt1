import matplotlib.pyplot as plt
import streamlit as st
 
fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하십시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 형태를 선택하십시오',['-',':','-.','--'])
m1 = st.sidebar.radio('마커스의 스타일을 선택하시오',['o','^','s','p'])
fig, ax = plt.subplots()

love = []
y = []
for i in range (-20,21,2):
    love.append(i)
    y.append(-2*i*i+3*i+5)

    plt.plot(love,y,color=c1, linestyle=s1, marker=m1)
    st.pyplot(fig)
import sys
sys.exit()

