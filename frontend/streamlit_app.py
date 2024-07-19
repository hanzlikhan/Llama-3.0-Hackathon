import streamlit as st
import requests

backend_url = "http://localhost:5000"

st.title("AI Mental Health Support Platform")

# Chatbot Interaction
st.header("Chat with AI")
user_message = st.text_input("Enter your message:")
if st.button("Send"):
    response = requests.post(f"{backend_url}/chatbot", json={"message": user_message})
    st.write("Bot Response:", response.json().get("response"))

# Sentiment Analysis
st.header("Sentiment Analysis")
sentiment_message = st.text_input("Enter text for sentiment analysis:")
if st.button("Analyze Sentiment"):
    sentiment_response = requests.post(f"{backend_url}/sentiment", json={"text": sentiment_message})
    st.write("Sentiment Analysis Result:", sentiment_response.json())

# Resource Directory
st.header("Resource Directory")
resource_type = st.selectbox("Select resource type:", ["All", "therapist", "support_group"])
if st.button("Get Resources"):
    resources_response = requests.get(f"{backend_url}/resources", params={"type": resource_type.lower()})
    resources = resources_response.json()
    for resource in resources:
        st.write(f"Name: {resource['name']}, Contact: {resource['contact']}")

# Crisis Management
st.header("Crisis Management")
crisis_message = st.text_input("Enter crisis message:")
crisis_phone = st.text_input("Enter phone number for alert:")
if st.button("Send Alert"):
    alert_response = requests.post(f"{backend_url}/crisis", json={"phone": crisis_phone, "message": crisis_message})
    st.write("Crisis Alert Sent")

# User Analytics
st.header("User Analytics")
user_id = st.text_input("Enter User ID to track interactions:")
if st.button("Get User Data"):
    user_data_response = requests.get(f"{backend_url}/user_data", params={"user_id": user_id})
    user_data = user_data_response.json()
    st.write("User Data:", user_data)
