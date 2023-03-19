// Make a POST request to the server when the form is submitted
document.getElementById('measurements-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get the form data
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    const waist = document.getElementById('waist').value;
    const hip = document.getElementById('hip').value;

    // Construct the request body
    const requestBody = {
        'measurements': {
            'Height': height,
            'Weight': weight,
            'Waist': waist,
            'Hip': hip
        }
    };

    // Make the POST request to the server
    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify(requestBody),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Update the result element with the predicted size
        const resultElement = document.getElementById('result-container');
        resultElement.innerHTML = `Your recommended clothing size is ${data.size}`;
    });
});
