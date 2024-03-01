import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['Line-1','Line-2','Line-3'])

st.subheader('Line chart')
st.line_chart(chart_data)

st.subheader('Area chart')
st.area_chart(chart_data)

st.subheader('bar chart')
st.bar_chart(chart_data)

st.subheader('Data Visualization with matplotlib and seaborn')

df = pd.read_csv('/Users/yashika/geeksforgeeks/Streamlit/ref/iris.csv')
st.dataframe(df)

st.subheader('Distribution plot')
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution plot with SNS')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.subheader('Multiple Graphs')
col1,col2 = st.columns(2)
with col1:
    col1.header = 'Kde = False'
    fig1=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)

st.subheader('Changing style')
col1,col2 = st.columns(2)
with col1:
    fig=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig)
with col2:
    fig2=plt.figure()
    sns.set_theme(context = 'poster',style='darkgrid')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig2)

st.subheader('Scatter plot')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('count plot')
fig= plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species')
st.pyplot(fig)

st.subheader('box plot')
fig= plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)

st.subheader('violin plot')
fig= plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='species',y='petal_length')
st.pyplot(fig)
