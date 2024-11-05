// Select the button by its ID and add a click event listener
document.getElementById('callFunctionButton').addEventListener('click', function() {
    // Make a GET request to the /call_function endpoint on the Flask server
    fetch('/call_function')
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            alert(data.message);  // Display the message returned from the Python function
        })
        .catch(error => console.error('Error:', error));  // Log any errors to the console
});
