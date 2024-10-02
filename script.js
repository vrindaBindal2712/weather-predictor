fetch('http://127.0.0.1:5000', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        temperature: 25,
        humidity: 60,
        wind_speed: 10
    })
})
.then(response => response.json())
.then(data => {
    console.log('Weather prediction:', data.prediction);
})
.catch((error) => {
    console.error('Error:', error);
});
