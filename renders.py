import streamlit as st

# Custom CSS for button styling
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #001F3F; /* Navy Blue */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    div.stButton > button:first-child:hover {
        background-color: #003366; /* Darker Navy Blue */
    }
    </style>
""", unsafe_allow_html=True)

# Button
if st.button('Code for Single Feature by Combining the 2-3 Features [ RECOMMENDED ]'):
    st.write("Button Clicked!")
