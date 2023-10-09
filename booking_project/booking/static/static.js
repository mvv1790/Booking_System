// booking/static/booking/script.js
document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('/submit_booking/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        alert(JSON.stringify(data));
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
