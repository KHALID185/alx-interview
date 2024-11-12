#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie
 * Usage: ./0-starwars_characters.js <movie_id>
 */
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  let count = 0;

  const printCharacter = function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.error('Error:', error);
        process.exit(1);
      }
      
      const character = JSON.parse(body);
      console.log(character.name);
      count++;

      if (count === characters.length) {
        process.stdout.write('');  // Ensure no trailing newline
      }
    });
  };

  characters.forEach(function (characterUrl) {
    printCharacter(characterUrl);
  });
});
