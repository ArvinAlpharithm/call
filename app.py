import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def initiate_call(phone_number, pathway_id, authorization):
    url = "https://api.bland.ai/v1/calls"
    payload = {
        "phone_number": phone_number,
        "pathway_id": pathway_id
    }
    headers = {
        "authorization": authorization,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text

# Streamlit App
st.write("Enter your phone number along with the country code to initiate a call.")

# Input Fields
phone_number = st.text_input("Phone Number (with country code, e.g., +1234567890):")

# Fetch Authorization Token from Environment Variables
authorization = os.getenv("API_KEY")
if not authorization:
    st.error("Authorization token (API_KEY) is not set in the environment variables.")

# Pathway ID (fixed as per your requirement)
pathway_id = "14d756da-d81d-4bdc-bd12-151dc665bdcb"

# Button to Initiate Call
if st.button("Initiate Call"):
    if phone_number and authorization:
        st.write("Initiating call...")
        response = initiate_call(phone_number, pathway_id, authorization)
        st.write("Response from API:", response)
    else:
        st.error("Please enter the phone number and ensure the authorization token is set.")
