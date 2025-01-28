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
slide_option=st.slider('Filter by score ',min_value=0,max_value=100)
# mininmum_score=50
# if slide_option>=mininmum_score:
#     st.write('Filter records >=',slide_option)
#     st.write('Nice work')
#     filter_data=df[df['score']>=mininmum_score]
#     st.dataframe(filter_data)
# else:
#     st.write('No records found')
minimum_score = 50
filtered_students = []
for student, student_score in zip(st.session_state.student_name, st.session_state.student_score):
    if slide_option >= minimum_score & student_score >= minimum_score:
        filtered_students.append((student, student_score))
        
        # st.write(filtered_students)
        
    else:
        st.write('No records found')
st.write(pd.DataFrame(filtered_students,columns=['name','score']))