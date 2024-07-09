from flask import Flask, request, jsonify, render_template
from transformers import pipeline, set_seed
import random


set_seed(42)

# List of possible greetings
greetings = [
    "Hello! How can I assist you today?",
    "Hi there! How may I help you?",
    "Good day! What can I do for you?",
    "Welcome! How can I assist you?",
]

# List of banking-related keywords
banking_keywords = [
    "account", "balance", "transfer", "deposit", "withdrawal",
    "loan", "credit", "debit", "mortgage", "savings", "checking",
    "bank", "atm", "branch", "statement", "interest", "overdraft"
]

# Function to generate a greeting message
def get_greeting():
    return random.choice(greetings)

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load GPT-2 model for conversation generation
generator = pipeline("text-generation", model="gpt2", pad_token_id=50256)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['GET'])
def greeting():
    return jsonify({"response": get_greeting()})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Check if the message contains any banking-related keywords
    if any(keyword in user_message.lower() for keyword in banking_keywords):
        # Generate response using GPT-2 with adjusted parameters
        response = generator(
            user_message, 
            max_length=100, 
            num_return_sequences=1,
            temperature=0.2,  # Adjust temperature for creativity control
            top_k=25,  # Limit to top-k tokens for diversity
            truncation=True
        )
        generated_text = response[0]['generated_text']
        
        # Remove the input message from the generated response
        response_message = generated_text[len(user_message):].strip()
        
        # Find the index of the last period in the response message
        last_period_index = response_message.rfind('.')
        
        # Truncate the response at the last period if it exists
        if last_period_index != -1:
            response_message = response_message[:last_period_index + 1].strip()
        
        # Additional post-processing to remove repetitive phrases
        response_message = ' '.join(dict.fromkeys(response_message.split()))
    else:
        response_message = "Sorry, I can only answer questions related to banking."

    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
