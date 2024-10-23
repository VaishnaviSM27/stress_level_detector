import streamlit as st
import warnings
def app():
    """This function creates the home page"""
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Add title to the home page with a larger font size and a brighter color
    st.markdown("<h1 style='text-align: center; color: #3f84b3; font-family: Arial, sans-serif;'>Stress Level Detector</h1>", unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns(2)

    # Add the first image to the first column
    with col1:
        st.image("images/home.png", width=400)

    # Add the second image to the second column
    with col2:
        st.image("images/second_image.png", width=400)

    # Add brief description of your web app with custom styling
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify; margin-bottom: 20px;">
            In the last two decades, researchers have realized that there is an important relationship between the physical health of an individual and his/her emotional state. Stress is a significant problem of the modern society. It is a growing issue and it has become an inescapable part of our daily lives. The early detection will decrease the damage it costs and prevents it from being chronic.
        </p>
        <p style="font-size: 18px; text-align: justify; margin-bottom: 20px;">
            Introducing a web application designed to detect and analyze a person's stress level using a Decision Tree Classifier. This app evaluates various features to identify the presence of mental stress and highlights the potential causes of mental ailments due to stress by indicating the most relevant factors. With a focus on accuracy and user-friendly interfaces, the application provides insights into stress levels and contributing factors, helping users manage and understand their mental health better.
        </p>
        """, unsafe_allow_html=True
    )

    # Add a horizontal line to separate the content
    st.markdown("<hr>", unsafe_allow_html=True)

    # Add a call-to-action message
    st.markdown("<p style='font-size: 18px; text-align: center; margin-bottom: 20px; color: red;'>Get Started<br>Embrace calmness within; detecting stress is the first step to conquering it.</p>", unsafe_allow_html=True)