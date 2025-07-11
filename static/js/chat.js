function createSenderChat() {
    // Show the sender's chat when a role is selected
    const role = document.getElementById("role").value;
    if (role) {
        document.getElementById("sender-chat-box-container").style.display = "block";
    }
}

function sendSenderMessage() {
    const message = document.getElementById('sender-message').value;

    if (message.trim() !== "") {
        // Add the sender's message to the sender's chat box
        const senderChatBox = document.getElementById('sender-chat-box');
        const senderMessageElement = document.createElement('p');
        senderMessageElement.textContent = "Sender: " + message;
        senderChatBox.appendChild(senderMessageElement);

        // Also add the sender's message to the user's chat box
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            const userChatBox = document.getElementById('user-chat-box');
            const userMessageElement = document.createElement('p');
            userMessageElement.textContent = "Sender: " + message;
            userChatBox.appendChild(userMessageElement);

            if (data.sensitive) {
                const alertText = document.getElementById('alert-text');
                alertText.textContent = "Sensitive Alert: " + data.sensitive_message;
            }

            document.getElementById('sender-message').value = ""; // Clear the input
        });
    }
}
