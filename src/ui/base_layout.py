import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://googleapis.com');
        @import url('https://googleapis.com');

            /* स्ट्रीमलिट का टॉप बार और फुटर छुपाएं */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            /* --- 1. लैपटॉप और बड़ी स्क्रीन्स के लिए स्टाइल (Default) --- */
            .block-container {
                padding-top: 1.5rem !important;    
                padding-left: 5rem !important;
                padding-right: 5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: inherit !important;
            }
                
            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                color: inherit !important;
            }
                
            h3, h4, p, label, span {
                font-family: 'Outfit', sans-serif;    
                color: inherit !important;
            }

            /* इनपुट बॉक्स स्टाइल (हमेशा वाइट रहेगा) */
            div[data-testid="stTextInputRootElement"], 
            div[data-testid="stNumberInputRootElement"],
            div[data-baseweb="input"] {
                background-color: #FFFFFF !important;
                border: 1px solid #CCCCCC !important;
            }
            
            input {
                color: #000000 !important;
                background-color: #FFFFFF !important;
                -webkit-text-fill-color: #000000 !important;
            }

            /* बटन स्टाइल्स */
            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                width: auto !important; /* लैपटॉप में बटन कंटेंट के हिसाब से रहेगा */
            }
            button[kind="secondary"] { background-color: #EB459E !important; border-radius: 1.5rem !important; color: white !important; padding: 10px 20px !important; border: none !important; transition: transform 0.25s ease-in-out !important; }
            button[kind="tertiary"] { background-color: black !important; border-radius: 1.5rem !important; color: white !important; padding: 10px 20px !important; border: none !important; transition: transform 0.25s ease-in-out !important; }
            button:hover { transform: scale(1.05); }


            /* --- 2. मोबाइल स्क्रीन्स के लिए ग्लोबल स्टाइल (768px या उससे कम) --- */
            @media (max-width: 768px) {
                /* पूरे ऐप की साइड पैडिंग को कम करें ताकि कंटेंट स्क्रीन से न चिपके */
                .block-container {
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                    padding-top: 1rem !important;
                }

                /* मोबाइल में H1 का साइज छोटा किया ताकि स्क्रीन से बाहर न जाए */
                h1 {
                    font-size: 2.2rem !important;
                    line-height: 1.2 !important;
                }

                /* मोबाइल में H2 का साइज छोटा किया */
                h2 {
                    font-size: 1.5rem !important;
                    line-height: 1.1 !important;
                }

                /* पैराग्राफ और अन्य टेक्स्ट का साइज थोड़ा छोटा किया */
                p, label, span {
                    font-size: 0.95rem !important;
                }

                /* मोबाइल में बटन को पूरा चौड़ा (Full Width) किया ताकि अंगूठे से दबाने में आसानी हो */
                button, button[kind="secondary"], button[kind="tertiary"] {
                    width: 100% !important;
                    padding: 12px 20px !important; /* मोबाइल के लिए थोड़ा बड़ा क्लिक एरिया */
                    margin-bottom: 0.5rem !important;
                }
                
                /* मोबाइल में जो कॉलम्स अगल-बगल थे, उनके बीच नीचे की तरफ गैप दें */
                div[data-testid="stColumn"] {
                    margin-bottom: 1rem !important;
                }
            }
        </style>  
        """, unsafe_allow_html=True)
