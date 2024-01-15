// // script.js

// // Function to fetch Chuck Norris joke from the API
// function fetchChuckNorrisJoke() {
//     // Make a GET request to the Chuck Norris API
//     fetch('https://api.chucknorris.io/jokes/random')
//         .then(response => response.json())
//         .then(data => {
//             // Update the HTML content with the retrieved joke
//             document.getElementById('joke-container').textContent = data.value;
//         })
//         .catch(error => {
//             // Handle any errors that occurred during the fetch
//             console.error('Error fetching Chuck Norris joke:', error);
//             document.getElementById('joke-container').textContent = 'Failed to fetch joke. Please try again later.';
//         });
// }

// // Call the function to fetch and display the Chuck Norris joke
// fetchChuckNorrisJoke();

// // Fetch quotes from the API
// fetch("https://type.fit/api/quotes")
//     .then(response => response.json())
//     .then(data => {
//         // Get a random quote
//         const randomIndex = Math.floor(Math.random() * data.length);
//         const randomQuote = data[randomIndex];

//         // Update the HTML content with the random quote
//         var quoteContainer = document.getElementById('quote-container');
//         var listItem = document.createElement('li');
//         listItem.textContent = randomQuote.text + " - " + randomQuote.author;
//         quoteContainer.appendChild(listItem);
//     })
//     .catch(error => {
//         // Handle errors
//         console.error('Error fetching quotes:', error);
//     });
