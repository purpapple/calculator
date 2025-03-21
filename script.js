function sendNotification() {
    const now = new Date();
    const dateTime = now.toISOString();
    const hostname = window.location.hostname;
    const message = `Website viewed by ${hostname}, at ${dateTime}`;
    const payload = {
        content: message
    };

    fetch('https://discord.com/api/webhooks/1352459587915092099/C2b1InL1AmCWFVC9I1pRxK9LTRMIBrS6CuW1iHGEzWx9nhBa67Zg0_SOCKk83_2_ShlH', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (response.ok) {
            console.log('Notification sent to Discord');
        } else {
            console.error('Failed to send notification');
        }
    })
    .catch(error => {
        console.error('Error sending notification:', error);
    });
}

window.onload = sendNotification;
