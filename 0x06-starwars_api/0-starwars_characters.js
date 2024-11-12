#!/usr/bin/node

const request = require('request');

/**
 * Promisifies the request function to use with async/await
 * @param {string} url - The URL to make the request to
 * @returns {Promise} Promise object represents the request
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || `Status code: ${response.statusCode}`);
      }
      resolve(JSON.parse(body));
    });
  });
}

/**
 * Gets and prints all character names for a specific Star Wars movie
 * @param {string} movieId - The ID of the movie to get characters from
 */
async function printMovieCharacters(movieId) {
  try {
    const baseUrl = 'https://swapi-api.hbtn.io/api';
    const movieData = await makeRequest(`${baseUrl}/films/${movieId}`);
    const characterUrls = movieData.characters;

    const characterPromises = characterUrls.map(url => makeRequest(url));
    const characters = await Promise.all(characterPromises);

    // Print characters names
    characters.forEach((character, index) => {
      if (index === characters.length - 1) {
        // Last character - no newline
        process.stdout.write(character.name);
      } else {
        console.log(character.name);
      }
    });
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Get movie ID from command line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Execute main function
printMovieCharacters(movieId);
