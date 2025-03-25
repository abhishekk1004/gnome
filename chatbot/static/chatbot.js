document.addEventListener("DOMContentLoaded", function () {
    console.log("Chatbot loaded!");
});

function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");

    let userMessage = document.createElement("div");
    userMessage.classList.add("message", "user");
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);

    document.getElementById("user-input").value = "";

    fetch("/chatbot/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() // CSRF Token for security
        },
        credentials: "same-origin", // Required for CSRF
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("div");
        botMessage.classList.add("message", "bot");
        botMessage.innerText = data.answer;
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Error:", error));
}

// Function to get CSRF token
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1];
}

// Send message when "Enter" key is pressed
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}


