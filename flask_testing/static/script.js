// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Select the callFunctionButton by its ID and add a click event listener
    document.getElementById('callFunctionButton').addEventListener('click', function() {
        // Make a GET request to the /call_function endpoint on the Flask server
        fetch('/call_function')
            .then(response => response.json())  // Parse the JSON response
            .then(data => {
                alert(data.message);  // Display the message returned from the Python function
            })
            .catch(error => console.error('Error:', error));  // Log any errors to the console
    });

    // Select the sendTextButton and add a click event listener
    document.getElementById('sendTextButton').addEventListener('click', function() {
        // Get the value from the textbox
        const text = document.getElementById('textBox').value;

        // Make a POST request to the /send_text endpoint on the Flask server
        fetch('/send_prompt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })  // Send the text as JSON
        })
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            alert(data.response);  // Display the response message returned from the Python function
        })
        .catch(error => console.error('Error:', error));  // Log any errors to the console
    });
});
