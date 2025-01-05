import streamlit as st
import pandas as pd
# import numpy as np

st.title('Student Information system')

if 'student_name' not in st.session_state:
    st.session_state.student_name=[]
    
if 'student_score' not in st.session_state:
    st.session_state.student_score=[]
   
name=st.text_input('Enter student name')
score=st.number_input('Enter student score', min_value=20,max_value=100)
# st.write(st.session_state)
# 'before pressing button',st.session_state
df=pd.DataFrame([],columns=['name','score'])
if st.button('Add Student'):
    
     if name and score is not None:
        # Append as a tuple or dictionary
        st.session_state.student_name.append(name)
        st.session_state.student_score.append(score)
        st.success(f"Added: {name} with score: {score}")
        df['name']=st.session_state.student_name
        df['score']=st.session_state.student_score
        
     else:
        st.error("Please enter both name and score!")
st.write('student record')
df
slide_option=st.slider('Filter by score ',min_value=30,max_value=100)
if slide_option:
    st.write('Filter records >=',slide_option)
    filter_data=df[df['score']>=slide_option]
    st.dataframe(filter_data)

# data=pd.read_csv('student_score.csv')
# st.write(data)
# Clear the list button
# if st.button("Clear Student List"):
#     st.session_state.Students.clear()
#     st.warning("Student list cleared.")

    
# st.write("### Student List:")
# for student in st.session_state.Students:
#     st.write(f"**{student['name']}** - Score: {student['score']}")
    