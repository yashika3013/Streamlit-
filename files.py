import streamlit as st
import pandas as pd

st.subheader('Uploading the csv file')
df = st.file_uploader('Upload the csv file: ',type=['csv','xlxs'])
#st.table(df)

st.subheader("Loading the csv file")
df = pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head(5))

st.subheader('Uploading the imageS:')
st.image('img.png')

st.subheader('Uploading the imageS:')
img = st.file_uploader('upload the image file: ', type = ['png','jpeg'])
if img is not None:
     st.image(img)

st.subheader("Working with videos")
video_f= st.file_uploader("Upload the video file: ",type=['mkv','mp4'])
if video_f is not None:
    st.video(video_f,start_time = 5)

st.subheader('Working with audio')
aud = st.file_uploader('Upload the audio file: ',type=['mp3','wav'])
if aud is not None:
    st.audio(aud.read())
