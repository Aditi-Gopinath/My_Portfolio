function sendMessage() {
    
    const mail = document.getElementById('mail').innerText.trim();
    const text = document.getElementById('text').value.trim();

    
    const alertMessage = `Name: ${mail}\nMessage: ${text}\n\n MESSAGE SENT!!`;
    alert(alertMessage);
}

