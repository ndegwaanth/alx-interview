#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie details using the movie ID
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    // Get the list of character URLs
    const characters = movieData.characters;

    // Function to fetch and print each character's name
    const fetchCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject('Error fetching character data:', error);
            return;
          }

          if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            resolve();
          } else {
            reject('Failed to fetch character data');
          }
        });
      });
    };

    // Fetch and print each character's name in sequence
    (async () => {
      for (const characterUrl of characters) {
        await fetchCharacter(characterUrl);
      }
    })();
  } else {
    console.log(`Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});
