# AI Wedding Planner

This repository contains a Streamlit-based web application that leverages OpenAI's GPT-3.5-turbo model to provide wedding planning advice. Users can input their wedding details such as location, budget, and specific queries to receive tailored recommendations.

## Features

- **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit.
- **Personalized Advice**: Generates customized wedding planning suggestions based on user inputs.
- **Secure API Integration**: Uses OpenAI's API to generate responses while ensuring API key security.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python client library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Anikait10/AI-Wedding-Planner.git
    cd ai-wedding-planner
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API key**:
   - Ensure you securely load your OpenAI API key. Do not hard-code it in the script. Use environment variables or a configuration file.

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the app**:
   - Open your web browser and go to the provided local URL (e.g., http://localhost:8501).
   - Fill in the details
