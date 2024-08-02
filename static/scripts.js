document.addEventListener("DOMContentLoaded", function() {
    fetch('/greeting')
        .then(response => response.json())
        .then(data => {
            displayMessage(data.response, 'bot-message');
        });

    // Add an event listener for the Enter key
    const userInput = document.getElementById('user-input');
    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent form submission
            sendMessage();
        }
    });
});

function displayMessage(message, className) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${className}`;
    messageDiv.innerText = message;
    document.getElementById('messages').appendChild(messageDiv);
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") {
        return; // Do not send empty messages
    }
    displayMessage(userInput, 'user-message');

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, 'bot-message');
    });

    document.getElementById('user-input').value = '';
}
