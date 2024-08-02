# Bank Customer Service Chatbot
## Overview
This project is a web-based chatbot application designed for bank customer service. It uses a fine-tuned GPT-2 model to handle customer inquiries related to banking services. The application includes a Flask server, a fine-tuned GPT-2 model for generating responses, and a simple HTML frontend for user interaction.

## Features
Greeting Endpoint: Provides a random greeting message.

Chat Endpoint: Processes user messages and generates responses based on banking-related queries.

Fine-Tuned Model: GPT-2 model fine-tuned on a banking-related dataset to generate relevant responses.

Simple UI: HTML frontend with input and output areas for user interaction.

## Setup
### Prerequisites
Python 3.6 or later

Flask

Transformers

Datasets

## Installation
Clone the Repository

git clone <repository-url>

cd <repository-directory>

python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt

## Fine-Tune the GPT-2 Model

Run the following script to fine-tune the GPT-2 model:

python fine_tune_model.py

This script will save the fine-tuned model in the ./fine_tuned_model directory.

## Running the Application
Start the Flask Server

python app.py

The server will start on http://127.0.0.1:5000.

Access the Web Interface

Open your web browser and navigate to http://127.0.0.1:5000 to interact with the chatbot.

## Project Structure
app.py: Flask application with endpoints for greetings and chat.

fine_tune_model.py: Script for fine-tuning the GPT-2 model.

templates/: Contains HTML templates.

static/: Contains CSS and JavaScript files.

data/: Contains dataset files (e.g., banking_data.json).
