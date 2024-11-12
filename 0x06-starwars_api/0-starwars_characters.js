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

    // Print each character name with proper formatting
    characters.forEach((character, index) => {
      const name = character.name;
      // For the last character, don't add a newline
      if (index === characters.length - 1) {
        process.stdout.write(name);
      } else {
        process.stdout.write(name + '\n');
      }
    });
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Debug function to show hidden characters
function debugOutput(movieId) {
  return new Promise((resolve) => {
    let output = '';
    const oldWrite = process.stdout.write;
    process.stdout.write = (function(write) {
      return function(string, encoding, fd) {
        output += string;
        write.apply(process.stdout, arguments);
      };
    })(process.stdout.write);

    printMovieCharacters(movieId).then(() => {
      process.stdout.write = oldWrite;
      console.log('\n\nDEBUG INFO:');
      console.log('Length:', output.length);
      console.log('Characters (showing hidden):');
      for (let i = 0; i < output.length; i++) {
        const char = output[i];
        const code = output.charCodeAt(i);
        console.log(`Position ${i}: '${char}' (ASCII: ${code})`);
      }
      resolve();
    });
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Comment out this line and uncomment the one below for normal usage
// printMovieCharacters(movieId);
debugOutput(movieId);
