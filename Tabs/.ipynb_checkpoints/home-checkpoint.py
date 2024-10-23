import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            In the last two decades, researchers have realized that there is an important relationship between the physical health of an individual and his/her emotional state.Stress is a significant problem of the modern society. It is a growing issue and it has become an inescapable part of our daily lives. The early detection will decrease the damage it costs and prevents it from being chronic.
            Introducing a web application designed to detect and analyze a person's stress level using a Decision Tree Classifier. This app evaluates various features to identify the presence of mental stress and highlights the potential causes of mental ailments due to stress by indicating the most relevant factors. With a focus on accuracy and user-friendly interfaces, the application provides insights into stress levels and contributing factors, helping users manage and understand their mental health better.
        </p>
    """, unsafe_allow_html=True) 