import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Enroll New Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', use_container_width=True, key='enroll_submit_btn'):
        if join_code:
            res = supabase.table('subjects').select('subject_id,name,subject_code').eq('subject_code', join_code).execute()
            
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_student').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()

                if check.data:
                    st.error('You are already enrolled in this program')
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.toast('Successfully enrolled!', icon='✅')
                    time.sleep(1)
                    st.rerun()
            else:
                st.error('Invalid subject code. Please try again.')
        else:
            st.warning('Please enter a valid code')

    
