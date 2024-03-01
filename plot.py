import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
st.subheader('Altair scatter plot')
chart_data = pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

st.subheader('line charts')
df = pd.read_csv('/Users/yashika/geeksforgeeks/Streamlit/ref/lang_data.csv')
lang_list=df.columns.tolist()
lang_choices = st.multiselect("choose your langauge: ",lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader('Areacharts')
st.area_chart(new_df)

st.subheader('Data visualization with plotly')
df = pd.read_csv('/Users/yashika/geeksforgeeks/Streamlit/ref/tips.csv')
st.dataframe(df.head())

st.subheader('Pie chart')
fig = px.pie(df,values = 'total_bill',names = 'sex')
st.plotly_chart(fig)

st.subheader('Pie chart with multiple paramters')
fig = px.pie(df,values = 'total_bill',names = 'day',opacity=.7,
    color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('Histogram')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)
hist_data = [x1,x2,x3]
group_labels = ['Group-1','Group-2','Group-3']
fig = ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)
