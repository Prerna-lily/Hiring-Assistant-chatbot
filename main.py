import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # This will load the API key from your .env file

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get the OpenAI API key from environment variable

# Function to generate questions based on tech stack
def generate_questions(tech_stack):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if available in your plan
            messages=[
                {"role": "system", "content": "You are a hiring assistant generating technical questions."},
                {"role": "user", "content": f"Generate 3-5 technical questions for the following tech stack: {tech_stack}"}
            ]
        )
        questions = response['choices'][0]['message']['content']  # Corrected response structure
        return questions
    except Exception as e:
        return f"Error generating questions: {e}"

# Streamlit UI
st.title("TalentScout Hiring Assistant")
st.markdown("Welcome to the TalentScout Hiring Assistant chatbot. Please provide the required details below.")

# Collect candidate information
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", min_value=0, step=1)
desired_position = st.text_input("Desired Position(s)")
current_location = st.text_input("Current Location")
tech_stack = st.text_area("Tech Stack (e.g., Python, Django, React, MySQL)")

# Submit button
if st.button("Submit"):
    if all([full_name, email, phone, experience, desired_position, current_location, tech_stack]):
        st.success("Thank you! Generating technical questions...")
        questions = generate_questions(tech_stack)
        st.subheader("Technical Questions")
        st.write(questions)  # Display the generated technical questions
    else:
        st.error("Please fill in all the required fields.")

# Graceful ending
st.markdown("Thank you for using the TalentScout Hiring Assistant chatbot!")
