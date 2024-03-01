import streamlit as st
st.title('Title -> Hello Guys, Welcome to my Page')
st.header('Header - > geeks')
st.subheader('SubHeader - > geeks')
st.text('Text -> geeks')

st.markdown('# Hello')
st.markdown('## Hello')
st.markdown('### Hello')
st.markdown('#### Hello')
st.markdown('##### Hello')
st.markdown('Hi')

st.success('Success !')
st.info('Information!')
st.warning('WARNING!')
st.error('Error!')

exp = ZeroDivisionError('Division not possible')
st.exception(exp)

st.exception(ValueError('Value error!'))
st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x = 10\n'
         'for i in range(x):\n'
        '     print(i)')

st.write('Select your hobbies: ')
st.checkbox('Dancing')
st.checkbox('Singing')
st.checkbox('Reading Books')
st.checkbox('Outdoor games')

#st.radio('Select your gender: ',('Male','Female','Other'))
radioButton=st.radio('Select your gender: ',('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write("You're Male")
elif(radioButton == 'Female'):
    st.write("You're Female")
else:
    st.write('You die!')

st.subheader('Select box')
#st.selectbox("Data science: ",['Data analysis','Web scraping','ML','Dl','CV','NLP','Image processing'])
selectBox = st.selectbox("Data science: ",['Data analysis','Web scraping','ML','Dl','CV','NLP','Image processing'])
st.write("You've selected: ",selectBox)

st.subheader('Multi select box: ')
#st.multiselect("Data science: ",['Data analysis','Web scraping','ML','Dl','CV','NLP','Image processing'])
multiSelect = st.multiselect("Data science: ",['Data analysis','Web scraping','ML','Dl','CV','NLP','Image processing'])
st.write("You've selected",len(multiSelect),'courses')


st.subheader('Button')
st.button('Click me')
if(st.button('click me')):
    st.write('Thanks for clicking!')

st.subheader('Slider')
vol = st.slider('Select the Volume level',0,100,step=1)
st.write('Volume is: ',vol)


st.subheader('User input')
uname = st.text_input("Username: ")
passw = st.text_input("Password: ",type='password')

st.subheader('Text area')
st.text_area("Write about yourself in 500 words")

st.subheader('Input number')
st.number_input("Select your age: ",18,100)

st.subheader('input date')
st.date_input("Enter your dob")

st.subheader('Input time')
st.time_input('Time')
