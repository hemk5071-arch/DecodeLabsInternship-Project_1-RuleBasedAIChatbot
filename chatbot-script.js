document.addEventListener("DOMContentLoaded", () => {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function addMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message");
        messageDiv.classList.add(sender === 'user' ? "user-message" : "bot-message");

        const messageText = document.createElement("p");
        messageText.textContent = message;
        messageDiv.appendChild(messageText);
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;
        addMessage(message, 'user');
        userInput.value = "";

        try{
            const response = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            });
            const data = await response.json();
            addMessage(data.response,'bot');
        }
        catch (error) {
            console.error("Error:", error);
        }

    }
    sendButton.addEventListener("click",sendMessage);
    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});