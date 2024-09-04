import streamlit as st

# Set the title of the web page
st.set_page_config(page_title="Nimbus Insights", page_icon=":office:")

# Custom CSS for buttons and layout
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stSidebar .stRadio>div {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .stSidebar .stRadio>div:hover {
        background-color: #45a049;
    }
    .logo-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
    }
    .logo-container img {
        margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Company Name and Logo
st.title("Welcome to Nimbus Insights")
st.image("static/logo-no-background.png", use_column_width=True)  # Use relative path

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Services", "Contact"])

# Home Page
if page == "Home":
    st.header("Home")
    st.write("""
    Welcome to Nimbus Insights! We are dedicated to providing the best services to our clients.
    Our team of experts is here to help you with all your needs.
    """)

# About Us Page
elif page == "About Us":
    st.header("About Us")
    st.write("""
    **Our Mission**: To deliver high-quality products and services that create value for our customers.

    **Our Vision**: To be the leading company in our industry, known for our innovation and customer satisfaction.

    **Our Values**: Integrity, Excellence, and Teamwork.
    """)

# Services Page
elif page == "Services":
    st.header("Services")
    st.write("""
    We offer a wide range of services to meet your needs:

    - **Consulting**: Expert advice to help you grow your business.
    - **Development**: Custom software solutions tailored to your requirements.
    - **Support**: 24/7 support to ensure your operations run smoothly.
    - **Data Engineering**: Comprehensive data engineering services including:
        - **Snowflake**
        - **Airflow**
        - **AWS**
        - **Azure**
        - **GCP**
    """)

    # Display logos for the technologies
    st.markdown("""
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Snowflake_Logo.svg/330px-Snowflake_Logo.svg.png" width="100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" width="100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width="100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Microsoft_Azure_Logo.svg" width="100">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg" width="100">
    
    </div>
    """, unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.header("Contact Us")
    st.write("Feel free to reach out to us through the following channels:")
    st.write("""
    - **Email**: Hr@NimbusInsights.in
    - **Phone**: +1 234 567 890
    - **Address**: Hyderabad, Hi-Tech, HY 12345
    """)

    # Contact Form
    st.subheader("Send us a message")
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success("Thank you for your message! We will get back to you soon.")

# Footer
st.write("---")
st.write("©Nimbus Insights. All rights reserved.")
