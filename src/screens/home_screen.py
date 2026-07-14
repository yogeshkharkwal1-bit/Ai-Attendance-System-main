import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    st.write("") 
    style_base_layout()
    style_background_home()
    header_home()

    # --- केवल होम स्क्रीन के बॉक्स को छोटा करने वाली CSS ---
    st.markdown("""
        <style>
            /* केवल इस स्क्रीन के कॉलम्स को टारगेट करने के लिए */
            .home-box div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 1.8rem !important;        /* अंदर का गैप थोड़ा कम किया */
                border-radius: 3rem !important;   /* गोल कोने */
                max-width: 320px !important;      /* बॉक्स का साइज छोटा करके 320px किया */
                margin: 0 auto 1.5rem auto !important; /* सेंटर में रखने के लिए */
                text-align: center !important;    /* कंटेंट सेंटर */
            }
            
            /* बॉक्स के अंदर की इमेज को सेंटर करने के लिए */
            .home-box div[data-testid="stColumn"] img {
                display: block !important;
                margin: 0 auto 1rem auto !important;
            }

            /* मोबाइल स्क्रीन के लिए */
            @media (max-width: 768px) {
                .home-box div[data-testid="stColumn"] {
                    max-width: 85% !important;   /* मोबाइल में थोड़ा और छोटा दिखेगा */
                    padding: 1.5rem !important;
                    border-radius: 2rem !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # 1. यहाँ हमने कॉलम्स को एक 'home-box' नाम के कंटेनर में डाल दिया है
    with st.container(key="home_layout"):
        st.markdown('<div class="home-box">', unsafe_allow_html=True) # कस्टम क्लास शुरू
        
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.header("I'm Student")
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
            if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='stud_home_btn'):
                st.session_state['login_type']='student'
                st.rerun()

        with col2:
            st.header("I'm Teacher")
            st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
            if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='teach_home_btn'):
                st.session_state['login_type']='teacher'
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True) # कस्टम क्लास बंद

    footer_home()
