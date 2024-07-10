import streamlit as st
import asyncio
from aiconfig import AIConfigRuntime
from openai import OpenAI
client = OpenAI()

# Securely load your OpenAI API key
# It is critical to keep your API key secure and not hard-coded in your script.
openai_api_key = "YOUR_API_KEY_HERE"

def get_wedding_planning_advice(location, budget, guests, food_preferences, style, functions, season, query):
    # Initialize OpenAI API client with your API key
    
    full_query = f"You are a wedding planning expert. Based on the following inputs generate a few recommendations for planning a wedding party.\nLocation: {location}\nBudget: {budget}\nGuests: {guests}\nFood Preferences: {food_preferences}\nWedding Style: {style}\nNo of Functions: {functions}\nPreferred Season: {season}\n{query}"
    print(full_query)
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a wedding planning expert with creative flair."},
        {"role": "user", "content": full_query},
        
    ]
    )
    # Call the OpenAI API to generate text using GPT-4
    advice = completion.choices[0].message
    print(advice)
    print(type(advice))
    return advice.content

async def main():
    st.title('AI Wedding Planner')

    # Input form
    with st.form("wedding_planner_form"):
        st.write("Please provide details about your wedding to get personalized advice.")
        location = st.text_input("Location (city, country):")
        budget = st.number_input("Budget (in USD):", min_value=0, max_value=100000, step=5000)
        guests = st.number_input("Number of Guests:", min_value=1, max_value=1000, step=1)
        food_preferences = st.selectbox("Food Preferences:", ["Vegetarian", "Non-Vegetarian", "Vegan", "Mixed"])
        style = st.selectbox("Style or Theme of Wedding:", ["Rustic", "Modern", "Traditional", "Beach", "Garden"])
        functions = st.number_input("Number of Functions:", min_value=1, max_value=5, step=1)
        season = st.selectbox("Season:", ["Spring", "Summer", "Fall", "Winter"])
        #no of guests, food preferences, style or theme of wedding, no of functions, season(spring, summer, winter, fall)
        query = st.text_area("What do you need help with? For example, 'I'm looking for rustic wedding theme ideas.'")
        submit_button = st.form_submit_button("Get Advice")
        
        
        if submit_button:
            advice = get_wedding_planning_advice(location, budget, guests, food_preferences, style, functions, season, query)
            structured_advice = advice.split('\n')
            structured_advice = [line for line in structured_advice if line.strip() != '']
            for item in structured_advice:
                st.markdown(f"- {item}")
    
    # print("hey I ot here")
    # config = AIConfigRuntime.load('test_wedding planner.aiconfig.json')
    # # model_output = await config.run('prompt_1', params={"location": "New york"})
    # config.update_parameter("temp", "new_value", "prompt_1")
    # config.save()
    # # print(model_output)

if __name__ == "__main__":
    asyncio.run(main())
