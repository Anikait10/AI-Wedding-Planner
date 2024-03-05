import streamlit as st
from openai import OpenAI
client = OpenAI()

# Securely load your OpenAI API key
# It is critical to keep your API key secure and not hard-coded in your script.
# openai_api_key = "Your_API_KEY"

def get_wedding_planning_advice(location, budget, query):
    # Initialize OpenAI API client with your API key
    
    full_query = f"You are a wedding planning expert. Based on the following inputs generate a few recommendations for planning a wedding party.\nLocation: {location}\nBudget: {budget}\n{query}"

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a wedding planning expert with creative flair."},
        {"role": "user", "content": "Based on the following inputs generate a few recommendations for planning a wedding party.\nLocation: {location}\nBudget: {budget}\n{query}"}
    ]
    )
    # Call the OpenAI API to generate text using GPT-4
    advice = completion.choices[0].message
    print(advice)
    print(type(advice))
    return advice.content

def main():
    st.title('AI Wedding Planner')

    # Input form
    with st.form("wedding_planner_form"):
        st.write("Please provide details about your wedding to get personalized advice.")
        location = st.text_input("Location (city, country):")
        budget = st.number_input("Budget (in USD):", min_value=1000, max_value=100000, step=500)
        #no of guests, food preferences, style or theme of wedding, no of functions, season(spring, summer, winter, fall)
        query = st.text_area("What do you need help with? For example, 'I'm looking for rustic wedding theme ideas.'")
        submit_button = st.form_submit_button("Get Advice")

        if submit_button:
            advice = get_wedding_planning_advice(location, budget, query)
            structured_advice = advice.split('\n')
            structured_advice = [line for line in structured_advice if line.strip() != '']
            for item in structured_advice:
                st.markdown(f"- {item}")

if __name__ == "__main__":
    main()
