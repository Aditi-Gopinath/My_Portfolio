
function sendMessage() {
  
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
  

    const alertMessage = `Name: ${username}\nEmail: ${email}\nMessage: ${message}\n\n MESSAGE SENT!!`;
    alert(alertMessage);
  }
  