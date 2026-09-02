import streamlit as st


def style_base_layout():
    st.markdown("""
        <style>
        .stApp,
       {
                background: #5865F2 !important;
            }


            
            
        </style>
        """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """, unsafe_allow_html=True) 
    
    
    
    